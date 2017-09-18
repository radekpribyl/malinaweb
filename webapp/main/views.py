from flask import render_template, url_for, redirect, current_app
from . import main

@main.route('/')
def home():
    robot = current_app.config["ROBOT"]
    config = {"zapnuty" : robot.is_robot_initiated,
              "rychlost" : robot.steering.current_speed}

    return render_template('Index.html', config=config)

@main.route('/prepni')
def prepni():
    robot = current_app.config["ROBOT"]
    if robot.is_robot_initiated:
        robot.cleanup()
    else:
        robot.init()
    return redirect(url_for('main.home'))
