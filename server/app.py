#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return {'message': '200: Successfully cleared session data.'}, 200

@app.route('/articles')
def index_articles():
    # Implement logic to receive and render articles.
    return jsonify({"message": 'Article endpoint'})


@app.route('/articles/<int:id>')
def show_article(id):
    # Initialize page_views if it's the first request
    session['page_views'] = session.get('page_views', 0) + 1
    
    # Check if the user has viewed more than 3 pages
    if session['page_views'] > 3:
        # Render JSON response fro exceeding page views
        return jsonify({"message": "Maximum pageview limit reached"}), 401
    
    # Retrieve article data (replace this with actual logic to get article data)
    article_data = {'author': id, 'title': id, 'content': id, 'preview': id, 'minutes_to_read': id, 'date': id}
    
    # Render JSON response with article data
    return jsonify(article_data)
    

if __name__ == '__main__':
    app.run(port=5555)
