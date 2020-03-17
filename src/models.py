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

class Queue:
 
    def __init__(self):
        self.numbers = []
        self._queue = []
        self._mode = 'FIFO'

    def __repr__(self):
        return (self._queue)

    def enqueue(self, name, number):
        self._queue.append("kevinnn")
        self.numbers.append(number)

    def dequeue(self):
        self._queue.pop(name)
        self.numbers.pop(number)
   
    def get_queue(self):
        self._queue
   
    def size(self):
        return len(self._queue) 