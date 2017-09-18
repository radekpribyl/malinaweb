from flask import Flask
from flask_socketio import SocketIO
from .connected_users import ConnectedUsers
from .steering_dispatcher import SteeringDispatcher

socketio = SocketIO()

def create_app(appconfig):
    app = Flask(__name__)
    app.config.from_object(appconfig)
    app.config['CONNECTED_USERS'] = ConnectedUsers(app.config['ROBOT'], socketio)
    app.config['STEERING_DISPATCHER'] = SteeringDispatcher(app.config['ROBOT'])
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
