import sqlite3
from flask import Flask, render_template, jsonify
from werkzeug.exceptions import abort
import json

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', data=posts)


@app.route('/about')
def about():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('about.html', data=posts)



@app.route('/data')
def data():
    # conn = get_db_connection()
    # posts = conn.execute('SELECT * FROM posts').fetchall()
    # conn.close()
    local_data = {1: "hello", 2: "hi"}
    # local_data = json.dumps(local_data)
    return jsonify(local_data)

if __name__ == "__main__":
    app.run(debug=True)