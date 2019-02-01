# dts353
Python code to read the dts353 MODBUS kWh meters

get_register.py is the main Python script that reads the register as argument and returns the register content.
Current settings default to 4-byte float because most registers that are interesting are 4-byte floats.

influx.py is work-in-progress, and also needs python-influx. This script is far from finished.
