import sys
import time
import subprocess


class MockModel:
    def predict(self, X):
        return [42.0]


class MockScaler:
    def transform(self, X):
        return X


class MockJoblib:
    def load(self, path):
        if "sc.sav" in path:
            return MockScaler()
        if "lr.sav" in path:
            return MockModel()
        return MockModel()


sys.modules["joblib"] = MockJoblib()

import app  # noqa: E402, F401


def test_server_runs_debug_false():
    process = subprocess.Popen(
        [sys.executable, "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    try:
        time.sleep(2)  # Give server time to start
        assert process.poll() is None, "Server process terminated unexpectedly"
    finally:
        process.terminate()
        process.wait()
