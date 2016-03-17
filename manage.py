import os
import sys

from app import create_app
from flask.ext.script import Manager, Command
from werkzeug.serving import run_simple

# Create app
app = create_app()

# Factory app
def load_config(config=None):
    if config:
        app.config.from_object("config." + config)
    else:
        app.config.from_object("config.default")
    return app

# Create script manager
manager = Manager(load_config)
manager.add_option('-c', '--config', help='Configuration')


if __name__ == "__main__":
    manager.run()

