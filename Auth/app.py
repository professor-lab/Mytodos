from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import bcrypt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.string(100))

    def __init__(self,email,password):
        self.email=email
        self.password=bcrypt.haspw(password.encode('utf-8'),bcrypt.getsalt()).decode('utf-8')
        super().__init__()



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        #reuest handal
        pass   
    return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')
    



if __name__ == '__main__':
    app.run(debug=True)
    