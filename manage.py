import os
from api import create_app
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from models import db

app_settings = os.getenv('APP_SETTINGS', 'config.local.Development')
app = create_app(app_settings)
migrate = Migrate(app, db)
manager = Manager(app)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

PORT = os.getenv("SERVE_PORT", "5003")

manager.add_command("runserver", Server(host='0.0.0.0',port=PORT))

if __name__ == '__main__':
    manager.run()
