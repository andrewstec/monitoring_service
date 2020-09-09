import requests, threading, time

DELAY = 5
MONITOR_URI = 'http://localhost:12345/'

class Monitor():
    def health_check():
        res = requests.get(MONITOR_URI)
        if res.status_code >= 200 and res.status_code < 300:
            print('Success')
        else: 
            print('Failed')
            print(res.text)

class Timer:
    def start():
        print(time.ctime())
        threading.Timer(DELAY, Monitor.health_check).start()

if __name__ == "__main__":
    Timer.start()
