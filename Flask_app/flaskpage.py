from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from CSV_XML import Process_CSV_XML
from Visualisation import graphLanguage, graphMarital
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# TODO: class of patients and observations

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


def generate_visuals_dict():
    visuals = []
    graphLanguage()
    graphMarital()
    directory = r'./static/graphs_output'
    for filename in os.listdir(directory):
        title = filename[: filename.index(".")]
        visuals.append({"title": title,
                        "content": f"../static/graphs_output/{filename}"
                        })

    return visuals


# TODO: allow users to choose fields by UI
choose_fields = Process_CSV_XML(init_patients_page=3, patient_uuid=True, name=True, telecom=True, gender=True,
                                birthdate=True, address=True, marital=True, language=True)

# dictionary format that goes into home.html
patients = choose_fields.generate_dictionary()

visuals = generate_visuals_dict()


@app.route("/")
@app.route("/home")
def home():
    # TODO: Extend
    # posts = Post.query.all()
    return render_template('home.html', patients=patients)


@app.route('/home')
def file_downloads():
    try:
        return render_template('home.html')
    except Exception as e:
        return str(e)


@app.route('/return-csv/')
def return_csv():
    try:
        choose_fields.generate_csv("patient.csv")
        return send_file('static/CSV_output/patient.csv', attachment_filename='patient.csv')
    except Exception as e:
        return str(e)


@app.route('/return-xml/')
def return_xml():
    try:
        choose_fields.generate_xml("patient.xml")
        return send_file('static/XML_output/patient.xml', attachment_filename='patient.xml')
    except Exception as e:
        return str(e)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/graphs")
def graphs():
    return render_template('graphs.html', visuals=visuals, title='Graphs')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
