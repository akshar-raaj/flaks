from flask import Flask
from flask import redirect, url_for, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return 'POSTED'
    return render_template('login.html')

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return "Profile for %s" % (username,)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    assert isinstance(post_id, int)
    return "Post %d" % (post_id,)

@app.route('/show_static/')
def show_static_url():
    url = url_for('static', filename='style.css')
    return url

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
