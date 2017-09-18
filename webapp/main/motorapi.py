from __future__ import print_function
from flask import current_app
from .. import socketio

 #Websockets
@socketio.on('connect', namespace='/malina')
def client_connect():
    users = current_app.config['CONNECTED_USERS']
    users.add_user()
    print('New client connected: ' + str(users.connected_users))

@socketio.on('disconnect', namespace='/malina')
def client_disconnect():
    users = current_app.config['CONNECTED_USERS']
    users.remove_user()
    print('Client disconnected: ' + str(users.connected_users))

@socketio.on('rychlost', namespace='/malina')
def io_rychlost(data):
    dispatcher = current_app.config['STEERING_DISPATCHER']
    action = data['akce']
    speed = dispatcher.change_speed(action)
    socketio.emit('speed_change', {'rychlost' : speed}, namespace='/malina')
    return speed

@socketio.on('steering', namespace='/malina')
def io_steering(data):
    dispatcher = current_app.config['STEERING_DISPATCHER']
    action = data['akce']
    dispatcher.dispatch(action)

@socketio.on_error('/malina')
def malina_error_handler(e):
    print('An error has occurred: ' + str(e))

@socketio.on_error_default
def default_error_handler(e):
    print('An error has occurred: ' + str(e))
