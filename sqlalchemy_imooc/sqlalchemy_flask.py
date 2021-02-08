from flask import Flask, escape, url_for, render_template

app = Flask(__name__)


@app.route('/')
def test_name():
    return 'index'


@app.route('/hello/')
@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name='ppx'):
    return render_template('hello.html', name=name)


with app.test_request_context():
    print(url_for('test_name', name='ppx'))
    print(url_for('hello', name='dylan'))

if __name__ == "__main__":
    app.run(debug=True)
