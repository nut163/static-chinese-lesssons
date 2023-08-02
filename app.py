from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():
    pageTitle = "Welcome to Your 30-Day Chinese Language Journey!"
    pageContent = "Embark on a comprehensive, immersive language program..."
    return render_template('index.html', pageTitle=pageTitle, pageContent=pageContent)

@app.route('/about')
def about():
    pageTitle = "Our Approach"
    pageContent = "Immersion: Use Chinese in a variety of real-world contexts..."
    return render_template('about.html', pageTitle=pageTitle, pageContent=pageContent)

@app.route('/approach')
def approach():
    pageTitle = "Daily Routine"
    pageContent = "Spend 4-5 hours a day on various language activities..."
    return render_template('approach.html', pageTitle=pageTitle, pageContent=pageContent)

@app.route('/daily_routine')
def daily_routine():
    pageTitle = "Our Method"
    pageContent = "Spaced Repetition: Introduce vocabulary and key phrases..."
    return render_template('daily_routine.html', pageTitle=pageTitle, pageContent=pageContent)

@app.route('/method')
def method():
    pageTitle = "Weekly Targets"
    pageContent = "Week 1: Become comfortable with basic greetings..."
    return render_template('method.html', pageTitle=pageTitle, pageContent=pageContent)

@app.route('/weekly_targets')
def weekly_targets():
    pageTitle = "Sign Up"
    pageContent = "Join us now and immerse yourself in this exciting journey..."
    return render_template('weekly_targets.html', pageTitle=pageTitle, pageContent=pageContent)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your user"
    else:
        return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)