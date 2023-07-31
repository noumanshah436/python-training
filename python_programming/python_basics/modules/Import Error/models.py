
from flaskblog import db    # circular import  ( cannot import name 'User' from partially initialized module 'models' )
# from __main__ import db   # cannot import name 'db' from '__main__'

# ************

# when we run python script(file) directly from the python cmd, python calls the
# name of only that  script  __main__ , so the current name of file is undefined

# wo flaskblog ko janta hi nhi (because of direct run ), is liye wo dobara ise run krta ha
# lekin wo __main__ ko janta ha is liye usi jaga error deta ha

# lekin jb wo 2osri dfa flaskblog run krta ha tw , wo models file ko janta ha ,
# because k wo direct run nhi hoi , or error de deta ha k ye partially initialized module ha.


# ************


class User(db.Model):   # this type of class also called a model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
