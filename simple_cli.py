import os
import sys

def handle_echo(command):
    """Handle the echo command."""
    message = command[1:]
    sys.stdout.write(f"{' '.join(message)}\n")
    sys.stdout.flush()

def handle_type(command, path_env, builtin_cmds):
    """Handle the type command."""
    cmd = command[1]
    paths = path_env.split(':')
    cmd_path = next((f"{path}/{cmd}" for path in paths if os.path.isfile(f"{path}/{cmd}")), None)

    if cmd in builtin_cmds:
        sys.stdout.write(f"{cmd} is a shell builtin\n")
    elif cmd_path:
        sys.stdout.write(f"{cmd} is {cmd_path}\n")
    else:
        sys.stdout.write(f"{cmd}: not found\n")
    sys.stdout.flush()

def handle_pwd():
    """Handle the pwd command."""
    sys.stdout.write(f"{os.getcwd()}\n")
    sys.stdout.flush()

def handle_cd(command):
    """Handle the cd command."""
    try:
        path = command[1]
        if path.startswith("/") or path.startswith("."):
            absolute_path = os.path.normpath(os.path.join(os.getcwd(), path))
            os.chdir(absolute_path)
        elif path.startswith("~"):
            os.chdir(os.path.expanduser(path))
        else:
            sys.stdout.write(f"{path}: unsupported path\n")
    except FileNotFoundError:
        sys.stdout.write(f"{path}: No such file or directory\n")
    except PermissionError:
        sys.stdout.write(f"{path}: Permission denied\n")
    sys.stdout.flush()

def execute_external_command(command, path_env):
    """Execute an external command if it exists."""
    cmd_name = command[0]
    for path in path_env.split(':'):
        cmd_path = f"{path}/{cmd_name}"
        if os.path.isfile(cmd_path):
            os.system(' '.join([cmd_path] + command[1:]))
            return True
    return False

def main():
    """Main function to run the shell."""
    builtin_cmds = ["echo", "exit", "type", "pwd", "cd"]
    path_env = os.environ.get("PATH", "")

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            user_input = input().strip()
        except EOFError:
            break

        if not user_input:
            continue

        command = user_input.split()
        cmd_name = command[0]

        if cmd_name == "exit":
            if len(command) > 1 and command[1].isdigit() and int(command[1]) == 0:
                break
            else:
                sys.stdout.write("exit: invalid argument\n")
                sys.stdout.flush()
                continue

        if cmd_name == "echo":
            handle_echo(command)
        elif cmd_name == "type":
            handle_type(command, path_env, builtin_cmds)
        elif cmd_name == "pwd":
            handle_pwd()
        elif cmd_name == "cd":
            handle_cd(command)
        else:
            if not execute_external_command(command, path_env):
                sys.stdout.write(f"{cmd_name}: command not found\n")
                sys.stdout.flush()

if __name__ == "__main__":
    main()

