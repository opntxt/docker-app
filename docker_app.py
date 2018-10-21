from flask import Flask
from home.views import home_view
import os


def create_app(config_file):
    app = Flask(__name__)  # Create application object
    app.config.from_pyfile(config_file)  # Configure application with settings file, not strictly necessary
    app.register_blueprint(home_view)  # Register url's so application knows what to do
    return app


if __name__ == '__main__':
    app = create_app('settingslocal.py')  # Create application with our config file
    app.run(host='0.0.0.0', port=int(os.getenv('PORT_NUMBER', 5000)), debug=True, threaded=True)
