#GOPIGO AUTONOMOUS, INSTANTIATED CLASS
#http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-
# the-raspberry-pi-gopigo/

from gopigo import *
import time

STOP_DIST = 20

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
        i = 0
        for x in range(5):
            stop()
            time.sleep(.1)
        time.sleep(1)

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
        elif volt() > 14 or volt() < 6:
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
           # self.circleLeft()
            #time.sleep(.1)

            self.servoSweep()
            time.sleep(.1)

            self.circleRight()
            time.sleep(.1)
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
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()

    def servoSweep(self):
        for ang in range(20, 160, 10):
            print "Sweep!"
            servo(ang)
            time.sleep(.1)
            self.checkDist()

    def circleLeft(self):
        if self.keepGoing:
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
        if self.keepGoing:
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


    ############################
    ### FULL APP STARTS HERE ###
    ############################

beatrix = Pigo()

beatrix.dance()

beatrix.stop()
