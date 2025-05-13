# Token Counter CLI

A command-line tool to count tokens in text files or piped input using OpenAI's `tiktoken` library.

## Installation
(Instructions will be added here if you distribute it)

## Usage
tokenize [file] [-e ENCODING_NAME_OR_MODEL_NAME]

Examples:
  echo "Hello world" | tokenize
  tokenize my_file.txt
  tokenize my_file.txt -e gpt2