from gopigo import *
import time

STOP_DIST = 40

class Pigo:

    ################################
    ### BASIC STATUS AND METHODS ###
    ################################

    status = {"ismoving" : False, "servopos" : 90, "leftspeed" : 150,
              "rightspeed" : 150, 'dist' : 100}

    def __init__(self):
        print "I've gained sentience; hello world"
        self.checkDist()

    def stop(self):
        self.status["ismoving"] = False
        print "My velocity is > 0 and refuses to decrease"
        for z in range()

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(1)
            print "I've fallen, and I can't get up!"

    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            return False
        else:
            return True

    def checkDist(self):
         self.status['dist'] = us_dist(15)
         print "Object sighted " + str(self.status['dist']) + " millimeters away!"
        if not self.keepgoing():
            print "STOPPING FOR CHECK"
            self.stop()

    def dance(self):
        print "Dance fever!"
         if self.keepgoing():
             self.circleLeft()
             self.CircleRight()
             self.fwdBck()
             self.fullHeadturn()
             self.strobe()

    ########################
    ### ADVANCED METHODS ###
    ########################

    ############################
    ### FULL APP STARTS HERE ###
    ############################

beatrix = Pigo()
while beatrix.keepGoing():
    beatrix.fwd()
    time.sleep(2)

beatrix.stop()
