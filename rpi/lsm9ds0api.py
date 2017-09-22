#!/usr/bin/python

# based on berryIMU-simple.py from https://github.com/mwilliams03/BerryIMU

import smbus
import math
from LSM9DS0 import *



======================================================


def writeACC(register,value):
        bus.write_byte_data(ACC_ADDRESS , register, value)
        return -1


def readACCx():
        acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_X_L_A)
        acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_X_H_A)
	acc_combined = (acc_l | acc_h <<8)

	return acc_combined  if acc_combined < 32768 else acc_combined - 65536


def readACCy():
        acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Y_L_A)
        acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Y_H_A)
	acc_combined = (acc_l | acc_h <<8)

	return acc_combined  if acc_combined < 32768 else acc_combined - 65536


def readACCz():
        acc_l = bus.read_byte_data(ACC_ADDRESS, OUT_Z_L_A)
        acc_h = bus.read_byte_data(ACC_ADDRESS, OUT_Z_H_A)
	acc_combined = (acc_l | acc_h <<8)

	return acc_combined  if acc_combined < 32768 else acc_combined - 65536


======================================================



bus = 0

def initSensor():
	global bus
	bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards

	#initialise the accelerometer
	writeACC(CTRL_REG1_XM, 0b01100111) #z,y,x axis enabled, continuos update,  100Hz data rate
	writeACC(CTRL_REG2_XM, 0b00100000) #+/- 16G full scale


def readAccelX():
	return readAccx()

def readAccelY():
	return readAccy()

def readAccelZ():
	return readAccz()

def readAccel():
	return readAccelX(), readAccelY(), readAccelZ()

def readScaledAccel():
	ax, ay, az = readAccel()
	scale = math.sqrt(ax * ax + ay * ay + az * az)
	return ax/scale, ay/scale, az/scale


