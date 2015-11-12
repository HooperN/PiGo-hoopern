#GOPIGO AUTONOMOUS, INSTANTIATED CLASS
#

from gopigo import *
import time

STOP_DIST = 40

class Pigo:

    ################################
    ### BASIC STATUS AND METHODS ###
    ################################

<<<<<<< HEAD
    status = {"ismoving" : False, "servopos" : 90, "leftspeed" : 150,
              "rightspeed" : 150, 'dist' : 100}
=======
    status = {"ismoving" : False, "servopos" : 70, "leftspeed" : 150,
              "rightspeed" : 150}
>>>>>>> a0a1a6950becba6e97c880ed463a33bad9b768e4

    def __init__(self):
        print "I've gained sentience; hello world"
        self.checkDist()

    def stop(self):
        self.status["ismoving"] = False
<<<<<<< HEAD
        i = 0
        i += 1
        while i < 0:
            stop()
            return stop()
        while stop()!= 1:
            print "The gears are busted! Hold onto something!"
            for z in range()
            stop()
            return stop()
=======
        while stop() == -1:
            time.sleep(1)
            print "My velocity is > 0 and refuses to decrease"
>>>>>>> a0a1a6950becba6e97c880ed463a33bad9b768e4

    def fwd(self):
        self.status["ismoving"] = True
        while fwd() == -1:
            time.sleep(1)
            print "I've fallen, and I can't get up!"

    #Checks to see if conditions are safe to continue operating
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "Road block ahead, get down!"
            return False
        elif: volt() > 14 or volt() < 6:
            print "Voltage exceeds capacity; current voltage:" + str(volt())
            return False
        else:
            return True

    def checkDist(self):
         self.status['dist'] = us_dist(15)
         print "Object sighted " + str(self.status['dist']) + " millimeters away!"
        if not self.keepGoing():
            print "STOPPING FOR CHECK"
            self.stop()

    def dance(self):
        print "Dance fever!"
         if self.keepGoing():
             self.circleLeft()
             self.CircleRight()
             self.fwdBwd()
             self.fullHeadturn()
             self.strobe()

    ########################
    ### ADVANCED METHODS ###
    ########################


def circleLeft(self):
    if self.keepGoing:
        thyme = time.clock()
        if time.clock() < 40 + thyme:
            set_left_speed(100)
            fwd()
        else time.clock() = 40 + thyme:
            self.stop()
            set_left_speed(200)
    else:
        print "Check keepGoing"


def circleRight(self):
    if self.keepGoing:
        thyme = time.clock()
        if time.clock() < 40 + thyme:
            set_right_speed(100)
            fwd()
        else time.clock() = 40 + thyme:
            self.stop()
            set_right_speed(200)
    else:
        print "Check keepGoing"


def fwdBwd(self):
    if self.keepGoing:
        thyme = time.clock()
        if time.clock() < thyme + 10:
            fwd()
        elif time.clock() < thyme + 20:
            bwd()
        else time.clock() = thyme + 20:
            self.stop()
    else:
        print "Check keepGoing"


def fullHeadturn(self):
    servo(0)
    servo(180)
    servo(0)


def strobe(self):
    i = 0
    while i < 3:
        led_on(1)
        led_on(0)
        led_off(1)
        led_off(0)
        i += 1



def


    ############################
    ### FULL APP STARTS HERE ###
    ############################

beatrix = Pigo()
while beatrix.keepGoing():
    beatrix.fwd()
    time.sleep(2)

beatrix.stop()
