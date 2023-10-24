import chainlit as cl
import os
from dotenv import load_dotenv
from datasets import load_dataset
from haystack.document_stores import InMemoryDocumentStore
from haystack.schema import Document  # Update the import
from haystack.nodes import PromptNode, PromptTemplate, AnswerParser, BM25Retriever
from haystack.pipelines import Pipeline
from haystack.utils import print_answers
import pandas as pd

load_dotenv()

# Load the dataset from the CSV file
ds = pd.read_csv("data/eotc.csv")

# Initialize the document store
document_store = InMemoryDocumentStore(use_bm25=True)
documents = []

# Create Document objects from your CSV data
for index, row in ds.iterrows():
    document = Document(
        content=f"Name: {row['Name']}, Type: {row['Type']}, Location: {row['Location']}, Year: {row['Build in year']}",
        meta={
            "id": index,
            "latitude": row["Latitude"],
            "longitude": row["Longitude"],
            "wikipedia_link": row["Wikipedia link"],
            "picture_link": row["Picture link"]
        }
    )
    documents.append(document)

document_store.write_documents(documents)

# Define a prompt template
prompt_template = PromptTemplate(
    prompt="""
    Answer the question truthfully based solely on the given documents. If there is no answer to the question in the document, just say it is impossible to answer based on the documents provided. Your answer should be no longer than 50 words.
    Documents:{join(documents)}
    Question:{query}
    Answer:
    """,
    output_parser=AnswerParser(),
)

# Add your Hugging Face API token
HF_TOKEN = os.environ.get("HF_TOKEN")

# Initialize the prompt node
prompt_node = PromptNode(
    model_name_or_path="mistralai/Mistral-7B-Instruct-v0.1",
    api_key=HF_TOKEN,
    default_prompt_template=prompt_template
)

# Create the decorator to handle incoming messages
@cl.on_message
async def main(message: str):
    response = await cl.make_async(pipeline.run)(message)

    sentences = response['answers'][0].answer.split('\n')

    if sentences and not sentences[-1].strip().endswith(('.', '?', '!')):
        sentences.pop()  # Remove the last sentence to ensure the response is well-formed

    result = '\n'.join(sentences[1:])

    await cl.Message(author="Bot", content=result).send()

# Initialize the retriever
retriever = BM25Retriever(document_store=document_store, top_k=3)

# Create a pipeline with the retriever and prompt node
pipeline = Pipeline()
pipeline.add_node(component=retriever, name="retriever", inputs=["Query"])
pipeline.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])
