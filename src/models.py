from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, number):
        self.name = name
        self.number = number


    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "name": self.name
        }

class Queue:
 
    def __init__(self):
        self.number = []
        self._queue = []
        self._mode = 'FIFO'

    def __repr__(self):
        return (self._queue)

    def enqueue(self, name, number):
        self._queue.append(name)
        self.number.append(number)
    def dequeue(self):
        pass
    def get_queue(self):
        pass
    def size(self):
        return len(self._queue) 