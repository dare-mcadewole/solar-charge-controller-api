import import_env_file
import os
from flask import Flask
from router import Router
from flask_json import FlaskJSON

app = Flask(__name__)
FlaskJSON(app)

# Setup routes
Router.setup(app)

if __name__ == '__main__':
    # Run Application
    app.run(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        debug=True
    )
