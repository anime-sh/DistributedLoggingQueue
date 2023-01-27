# Distributed Logging Queue

## Part A



## Part B
Adding Persistence

## For each topic 

### Topic_Names
	One Field -> topic_name {Supports CreateTopic, ListTopic}
### TopicMessages
	Three fields -> message_id, topic_name, producer_id, message {supports enqueue, dequeue, size}

### TopicOffsets
	Three fields -> consumer_id, topic_name, offset {supports RegisterConsumer, used in deqeue, size}

### TopicProducer
	Two fields -> topic_name, producer_id {used for checking if producer exists for given topic}
