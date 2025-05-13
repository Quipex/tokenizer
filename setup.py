from setuptools import setup, find_packages

setup(
    name="token-counter-cli", # Name of your package
    version="0.1.0",         # Version of your package
    packages=find_packages(),
    install_requires=[
        "tiktoken", # Dependency
    ],
    entry_points={
        "console_scripts": [
            "tokenize = tokenizer_script:main", # Command 'tokenize' will run 'main' function from 'tokenizer_script.py'
        ],
    },
    author="Gemini 2.5 Pro", # Replace with your name
    author_email="rudas72@gmail.com", # Replace with your email
    description="A command-line tool to count tokens in text files or piped input using tiktoken.",
    long_description=open("README.md").read() if open("README.md") else "", # Optional: if you have a README.md
    long_description_content_type="text/markdown", # Optional
    url="https://github.com/yourusername/token_counter_project", # Optional: Replace with your project's URL
    classifiers=[ # Optional metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # Choose an appropriate license
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Environment :: Console",
    ],
    python_requires='>=3.7', # Specify minimum Python version
)
