#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_wheel = Motor(Port.C)
right_wheel = Motor(Port.B)
robotman = DriveBase(left_wheel,right_wheel,wheel_diameter=23,axle_track=44)
medium_motor = Motor(Port.A)

# Write your program here.

# A robot beszédet tart.
ev3.speaker.say("Hello guys, welcome to my minecraft lets play.")

# Bal kerék forogni kezd.
left_wheel.run_target(1000,2000)

# Jobb kerék is forogni kezd.
right_wheel.run_target(1000,2000)

# Mindkét kerék forogni kezd egyszerre.
robotman.turn(720)

# A robot megint beszélni kezd.
ev3.speaker.say("The command was succesful, Good Job!")

# A robot visszafelé kezd forogni.
robotman.turn(-720)

# A harmadik motor is forogni kezd.
medium_motor.run_target(1000,2000)

# A robot megint beszél.
ev3.speaker.say("I dont know what to do, so im gonna make another line of code.")

# Mindkét kerék ugyanabba az irányba kezd forogni
robotman.straight(200)

# A robot utoljára beszél
ev3.speaker.say("The command was succesful agian")


# Még egy sor valamiből
robotman.stop()
left_wheel.brake()
right_wheel.brake()

# i dont know bro

