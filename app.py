from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/ts2931', methods=['GET'])
def tahsina():
    return render_template('tahsina.html')

if __name__ == '__main__':
    app.run()

if __name__ == '__tahsina__':
    app.run()
