from ...myqueue import MyConsumer
HOST = "127.0.0.1"
PORT = 5000
base_url = f"http://{HOST}:{PORT}"

c1 = MyConsumer(topics=["T-1", "T-2", "T-3"], broker=base_url)

while True:
    print(c1.get_next("T-1"))
    print(c1.get_next("T-2"))
    print(c1.get_next("T-3"))
    