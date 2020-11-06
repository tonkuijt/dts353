#!/usr/bin/env python

# Import needed libraries
import sys
import minimalmodbus
import serial

# Declare an instrument (device) to be queried
instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)

# Settings for the given instrument
instrument.serial.baudrate = 9600		# Baud rate
instrument.serial.bytesize = 8			# Data bits
instrument.serial.parity = serial.PARITY_EVEN	# Parity
instrument.serial.stopbits = 1			# Stop bits
instrument.mode = minimalmodbus.MODE_RTU	# Device mode

## Read register value given on cli
register = int(sys.argv[1])
value = instrument.read_float(register, 3, 2) # Registernumber, number of decimals

# Return found register value
print(value)
