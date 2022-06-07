from flask import Flask, Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///test.db'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed= db.Column(db.Integer, default= 0)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id
@app.route('/')
def  home():
    return render_template('index.html')
    
    app.register_blueprint(home, url_prefix= '/')

@app.route('/user/<name>')

def user(name):

    return '<h1>Hello, %s!</h1>' % name
 
@app.route('/signup', methods=['GET', 'POST'])
def  sign_up():
    data = request.form
    print(data)
    return render_template('signup.html')
    
    app.register_blueprint(sign_up, url_prefix= '/')
    
@app.route('/login', methods=['GET', 'POST'])    
def  login():
    data = request.form
    print(data)
    return render_template('login.html')
    
    app.register_blueprint(login, url_prefix= '/')

if __name__ == '__main__':
        
     app.run(debug=True)
         