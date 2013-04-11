from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello/')
def hello_world():
    return 'Hello World!'

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
