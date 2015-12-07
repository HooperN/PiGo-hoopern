#GOPIGO AUTONOMOUS, INSTANTIATED CLASS
#http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

from gopigo import *
import time
import sys
from collections import Counter
import math

STOP_DIST = 20

class Pigo:

    ################################
    ### BASIC STATUS AND METHODS ###
    ################################

    status = {"ismoving" : False, "servopos" : 90, "leftspeed" : 150,
              "rightspeed" : 150, 'dist' : 100}

    free = [0] * 180

    superfree = [0] * 180

    def __init__(self):
        print "I've gained sentience; hello world"
        self.checkDist()

    def stop(self):
        self.status["ismoving"] = False
        print "Stopping."
        for x in range(5):
            stop()


    def moveIt(self):
        if self.checkDist():
            fwd()
            time.sleep(2)
            self.checkDist()
        while fwd() == -1:
            time.sleep(1)
            print "I've fallen, and I can't get up!"

    def checkDist(self):
        if us_dist(15) < STOP_DIST:
            print "Road block ahead, get down!"
            return False
        elif volt() > 14 or volt() < 6:
            print "Voltage exceeds capacity; current voltage:" + str(volt())
            return False
        else:
            return True

    def dance(self):
        print "Dance fever!"
        self.circleLeft()
        self.servoSweep()
        self.stop()
        self.circleRight()
        self.stop()
        self.fwdBwd()
        time.sleep(.1)
        self.fullHeadturn()
        time.sleep(.1)
        self.strobe()
        time.sleep(.1)
        self.servoSweep()

    ########################
    ### ADVANCED METHODS ###
    ########################

    def autoPilot(self):
        self.moveIt()
        while True:
            self.checkDist()
            time.sleep(5)
        self.stop()

    def servoSweep(self):
        print "Sweep!"
        for ang in range(20, 160, 10):
            servo(ang)
            time.sleep(.1)
            self.checkDist()

    def circleLeft(self):
        if self.checkDist():
            thyme = time.clock()
            if time.clock() < 10 + thyme:
                print "Left Circle!"
                set_left_speed(100)
                fwd()
            elif time.clock() == 10 + thyme:
                time.sleep(1)
                self.stop()
                set_left_speed(200)
        else:
            print "Check keepGoing"
            stop()


    def circleRight(self):
        print "Start CR"
        for x in range(3):
            right_rot()
        time.sleep(1)
        self.stop()
        print "Done CR"

        '''
        if self.keepGoing:
            thyme = time.clock()
            if time.clock() < 10 + thyme:
                print "Right Circle!"
                set_right_speed(100)
                fwd()
            elif time.clock() == 10 + thyme:
                time.sleep(1)
                self.stop()
                set_right_speed(200)
        else:
            print "Check keepGoing"
            stop()
        '''

    def fwdBwd(self):
        if self.checkDist():
            print "Forwards, Then Backwards!"
            thyme = time.clock()
            if time.clock() < thyme + 10:
                fwd()
            elif time.clock() < thyme + 20:
                bwd()
            elif time.clock() == thyme + 20:
                self.stop()
        else:
            print "Check keepGoing"


    def fullHeadturn(self):
        print "Head Turn!"
        servo(0)
        time.sleep(1)
        servo(180)
        time.sleep(1)
        servo(0)
        time.sleep(1)




    def strobe(self):
        i = 0
        print "Strobe light!"
        while i < 3:
            led_on(1)
            time.sleep(1)
            led_on(0)
            time.sleep(1)
            led_off(1)
            time.sleep(1)
            led_off(0)
            i += 1

    def trot(self):   #method to adjust the forward speed
        set_left_speed(180)
        set_right_speed(180)
        fwd()

    def run(self):
        print "Press ENTER to start"
        raw_input()				#Wait for input to start
        self.trot()					#Start moving
        while True:
            dist=us_dist(15)			#Find the distance of the object in front
            print "Dist:",dist,'cm'
            if dist < STOP_DIST:	#If the object is closer than the "STOP_DIST" distance, stop the GoPiGo
                print "Something in my way. Going to look for a new path"
                stop()					#Stop the GoPiGo
                self.findPathRight()
            else:
                print "Let's hit the road again."
                self.trot()
                time.sleep(.5)

    def servoCheck(self):
        for ang in range(50, 110, 3):
            self.free[ang] = us_dist(15)

    def findPathLeft(self):
         if self.servoCheck():
            if self.findAngle() is False:
                if self.findPathRight() is False:
                    self.turnTo('left')
                    return True
                else:
                    return False
            else:
                print "Check the find Angle"
         else:
            print "Check the Servo Check"

    def findPathRight(self):
        if self.servoCheck():
            if self.findAngle() is False:
                if self.findPathLeft() is False:
                    self.turnTo('right')
                    return True
                else:
                    return False

    def pathing(self):
        self.servoCheck()
        for self.free[ang] < STOP_DIST:
            self.superfree[].append

    def turnTo(self, direction):
        if direction is 'left':
            left()
            time.sleep(1)
            stop()
        elif direction is 'right':
            right()
            time.sleep(1)
            stop()
        else:
            return False


    def findAngle(self):
        self.servoCheck()
        for dist in self.free:
            counter = 0
            if dist > STOP_DIST:
                counter += 1
            else:
                counter = 0
            if counter = 20:
                return True
        return False



    def reverse(self):


    def avoidance(self):
        while True:
            if self.checkDist():
                self.autoPilot()
            else:
                self.servoCheck()
                if self.pathing:
                    self.turnTo(self.findAngle)
                else:
                    self.reverse()





    ############################
    ### FULL APP STARTS HERE ###
    ############################

beatrix = Pigo()

beatrix.avoidance()

