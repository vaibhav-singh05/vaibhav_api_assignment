import subprocess
import webbrowser
import time
import os

# Start FastAPI backend
backend = subprocess.Popen(["uvicorn", "app.main:app", "--reload"])

# Wait a few seconds for the server to start
time.sleep(3)

# Open frontend in default browser
frontend_path = os.path.abspath("frontend/index.html")
webbrowser.open(f"file:///{frontend_path}")

# Wait for backend process to finish (Ctrl+C to stop)
try:
    backend.wait()
except KeyboardInterrupt:
    backend.terminate() 