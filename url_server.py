from flask import Flask, render_template, url_for, redirect, request, Response, jsonify
import sqlite3
import database
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add():
	long_url = request.form["long_url"]
	short_url = request.form["short_url"]
	conn = sqlite3.connect('smallurl.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO urlshort (longurl, shorturl) VALUES (?, ?)", (long_url, "http://localhost:5000/"+short_url))
	conn.commit()
	detail = {"long_url": long_url, "short_url": short_url}
	return jsonify(detail)
	
	










if __name__ == '__main__':
	app.run(debug=True)

