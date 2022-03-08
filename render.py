from flask import Flask

import data_

app = Flask(__name__)

@app.route('/')
def forwardslash():
    return 'Hello World'
