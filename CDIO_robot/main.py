#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Stop, Direction
from pybricks.tools import wait

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.C)
indsamler = Motor(Port.D)

# Write your program here.
ev3.speaker.beep()

# Run indsamler concurrently while testing left and right motors
indsamler.run(speed=800)

# Run left and right motors together
left_motor.run(-200)
right_motor.run(-200)

# Wait for 3 seconds
wait(20000)

# Stop left and right motors
left_motor.stop()
right_motor.stop()

# Stop indsamler
indsamler.stop()
