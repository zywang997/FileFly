from flask_script import Manager, Shell, Server
from app.models import UserTable, FileTable
from flask_migrate import Migrate, MigrateCommand, upgrade
from app import create_app, db
from config import config

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, user_table=UserTable, file_table=FileTable)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

config_ = config['default']
IP_ = config_.BASE_HOST.split(":")[1][2:]
PORT_ = int(config_.BASE_HOST.rstrip('/').split(":")[-1])
DEBUG_ = config_.DEBUG
manager.add_command('runserver', Server(use_debugger=DEBUG_, host=IP_, port=PORT_, threaded=4))

@manager.command
def dev():
    pass


@manager.command
def test():
    pass


@manager.command
def deploy():
    from app.models import UserTable
    UserTable.insert_admin()


if __name__ == "__main__":
    manager.run()
    '''
    app.run(host=IP_, port=PORT_, debug=DEBUG_, threaded=4)
    '''
