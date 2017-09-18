from __future__ import print_function
import atexit
from webapp import create_app, socketio
from webapp.config import TestingConfig

app = create_app(TestingConfig)

@atexit.register
def robot_cleanup_on_exit():
    print("Robot cleanup")
    app.config["ROBOT"].cleanup()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
