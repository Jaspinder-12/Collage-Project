import subprocess
import time
import requests

def test_debug_mode_disabled():
    # Start the Flask app in a separate process
    process = subprocess.Popen(
        ["python", "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Give the server a moment to start
    time.sleep(2)

    try:
        # Intentionally cause an error to check for Werkzeug debugger by not providing form data
        response = requests.post("http://localhost:9457/predict")
        assert response.status_code == 400  # Bad Request because of missing form data

        # Check if the debugger console is exposed (indicates debug=True)
        assert "Werkzeug Debugger" not in response.text
        assert "console" not in response.text
    finally:
        # Terminate the server
        process.terminate()
        process.wait()
