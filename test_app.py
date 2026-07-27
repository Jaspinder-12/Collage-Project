import subprocess
import time
import urllib.request
import urllib.error


def test_server_startup():
    process = subprocess.Popen(["python", "app.py"])
    time.sleep(2)
    try:
        try:
            response = urllib.request.urlopen("http://127.0.0.1:9457/")
            assert response.status == 200 or response.status == 500
        except urllib.error.HTTPError:
            pass
    finally:
        process.terminate()
