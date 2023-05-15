import os
import textwrap
import subprocess

def main():
    python_script = os.path.abspath("sleeptimer.py")
    script = textwrap.dedent(f"""\
    #!/bin/sh
    python3 {python_script} $1
    """)

    script_path = "/usr/local/bin/sleeptimer"
    print(f"Create script at [{script_path}]")

    with open(script_path, "w") as f:
        f.write(script)

    print(f"Make script executable")
    subprocess.run(["chmod", "+x", script_path])

    
if __name__ == "__main__":
    main()