from ...myqueue import MyConsumer
HOST = "127.0.0.1"
PORT = 5000
base_url = f"http://{HOST}:{PORT}"

c2 = MyConsumer(topics=["T-1",  "T-3"], broker=base_url)

while True:
    c2.get_next("T-1")
    c2.get_next("T-3")
    