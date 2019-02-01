#!/usr/bin/env python
import sys
import minimalmodbus
minimalmodbus.BAUDRATE=9600
minimalmodbus.PARITY='E'

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)

## Read register value
register = int(sys.argv[1])
value = instrument.read_float(register, 3, 2) # Registernumber, number of decimals
print(value) 
