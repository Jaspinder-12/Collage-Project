import time
import requests
import threading
import multiprocessing
from app import app
import os

def run_server():
    app.run(port=9457)

def benchmark():
    # Allow server to start
    time.sleep(2)

    url = 'http://127.0.0.1:9457/predict'
    data = {
        'item_weight': '9.3',
        'item_fat_content': '0',
        'item_visibility': '0.016',
        'item_type': '4',
        'item_mrp': '249.8',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }

    start_time = time.time()
    for _ in range(100):
        try:
            requests.post(url, data=data)
        except Exception as e:
            print(f"Request failed: {e}")
    end_time = time.time()

    print(f"Total time for 100 requests: {end_time - start_time:.4f} seconds")
    print(f"Average time per request: {(end_time - start_time) / 100:.4f} seconds")

if __name__ == '__main__':
    # Start server in a separate process
    server_process = multiprocessing.Process(target=run_server)
    server_process.start()

    try:
        benchmark()
    finally:
        server_process.terminate()
        server_process.join()
