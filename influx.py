#!/usr/bin/python
import sys
import minimalmodbus

# Set MinimalModbus parameters: 9600 baud and Even parity for my RS485
minimalmodbus.BAUDRATE=9600
minimalmodbus.PARITY='E'

# Declare an object on port /dev/ttyUSB0, slave address 1
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

energy_all = None
while energy_all is None:
	try:
		energy_all = (instrument.read_float(256, 3, 2))
	except: 
		pass

energy_l1 = None
while energy_l1 is None:
        try:
                energy_l1 = (instrument.read_float(258, 3, 2))
        except:
                pass

energy_l2 = None
while energy_l2 is None:
        try:
                energy_l2 = (instrument.read_float(260, 3, 2))
        except:
                pass

energy_l3 = None
while energy_l3 is None:
        try:
                energy_l3 = (instrument.read_float(262, 3, 2))
        except:
                pass


power_all = None
while power_all is None:
	try:
		power_all = (instrument.read_float(28, 3, 2))
	except:
		pass

power_l1 = None
while power_l1 is None:
	try:
		power_l1 = (instrument.read_float(30, 3, 2))
	except:
		pass

power_l2 = None
while power_l2 is None:
	try:
		power_l2 = (instrument.read_float(32, 3, 2))
	except:
		pass

power_l3 = None
while power_l3 is None:
	try:
		power_l3 = (instrument.read_float(34, 3, 2))
	except:
		pass


voltage_l1 = None
while voltage_l1 is None:
	try:
		voltage_l1 = (instrument.read_float(14, 3, 2))
	except:
		pass

voltage_l2 = None
while voltage_l2 is None:
	try:
		voltage_l2 = (instrument.read_float(16, 3, 2))
	except:
		pass

voltage_l3 = None
while voltage_l3 is None:
	try:
		voltage_l3 = (instrument.read_float(18, 3, 2))
	except:
		pass

print(energy_all, energy_l1, energy_l2, energy_l3)
print(power_all, power_l1, power_l2, power_l3)
print(voltage_l1, voltage_l2, voltage_l3)
