import threading

class ConnectedUsers(object):

    def __init__(self, robot, sockio):
        self._connected_users = 0
        self._sockio = sockio
        self._lock = threading.Lock()
        self._robot = robot
        self._distance_sensor = robot.components["distance_sensor"]
        self._left_obstacle_sensor = robot.components["obstacle_left"]
        self._right_obstacle_sensor = robot.components["obstacle_right"]

    def add_user(self):
        with self._lock:
            self._connected_users += 1
            if (self._connected_users > 0
                and self._robot.is_robot_initiated
                and not self._distance_sensor.measure_running.is_set()):

                # self._distance_sensor.start_distance_measure(
                #     lambda dist: self._sockio.emit('sensors',
                #     {'sensor':'distance', 'value':dist}, namespace='/malina'))

                self._left_obstacle_sensor.register_both_callbacks(
                    lambda pin, state: self._sockio.emit('sensors', {'sensor':'obs_lf', 'value':state}, namespace='/malina'))

                self._right_obstacle_sensor.register_both_callbacks(
                    lambda pin, state: self._sockio.emit('sensors', {'sensor':'obs_rg', 'value':state}, namespace='/malina'))

    def remove_user(self):
        with self._lock:
            self._connected_users -= 1
            if self._connected_users < 0:
                self._connected_users = 0
            if self._connected_users == 0:
                self._distance_sensor.stop_distance_measure()
                self._left_obstacle_sensor.remove_callbacks()
                self._right_obstacle_sensor.remove_callbacks()

    @property
    def connected_users(self):
        return self._connected_users
