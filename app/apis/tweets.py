# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository
from flask import jsonify
import json

api = Namespace('tweets')

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else: 
            tweet_id = {"id": tweet.id, "text": tweet.text, "created_at": tweet.created_at}
            return jsonify(tweet_id)
