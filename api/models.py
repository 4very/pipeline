import datetime
import time

import peewee

db = peewee.PostgresqlDatabase('postgres',
                               user='postgres',
                               host='db',
                               connect_timeout=5)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Story(BaseModel):
    # TODO: id = peewee.UUIDField or something...
    created = peewee.DateTimeField(default=datetime.datetime.now)
    title = peewee.TextField()
    event_time = peewee.DateTimeField(null=True)
    location = peewee.TextField(null=True)
    section = peewee.TextField(null=True)


class Person(BaseModel):
    created = peewee.DateTimeField(default=datetime.datetime.now)
    name = peewee.TextField()
    slack_handle = peewee.TextField(null=True)
    slack_id = peewee.TextField(null=True)


class Photo(BaseModel):
    created = peewee.DateTimeField(default=datetime.datetime.now)
    photo = peewee.BlobField(null=False)
    mime_type = peewee.TextField(null=False)


class StoryPerson(BaseModel):
    created = peewee.DateTimeField(default=datetime.datetime.now)
    story = peewee.ForeignKeyField(Story, related_name='story_people')
    person = peewee.ForeignKeyField(Person, related_name='story_people')

    class Meta:
        primary_key = peewee.CompositeKey('story', 'person')


class StoryPhoto(BaseModel):
    created = peewee.DateTimeField(default=datetime.datetime.now)
    photo = peewee.ForeignKeyField(Photo, related_name='story_photos')
    story = peewee.ForeignKeyField(Story, related_name='story_photos')

    class Meta:
        primary_key = peewee.CompositeKey('story', 'photo')


class Setting(BaseModel):
    key = peewee.TextField(unique=True)
    value = peewee.TextField(null=True)


def connect():
    # Wait at most 10 seconds for database to come up
    start_time = time.time()
    while True:
        try:
            db.connect()
        except peewee.OperationalError:
            if time.time() - start_time > 10:
                raise
            continue
        break

    # we connected; make our tables
    db.create_tables([Story, Person, Photo, StoryPerson, StoryPhoto, Setting],
                     safe=True)
