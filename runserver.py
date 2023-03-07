"""
This script runs the NetworkSec application using a development server.
"""

from os import environ
from NetworkSec import app

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
