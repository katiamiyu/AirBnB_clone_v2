#!/usr/bin/python3
"""lunch a flask web application run at port 5000
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """display a static string when queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
