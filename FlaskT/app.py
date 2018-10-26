from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    names = {'name1' : 'Jesus', 'name2' : 'Lucero'}
    items = [{'text' : 'uno'}, {'text' : 'dos'}, {'text' : 'tres'}]
    return render_template('layout.html', name = names, var = False, entorno1 = 'Python', entorno2 = 'Flask', items = items)

if __name__ == '__main__':
    app.run(debug=True)