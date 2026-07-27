import pytest
import subprocess
import time
import app  # noqa: E402

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client, mocker):
    mocker.patch('app.render_template', return_value="Mocked Template")
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Mocked Template"

def test_app_debug_false():
    process = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)
    try:
        pass
    finally:
        process.terminate()
        stdout, stderr = process.communicate()
        output = stdout.decode() + stderr.decode()
        assert "Debugger is active!" not in output
