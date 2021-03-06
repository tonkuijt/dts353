#!/bin/bash

# InfluxDB server goes here
INFLUXSERVER=[InfluxDB Server URL]

# Script location goes here
SCRIPTLOCATION=${PWD}

if [ "$1" == "1" ]; then debug=1; fi

while [ -z $totalenergy ]; do
	totalenergy=`python $SCRIPTLOCATION/get_register.py 256 2> /dev/null`
	count=$(($count+1))
	if [ "$debug" == "1" ]; then echo $count; fi
done


while [ -z $l1_energy ]; do
        l1_energy=`python $SCRIPTLOCATION/get_register.py 258 2> /dev/null`
	count=$(($count+1))
	if [ "$debug" == "1" ]; then echo $count; fi
done

while [ -z $l2_energy ]; do
        l2_energy=`python $SCRIPTLOCATION/get_register.py 260 2> /dev/null`
	count=$(($count+1))
	if [ "$debug" == "1" ]; then echo $count; fi
done

while [ -z $l3_energy ]; do
        l3_energy=`python $SCRIPTLOCATION/get_register.py 256 2> /dev/null`
	count=$(($count+1))
	if [ "$debug" == "1" ]; then echo $count; fi
done

while [ -z $total_power ]; do
        total_power=`python $SCRIPTLOCATION/get_register.py 28 2> /dev/null`
	count=$(($count+1))
	if [ "$debug" == "1" ]; then echo $count; fi
done
while [ -z $l1_power ]; do
        l1_power=`python $SCRIPTLOCATION/get_register.py 30 2> /dev/null`
	count=$(($count+1))
	if [ "$debug" == "1" ]; then echo $count; fi
done
while [ -z $l2_power ]; do
        l2_power=`python $SCRIPTLOCATION/get_register.py 32 2> /dev/null`
	count=$(($count+1))
	if [ "$debug" == "1" ]; then echo $count; fi
done
while [ -z $l3_power ]; do
        l3_power=`python $SCRIPTLOCATION/get_register.py 34 2> /dev/null`
	count=$(($count+1))
	if [ "$debug" == "1" ]; then echo $count; fi
done

if [ "$debug" == "1" ]; then
	echo "Total energy $totalenergy kWh"
	echo "L1 energy $l1_energy kWh"
	echo "L2 energy $l2_energy kWh"
	echo "L3 energy $l3_energy kWh"
	echo "Total power $total_power kW"
	echo "L1 power $l1_power kW"
	echo "L2 power $l2_power kW"
	echo "L3 power $l3_power kW"
	echo "Number of retries: $count"
else
	curl --silent -i -XPOST '$INFLUXSERVER:8086/write?db=emobility' --data-binary "energy,phase=all value=$totalenergy
energy,phase=l1 value=$l1_energy
energy,phase=l2 value=$l2_energy
energy,phase=l3 value=$l3_energy
power,phase=all value=$total_power
power,phase=l1 value=$l1_power
power,phase=l2 value=$l2_power
power,phase=l3 value=$l3_power" --output /dev/null
fi

