# RAG Tool - A Haystack, Mistral, and ChainLit-based Question Answering Tool

![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)
## Goal:
The project aims to provide accurate answers to user questions based on the information available in the dataset. 
A powerful and customizable Question Answering (QA) tool that uses Haystack, Mistral, and ChainLit to extract answers from a dataset.

## Table of Contents

- [About](#about)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## About

This project aims to create a custom Question Answering (QA) tool that extracts answers from a dataset. It combines the power of [Haystack](https://github.com/deepset-ai/haystack) for document retrieval, [Mistral](https://mistralai.github.io/) for language modeling, and [ChainLit](https://github.com/chainlit/chainlit) for managing conversations. The tool takes a question and retrieves answers from a dataset, making it suitable for a variety of use cases.

## Project Structure

The project is organized as follows:

- `app/`: Contains the main application code.
  - `app.py`: The main application script.
  - `requirements.txt`: To specify the project's dependencies
- `data/`: Placeholder for csv dataset file
- `research.ipynb/`: Documentation files.
- `examples.txt/`: Example usage scenarios and input/output data.
- `tests.txt/`: Unit tests for the application.

## Getting Started

### Prerequisites

Before you get started, ensure you have the following installed:

- Python 3.9
- virtualenv

### Installation

1. Clone a repository:

   
   git clone https://github.com/shum05/rag_tool_q-a.git

1. Create a virtual environment and activate it:
cd rag-tool
python -m venv venv
venv\Scripts\activate

2. Install project dependencies:
pip install -r app/requirements.txt

3. Set up your dataset:
Place your eotc.csv dataset in data folder

4. Configure the Huggingface environment variables:
Create a .env file in the project root and dehine Hugging Face API key HF_TOKEN=...

5. Start the RAG Tool:
chainlit run app/app.py

## Usage
Access the tool by opening your web browser and navigating to http://localhost:8000.

Enter a question in the input box and click "Submit" icon

View the answers generated based on the dataset.

## Features
Customizable prompt templates for generating answers.
Document retrieval using BM25.
Integration with Hugging Face models.
Conversational interface for multiple questions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
