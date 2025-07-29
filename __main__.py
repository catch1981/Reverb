import os
import runpy
import argparse
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description="Launch the Hecate API server")
    parser.add_argument(
        "-b",
        "--background",
        action="store_true",
        help="Run the server in the background",
    )
    args = parser.parse_args()

    current_dir = os.path.dirname(__file__)
    script = os.path.join(current_dir, "OK workspaces", "main.py")

    if args.background:
        cmd = [sys.executable, script, "-b"]
        subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
        )
        print("Server started in background")
    else:
        runpy.run_path(script, run_name="__main__")

if __name__ == "__main__":
    main()
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'MandemOS Hecate online.'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # 👈 uses Railway's port
    app.run(host='0.0.0.0', port=port)
