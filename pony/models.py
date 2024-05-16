from django.db import models
from pony.orm import Database, Required

db = Database()


class Post(db.Entity):
    title = Required(str)
    content = Required(str)
    author = Required(str)

    def __str__(self):
        return self.title

"""
https://blog.stackademic.com/integrating-pony-orm-with-django-6fa7377df668
"""
