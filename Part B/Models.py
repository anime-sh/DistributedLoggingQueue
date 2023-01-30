from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TopicName(db.Model):
    __tablename__ = 'TopicName'
    topic_name = db.Column(db.String(), primary_key=True)

    def __init__(self, topic_name):
        self.topic_name = topic_name

    def __repr__(self):
        return f"{self.topic_name}"

    def ListTopics(self):
        return TopicName.query.all()

    def CreateTopic(self, topic_name):
        topic = TopicName(topic_name)
        db.session.add(topic)
        db.session.commit()

    def CheckTopic(self, topic_name):
        topic = TopicName.query.filter_by(topic_name=topic_name).first()
        return True if topic else False


class TopicMessage(db.Model):
    __tablename__ = 'TopicMessage'
    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(), db.ForeignKey('TopicName.topic_name'))
    producer_id = db.Column(db.String())
    message = db.Column(db.String())

    def __init__(self, topic_name, producer_id, message):
        self.topic_name = topic_name
        self.producer_id = producer_id
        self.message = message

    def addMessage(self, topic_name, producer_id, message):
        # check if topic exists
        if not TopicName.CheckTopic(topic_name):
            raise Exception("Topic does not exist")

        topic = TopicMessage(topic_name, producer_id, message)
        db.session.add(topic)
        db.session.commit()

    def retrieveMessage(self, topic_name, offset):
        left_messages = self.getSizeforTopic(topic_name, offset)
        if (offset > left_messages):
            return -1
        data = TopicMessage.query.filter_by(
            topic_name=topic_name).sort_by(id).offset(offset).first()
        return data.message

    def getSizeforTopic(topic_name, offset):
        # offset is 0-indexed
        return TopicMessage.query.filter_by(topic_name=topic_name).count() - offset - 1

    def __repr__(self):
        return f"{self.id} {self.topic_name} {self.producer_id} {self.message}"

class TopicOffsets(db.Model):
    consumer_id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(), db.ForeignKey('TopicName.topic_name'))
    offset = db.Column(db.Integer)

    def __init__(self, consumer_id, topic_name):
        self.consumer_id = consumer_id
        self.topic_name = topic_name
        self.offset = 0

    def getOffset(consumer_id):
        return TopicOffsets.query.filter_by(consumer_id=consumer_id).first().offset

    def IncrementOffset(consumer_id):
        offset = TopicOffsets.getOffset(consumer_id)
        TopicOffsets.query.filter_by(consumer_id=consumer_id).update(
            {TopicOffsets.offset: offset + 1})
        db.session.commit()

    def getTopicName(consumer_id):
        return TopicOffsets.query.filter_by(consumer_id=consumer_id).first().topic_name

    def registerConsumer(consumer_id, topic_name):
        if not TopicName.CheckTopic(topic_name):
            raise Exception("Topic does not exist")
        consumer = TopicOffsets(consumer_id, topic_name)
        db.session.add(consumer)
        db.session.commit()

    def checkConsumer(consumer_id):
        return TopicOffsets.query.filter_by(consumer_id=consumer_id).count() != 0

    def __repr__(self):
        return f"{self.consumer_id} {self.topic_name} {self.offset}"

class TopicProducer(db.Model):
    producer_id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String())

    def __init__(self, producer_id, topic_name):
        self.producer_id = producer_id
        self.topic_name = topic_name

    def registerProducer(producer_id, topic_name):  
        if not TopicName.CheckTopic(topic_name):
            raise Exception("Topic does not exist")
        producer = TopicProducer(producer_id, topic_name)
        db.session.add(producer)
        db.session.commit()

    def checkProducer(producer_id):
        return TopicProducer.query.filter_by(producer_id=producer_id).count() != 0

    def __repr__(self):
        return f"{self.producer_id} {self.topic_name}"


def return_objects():
    return TopicProducer(), TopicMessage(), TopicName(), TopicOffsets()