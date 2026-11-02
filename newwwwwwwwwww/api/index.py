import os
import sys

# Ensure the project root directory is added to sys.path so that
# root modules (app, config, database, analytics, csv_validator) can be imported
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from app import app

# Vercel Serverless Function looks for the `app` WSGI callable
if __name__ == '__main__':
    app.run()
