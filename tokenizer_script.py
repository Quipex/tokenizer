#!/usr/bin/env python3
# tokenizer_script.py

import sys
import argparse
import tiktoken

def count_tokens(text, encoding_name="cl100k_base"):
    """
    Counts the number of tokens in a given text using the specified tiktoken encoding.

    Args:
        text (str): The text to tokenize.
        encoding_name (str): The name of the encoding to use (e.g., "cl100k_base", "p50k_base", "gpt2").
                             Can also be a model name like "gpt-4", "gpt-3.5-turbo".

    Returns:
        int: The number of tokens, or None if an error occurs.
    """
    try:
        # Attempt to get encoding by model name first
        try:
            encoding = tiktoken.encoding_for_model(encoding_name)
        except KeyError:
            # If model name not found, try as a direct encoding name
            encoding = tiktoken.get_encoding(encoding_name)
        
        tokens = encoding.encode(text)
        return len(tokens)
    except KeyError as e:
        # This handles cases where encoding_for_model fails and get_encoding also fails for the name
        print(f"Error: No encoding found for '{encoding_name}'. {e}", file=sys.stderr)
        # You can list available models/encodings if desired, but it can be long.
        # For simplicity, just printing the error.
        return None
    except Exception as e:
        print(f"Error during tokenization: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to handle argument parsing and input/output.
    """
    parser = argparse.ArgumentParser(
        description="Count tokens in a file or from stdin using tiktoken.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  echo "Hello world" | tokenize
  tokenize my_file.txt
  tokenize my_file.txt -e gpt2
  cat my_file.txt | tokenize -e p50k_base
"""
    )
    parser.add_argument(
        "file",
        nargs="?",  # 0 or 1 argument
        type=str,
        help="Path to the text file to tokenize. Reads from stdin if not provided."
    )
    parser.add_argument(
        "-e", "--encoding",
        type=str,
        default="cl100k_base", # Default encoding for models like gpt-3.5-turbo, gpt-4
        help=(
            "The tiktoken encoding name or model name to use.\n"
            "Common encodings: cl100k_base, p50k_base, r50k_base (or gpt2).\n"
            "Model names: gpt-4, gpt-3.5-turbo, text-davinci-003, etc.\n"
            "Default: cl100k_base"
        )
    )

    args = parser.parse_args()

    input_text = ""

    if args.file:
        # Read from file
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                input_text = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file {args.file}: {e}", file=sys.stderr)
            sys.exit(1)
    elif not sys.stdin.isatty():
        # Read from stdin (pipe)
        input_text = sys.stdin.read()
    else:
        # No file and no pipe - show help
        parser.print_help(sys.stderr)
        print("\nError: No input file provided and no data piped from stdin.", file=sys.stderr)
        sys.exit(1)

    if not input_text.strip() and args.file:
        # File was provided but is empty or whitespace only
        print(0) # An empty file has 0 tokens
        sys.exit(0)
    elif not input_text.strip() and not args.file and not sys.stdin.isatty():
        # Piped input was empty or whitespace only
        print(0)
        sys.exit(0)


    token_count = count_tokens(input_text, args.encoding)

    if token_count is not None:
        print(token_count)
    else:
        sys.exit(1) # Exit with error if token counting failed

if __name__ == "__main__":
    main()
