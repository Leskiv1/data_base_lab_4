import requests
import threading
import time

# URL REST-сервісу
url = "http://second-1119110736.eu-north-1.elb.amazonaws.com/api/operators"

# Кількість одночасних потоків
threads_count = 100  # збільшено для значного навантаження
# Час між запитами в секундах
delay = 0.3  # майже без паузи

def send_requests():
    while True:
        try:
            response = requests.get(url, headers={"accept": "application/json"})
            print(f"Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(delay)

threads = []

for _ in range(threads_count):
    t = threading.Thread(target=send_requests)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

