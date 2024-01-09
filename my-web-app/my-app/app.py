#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path

from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=str(Path(__file__).parent))
url = os.environ.get('URL')


@app.route("/user/<username>")
def hello_world(username):
	return render_template("index.html", utc_dt=datetime.utcnow(), username=username, database_url=url)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
