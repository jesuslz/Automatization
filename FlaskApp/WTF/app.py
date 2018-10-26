from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Thisisasecret!'

class loginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
@app.route('/')
def form():
    form = loginForm()
    return render_template('form.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)


'''
https://www.youtube.com/watch?v=vzaXBm-ZVOQ

'''