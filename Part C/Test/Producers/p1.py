from ...myqueue import MyProducer
import random
import time

HOST = "127.0.0.1"
PORT = 5000
base_url = f"http://{HOST}:{PORT}"

p1 = MyProducer(topics=["T-1", "T-2", "T-3"], broker=base_url)

with open("test_asgn1/producer_1.txt", "r") as f:
    for line in f:
        line=line.strip()
        topic = line.split('\t')[-1]
        message= '\t'.join(line.split('\t')[:-1])
        p1.send(topic_name=topic, message=message)
        time.sleep(random.uniform(0,1))