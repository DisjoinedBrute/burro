'''

mixed.py

Methods to create, use, save and load pilots. Pilots
contain the highlevel logic used to determine the angle
and throttle of a vehicle. Pilots can include one or more
models to help direct the vehicles motion.

'''
from __future__ import division

import os
import math
import random
from operator import itemgetter
from datetime import datetime

import methods
from rc import RC
from f710 import F710
from pilots import BasePilot, KerasCategorical


class MixedRC(BasePilot):
    def __init__(self, keras_pilot, **kwargs):
        self.RCPilot = RC()
        self.KerasCategoricalPilot = keras_pilot
        super(Mixed, self).__init__(**kwargs)

    def decide(self, img_arr):
        rc_yaw, rc_throttle = self.RCPilot.decide(img_arr)
        keras_angle, keras_throttle = self.KerasCategoricalPilot.decide(
            img_arr)
        return keras_angle, rc_throttle

    def pname(self):
        return "Mixed (Keras+RC)"


class MixedF710(BasePilot):
    def __init__(self, keras_pilot, **kwargs):
        self.F710Pilot = F710()
        self.KerasCategoricalPilot = keras_pilot
        super(Mixed, self).__init__(**kwargs)

    def decide(self, img_arr):
        f_yaw, f_throttle = self.F710.decide(img_arr)
        keras_angle, keras_throttle = self.KerasCategoricalPilot.decide(
            img_arr)
        return keras_angle, f_throttle

    def pname(self):
        return "Mixed (Keras+F710 Gamepad)"
