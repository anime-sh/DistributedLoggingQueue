from ...myqueue import MyProducer

HOST = "127.0.0.1"
PORT = 5000
base_url = f"http://{HOST}:{PORT}"

p1 = MyProducer(topics=["T-1", "T-2", "T-3"], broker=base_url)

