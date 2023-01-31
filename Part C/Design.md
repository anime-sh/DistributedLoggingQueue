responsibility of Class MyProducer

- Constructor (topics : ["t1", "t2"]), broker="localhost:9092")
- send(topic_name, log message)
- add_topic(topic_name)

responsibility of Class MyConsumer
- Constructor (topics : ["t1", "t2"]), broker="localhost:9092")
- get_next(topic_name) implemented as generator (not sure how)
- add_topic(topic_name)

Design decision: whether to allow topic addition after register