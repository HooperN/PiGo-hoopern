from gopigo import *
import time

class Pigo:

    ################################
    ### BASIC STATUS AND METHODS ###
    ################################

    status = {"ismoving" : False, "servopos" : 90, "leftspeed" : 150,
              "rightspeed" : 150}

    def __init__(self):
        print "I've gained sentience; hello world"

    def stop(self):
        self.isMoving = False
        while stop()!= 1:
            time.sleep(1)
            print "My velocity is > 0 and refuses to decrease"

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(1)
            print "I've fallen, and I can't get up!"

    ########################
    ### ADVANCED METHODS ###
    ########################


    ############################
    ### FULL APP STARTS HERE ###
    ############################

beatrix = Pigo()
beatrix.fwd()
time.sleep(2)
beatrix.stop()
