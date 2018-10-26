from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def helloworld():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

#https://geekytheory.com/aprende-flask-introduccion-y-hola-mundo
#https://code.tutsplus.com/es/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
#https://www.youtube.com/watch?v=zRwy8gtgJ1A
