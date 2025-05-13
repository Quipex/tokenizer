# setup.py
from setuptools import setup # Removed find_packages from here

setup(
    name="token-counter-cli",    # This is the name pip/pipx will use
    version="0.1.1",            # Increment version for the change
    py_modules=['tokenizer_script'], # CHANGE: Explicitly list your script as a module
    install_requires=[
        "tiktoken",
    ],
    entry_points={
        "console_scripts": [
            # This tells setuptools to create a command 'tokenize'
            # that calls the 'main' function in your 'tokenizer_script.py'
            "tokenize = tokenizer_script:main",
        ],
    },
    author="Gemini 2.5 Pro", # Replace with your name
    author_email="rudas72@gmail.com", # Replace with your email
    description="A command-line tool to count tokens in text files or piped input using tiktoken.",
    long_description=open("README.md").read() if open("README.md", "r", encoding="utf-8") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/token_counter_project", # Optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Environment :: Console",
    ],
    python_requires='>=3.7',
)
