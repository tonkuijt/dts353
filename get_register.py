#!/usr/bin/env python

# Import needed libraries
import sys
import minimalmodbus

# Check if register is given
#if sys.argv[1] <=0 :
#	sys.exit("Please pass register to be queried to the script as decimal")


# Set minimalmodbus to the serial parameters for your device
minimalmodbus.BAUDRATE=9600
minimalmodbus.PARITY='E'

# Declare an instrument (device) to be queried
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)

## Read register value given on cli
register = int(sys.argv[1])
value = instrument.read_float(register, 3, 2) # Registernumber, number of decimals

# Return found register value
print(value) 
