
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
print("__name__ in flaskblog.py "+ __name__) # __main__ then flaskblog

# when we run python script(file) directly from the python cmd, python calls the
# name of that script __main__


from models import User, Post
app = Flask(__name__)
 

db = SQLAlchemy(app)

 


@app.route("/")
@app.route("/home")
def home():
    return "Home page"

 
print("__name__ in flaskblog.py "+__name__) # __main__
if __name__ == '__main__':
    app.run(debug=True) 
