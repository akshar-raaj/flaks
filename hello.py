from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

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
