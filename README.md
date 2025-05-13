# Token Counter CLI

A command-line tool to count tokens in text files or piped input using OpenAI's `tiktoken` library.

## Installation

Okay, if you want to install the `tokenize` CLI tool so that it's available for your user account without needing to activate that specific `venv` each time, there are a few ways to do this.

The **highly recommended method** for installing Python CLI applications like this "permanently" for your user is to use a tool called **`pipx`**.

### Recommended Method: Using `pipx`

`pipx` is a tool that lets you install and run Python applications in isolated environments. This means your `tokenize` tool will be available globally for your user, but its dependencies (like `tiktoken`) won't conflict with other Python projects or system Python packages. It's the cleanest and safest way.

**Here's how to do it:**

**1. Install `pipx` (if you haven't already):**

   Open your terminal and run:
   ```bash
   python3 -m pip install --user pipx
   ```
   Then, ensure `pipx`'s install location is in your system's PATH. `pipx` can help you with this:
   ```bash
   python3 -m pipx ensurepath
   ```
   You might need to open a new terminal window or re-source your shell configuration file (e.g., `source ~/.bashrc`, `source ~/.zshrc`) for the PATH changes to take effect. You can verify by typing `pipx --version`.

**2. Navigate to your project directory:**

   Make sure you are in the `token_counter_project` directory where your `setup.py` and `tokenizer_script.py` files are located.
   ```bash
   cd path/to/your/token_counter_project
   ```
   *(If you have the `venv` from the previous steps activated, you can `deactivate` it first, though `pipx` will create its own isolated environment anyway.)*

**3. Install your tool using `pipx`:**

   Now, tell `pipx` to install your local project:
   ```bash
   pipx install .
   ```
   The `.` tells `pipx` to install the package from the current directory (which it finds using your `setup.py`).

   `pipx` will:
   * Create a dedicated, isolated virtual environment just for your `tokenize` tool.
   * Install `tiktoken` and your script into that isolated environment.
   * Add a symbolic link to the `tokenize` command in a directory that's already part of your user's PATH (usually `~/.local/bin`).

**4. Use your command:**

   Now, you should be able to open any new terminal and directly use the `tokenize` command without activating any specific virtual environment:
   ```bash
   tokenize --help
   echo "some text" | tokenize
   ```

**To upgrade or uninstall later with `pipx`:**

* Upgrade: `pipx upgrade token-counter-cli` (using the name from `setup.py`)
* Uninstall: `pipx uninstall token-counter-cli`


## Usage
tokenize [file] [-e ENCODING_NAME_OR_MODEL_NAME]

Examples:
  echo "Hello world" | tokenize
  tokenize my_file.txt
  tokenize my_file.txt -e gpt2