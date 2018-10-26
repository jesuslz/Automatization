from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/action')
def action():
    return render_template('action.html')

if __name__ == '__main__':
    app.run(debug = True)


#https://www.youtube.com/watch?v=zRwy8gtgJ1A

#https://www.bootstrapcdn.com/
#http://getbootstrap.com/
