#!/usr/bin/env python

# Author: Brendan Le Foll <brendan.le.foll@intel.com>
# Copyright (c) 2014 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import mraa

print (mraa.getVersion())

try:
    analogPin0 = mraa.Aio(0)
    analogPin1 = mraa.Aio(1)
    analogPin2 = mraa.Aio(2)
    temperatureC = ( analogPin0.read()*5.0/1024.0 -0.5 )*100
    temperatureF = temperatureC*9/5+32
    print( "Temperature is %.5f degrees F" % temperatureF )
    photosense = ( 512 - analogPin1.read() )
    print( "Light reading is %.5f brightness" % photosense )
    audiosense = ( analogPin2.read() )
    print( "Ambient noise reading is %.5f" % audiosense )

except:
    print ("Are you sure you have an ADC?")

