class SteeringDispatcher(object):
    def __init__(self, robot):
        self._robot = robot

        self._steering_functions = {
            "dopredu" : robot.steering.forward, 
            "dozadu": robot.steering.reverse,
            "rotujvlevo" : robot.steering.spin_left,
            "rotujvpravo" : robot.steering.spin_right,
            "zatocvpredvpravo" : robot.steering.turn_right,
            "zatocvpredvlevo": robot.steering.turn_left,
            "zatocvzadvlevo" : robot.steering.turn_rev_left, 
            "zatocvzadvpravo" : robot.steering.turn_rev_right, 
            "stop": robot.steering.stop}

    def dispatch(self, action):
        if action in self._steering_functions:
            self._steering_functions[action]()
        else:
            print("Action not defined: " + action)

    def change_speed(self, action):
        if action == 'zrychli':
            speed = self._robot.steering.increase_speed()
        if action == 'zpomal':
            speed = self._robot.steering.decrease_speed()
        return speed
