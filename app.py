from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads
import os

app = Flask(__name__)

ENV = 'prod'

photos = UploadSet("photos", IMAGES)

app.config["UPLOADED_PHOTOS_DEST"] = "static/images"
app.config["SECRET_KEY"] = os.urandom(24)
configure_uploads(app, photos)


if ENV == 'dev':
    
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mimamamemima1.@localhost/bucketlistdb'

else:

    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rksleepgjesgyy:ee7c70a72b2c62fa08f3290de35c26a1b450d0ff33b1647a4c484564af4a7333@ec2-52-21-252-142.compute-1.amazonaws.com:5432/d1pihbamilr8ae'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class List(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text())
    image = db.Column(db.String(200))
    location = db.Column(db.String(100))

    def __init__(self, title, description, image, location):
        self.title = title
        self.description = description
        self.image = image
        self.location = location



@app.route('/')
def index():
    data = List.query.all()

    return render_template('index2.html', data=data)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.files['image']
        location = request.form['location']

        
        if title == '' or description == '' or image == '' or location == '':
            data = List.query.all()
            return render_template('index2.html', message='Llena todos los campos', data=data)

        if db.session.query(List).filter(List.title == title).count() == 0:
            image = photos.save(request.files['image'])
            data = List(title, description, image, location)
            db.session.add(data)
            db.session.commit()

    
            data = List.query.all()
            
            return render_template('index2.html', message='Has agregado una nueva actividad', data=data)
        else:
            data = List.query.all()
            return render_template('index2.html', message='Cambia el titulo', data=data)


if __name__== '__main__':
    app.run()
