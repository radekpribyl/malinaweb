from __future__ import print_function
import atexit
from webapp import create_app, socketio
from webapp.config import MalinaConfig
from os import environ

#Enable remote debugging
#import ptvsd
#ptvsd.enable_attach(secret = 'malina')

app = create_app(MalinaConfig)

@atexit.register
def robot_cleanup_on_exit():
    print("Robot cleanup")
    app.config["ROBOT"].cleanup()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
