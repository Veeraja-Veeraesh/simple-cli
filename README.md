# Simple Command Line Interface

This repository contains a simple shell emulator implemented in Python. The shell provides basic functionalities such as executing built-in commands, navigating the filesystem, and running external commands.

## Features

- **Built-in Commands**:
  - `echo`: Prints the provided message to the console.
  - `pwd`: Displays the current working directory.
  - `cd`: Changes the current working directory. Supports relative, absolute, and home directory paths.
  - `type`: Displays the type of a command (builtin or external).
  - `exit`: Exits the shell. Optionally accepts `0` as an argument for a clean exit.
  
- **External Command Execution**: 
  - Executes commands found in directories listed in the `PATH` environment variable.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/python-shell-emulator.git
   cd python-shell-emulator
   ```

2. Run the shell emulator
   ```
   python shell_emulator.py
   ```

3. Interact with the shell by typing commands:
   ```
   $ echo Hello, World!
   Hello, World!

   $ pwd
   /home/user/python-shell-emulator

   $ cd ..
   $ pwd
   /home/user

   $ type echo
   echo is a shell builtin
   ```

4. Exit the shell:
   ```
   $ exit 0
   ```

## Requirements
- Python 3.x

## Limitations
- Limited to basic command-line functionalities.  
- Assumes a Unix-like environment (e.g., Linux, macOS) for PATH handling and command execution.
- Does not handle advanced shell features like pipes, redirection, or background processes.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request for improvements or new features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

bash
Copy code
$ exit 0

