#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Mike Qin"
__email__ = "laigui@gmail.com"

import unittest

from usbmodule import r4i4d
import dummy_serial


###########################################
# Communication using a dummy serial port #
###########################################

class TestDummyCommunication(unittest.TestCase):

    def setUp(self):   
    
        # Prepare a dummy serial port to have proper responses
        dummy_serial.VERBOSE = False
        dummy_serial.RESPONSES = RESPONSES

        # Monkey-patch a dummy serial port for testing purpose
        r4i4d.minimalmodbus.serial.Serial = dummy_serial.Serial

        # Initialize a (dummy) instrument
        self.instrument = r4i4d.RelayModule('DUMMYPORTNAME', 1)
        self.instrument.debug = False

    ## Get digital inputs ##

    def test_get_digital_inputs(self):
        self.assertAlmostEqual( self.instrument.get_digital_inputs(), 8 ) 

    ## Set relay outputs and get status ##

    def test_set_relay1_output(self):
        self.instrument.set_relay_output(1, True)
        self.assertTrue(self.instrument.get_relay_output(1)) 

    def test_set_relay2_output(self):
        self.instrument.set_relay_output(2, True)
        self.assertTrue(self.instrument.get_relay_output(2)) 

    def test_set_relay3_output(self):
        self.instrument.set_relay_output(3, True)
        self.assertTrue(self.instrument.get_relay_output(3)) 

    def test_set_relay4_output(self):
        self.instrument.set_relay_output(4, True)
        self.assertTrue(self.instrument.get_relay_output(4))     
    
    
RESPONSES = {}
"""A dictionary of respones from a dummy HHC R4I4D instrument. 
The key is the message (string) sent to the serial port, and the item is the response (string) 
from the dummy serial port.
"""
# Note that the string 'AAAAAAA' might be easier to read if grouped, 
# like 'AA' + 'AAAA' + 'A' for the initial part (address etc) + payload + CRC.


# get_digital_inputs(): Return value 8
RESPONSES['\x01\x02' + '\x00\x20\x00\x04' + '\x78\x03'] = '\x01\x02' + '\x01\x08' + '\xa0\x4e'

# set_relay_output(1, True)
RESPONSES['\x01\x05' + '\x00\x10\xff\x00' + '\x8d\xff'] = '\x01\x05' + '\x00\x10\xff\x00' + '\x8d\xff'   

# set_relay_output(1, False)
RESPONSES['\x01\x05' + '\x00\x10\x00\x00' + '\xcc\x0f'] = '\x01\x05' + '\x00\x10\x00\x00' + '\xcc\x0f'   

# set_relay_output(2, True)
RESPONSES['\x01\x05' + '\x00\x11\xff\x00' + '\xdc\x3f'] = '\x01\x05' + '\x00\x11\xff\x00' + '\xdc\x3f'   

# set_relay_output(2, False)
RESPONSES['\x01\x05' + '\x00\x11\x00\x00' + '\x9d\xcf'] = '\x01\x05' + '\x00\x11\x00\x00' + '\x9d\xcf'   

# set_relay_output(3, True)
RESPONSES['\x01\x05' + '\x00\x12\xff\x00' + '\x2c\x3f'] = '\x01\x05' + '\x00\x12\xff\x00' + '\x2c\x3f'   

# set_relay_output(3, False)
RESPONSES['\x01\x05' + '\x00\x12\x00\x00' + '\x6d\xcf'] = '\x01\x05' + '\x00\x12\x00\x00' + '\x6d\xcf'   

# set_relay_output(4, True)
RESPONSES['\x01\x05' + '\x00\x13\xff\x00' + '\x7d\xff'] = '\x01\x05' + '\x00\x13\xff\x00' + '\x7d\xff'   

# set_relay_output(4, False)
RESPONSES['\x01\x05' + '\x00\x13\x00\x00' + '\x3c\x0f'] = '\x01\x05' + '\x00\x13\x00\x00' + '\x3c\x0f'   

# get_relay_output(1): return true
RESPONSES['\x01\x01' + '\x00\x10\x00\x01' + '\xfc\x0f'] = '\x01\x01' + '\x01\x01' + '\x90\x48'   

# get_relay_output(2): return true
RESPONSES['\x01\x01' + '\x00\x11\x00\x01' + '\xad\xcf'] = '\x01\x01' + '\x01\x01' + '\x90\x48' 

# get_relay_output(3): return true
RESPONSES['\x01\x01' + '\x00\x12\x00\x01' + '\x5d\xcf'] = '\x01\x01' + '\x01\x01' + '\x90\x48' 

# get_relay_output(4): return true
RESPONSES['\x01\x01' + '\x00\x13\x00\x01' + '\x0c\x0f'] = '\x01\x01' + '\x01\x01' + '\x90\x48' 


if __name__ == '__main__':
    unittest.main() 