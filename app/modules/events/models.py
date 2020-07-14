# encoding: utf-8

from .. import db

class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(200))
    event_date = db.Column(db.String(20))
    date = db.Column(db.DateTime())
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):

        return '<Event: {0}>'.format(self.name)
        
    @staticmethod
    def create(name, description, event_date, date):
        
        event = Event(name=name, description=description, event_date=event_date, date=date)
        
        db.session.add(event)
        db.session.commit()
        
        return event
        
    @staticmethod
    def update(self, _id, values):
    
        event = Event.query.filter_by(id=_id).update(values)
        db.session.commit()
    
    @staticmethod
    def delete(self, _id):
    
        todo = ToDo.query.filter_by(id=_id).first()
        db.session.delete(todo)
        db.session.commit()