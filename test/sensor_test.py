#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ShiningChan
# @Date:   2014-02-12 16:52:34
# @Last Modified by:   ShiningChan
# @Last Modified time: 2014-02-15 15:17:14
import sys
sys.path.append('..')
from sensors.dht11 import DHT11
from sensors.hc_sr04 import HC_SR04
from sensors.hc_sr501 import HC_SR501

if __name__ == '__main__':
    #dht11 = DHT11()   
    #dht11.getOutput()
    #hc_sr04 = HC_SR04()
    #hc_sr04.getOutput()
    hc_sr501 = HC_SR501()
    hc_sr501.getOutput()
