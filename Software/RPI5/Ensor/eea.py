#!/usr/bin/env python3

import gpiod
from smbus2 import SMBus
import time

from os.path import exists
from subprocess import Popen

import configparser

path_to_file = '/media/ensor/Ensor384/'
cfg_file = 'ensor.conf'

ti_reg={"PAGE_CFG": 0x00, 
		"SW_RESET": 0x01, 
		"SLEEP_CFG": 0x02, 
		"MISC_CFG": 0x03, 
		"MISC": 0x04, 
		"SHDN_CFG": 0x05, 
		"ASI_CFG0": 0x07, 
		"ASI_CFG1": 0x08, 
		"ASI_CFG2": 0x09, 
		"ASI_CH1": 0x0B, 
		"ASI_CH2": 0x0C, 
		"ASI_CH3": 0x0D, 
		"ASI_CH4": 0x0E, 
		"ASI_CH5": 0x0F, 
		"ASI_CH6": 0x10, 
		"ASI_CH7": 0x11, 
		"ASI_CH8": 0x12, 
		"MST_CFG0": 0x13, 
		"MST_CFG1": 0x14, 
		"ASI_STS": 0x15, 
		"CLK_SRC": 0x16, 
		"CLKGEN_CFG0": 0x17, 
		"CLKGEN_CFG1": 0x18, 
		"CLKGEN_CFG2": 0x19, 
		"CLKGEN_CFG3": 0x1A, 
		"CLKGEN_CFG4": 0x1B, 
		"CLKGEN_CFG5": 0x1C, 
		"CLKGEN_CFG6": 0x1D, 
		"CLKGEN_CFG7": 0x1E, 
		"PDMCLK_CFG": 0x1F, 
		"PDMIN_CFG": 0x20, 
		"GPIO_CFG0": 0x21, 
		"GPO_CFG0": 0x22, 
		"GPO_CFG1": 0x23, 
		"GPO_CFG2": 0x24, 
		"GPO_CFG3": 0x25, 
		"GPO_VAL": 0x29, 
		"GPIO_MON": 0x2A, 
		"GPI_CFG0": 0x2B, 
		"GPI_CFG1": 0x2C, 
		"GPI_MON": 0x2F, 
		"INT_CFG": 0x32, 
		"INT_MASK0": 0x33, 
		"INT_LTCH0": 0x36, 
		"INT_LIVE0": 0x38, 
		"BIAS_CFG": 0x3B, 
		"CH1_CFG0": 0x3C, 
		"CH1_CFG1": 0x3D, 
		"CH1_CFG2": 0x3E, 
		"CH1_CFG3": 0x3F, 
		"CH1_CFG4": 0x40, 
		"CH2_CFG0": 0x41, 
		"CH2_CFG1": 0x42, 
		"CH2_CFG2": 0x43, 
		"CH2_CFG3": 0x44, 
		"CH2_CFG4": 0x45, 
		"CH3_CFG0": 0x46, 
		"CH3_CFG1": 0x47, 
		"CH3_CFG2": 0x48, 
		"CH3_CFG3": 0x49, 
		"CH3_CFG4": 0x4A, 
		"CH4_CFG0": 0x4B, 
		"CH4_CFG1": 0x4C, 
		"CH4_CFG2": 0x4D, 
		"CH4_CFG3": 0x4E, 
		"CH4_CFG4": 0x4F, 
		"CH5_CFG0": 0x50, 
		"CH5_CFG1": 0x51, 
		"CH5_CFG2": 0x52, 
		"CH5_CFG3": 0x53, 
		"CH5_CFG4": 0x54, 
		"CH6_CFG0": 0x55, 
		"CH6_CFG1": 0x56, 
		"CH6_CFG2": 0x57, 
		"CH6_CFG3": 0x58, 
		"CH6_CFG4": 0x59, 
		"CH7_CFG0": 0x5A, 
		"CH7_CFG1": 0x5B, 
		"CH7_CFG2": 0x5C, 
		"CH7_CFG3": 0x5D, 
		"CH7_CFG4": 0x5E, 
		"CH8_CFG0": 0x5F, 
		"CH8_CFG1": 0x60, 
		"CH8_CFG2": 0x61, 
		"CH8_CFG3": 0x62, 
		"CH8_CFG4": 0x63, 
		"DSP_CFG0": 0x6B, 
		"DSP_CFG1": 0x6C, 
		"DRE_CFG0": 0x6D, 
		"DRE_CFG1": 0x6F, 
		"AGC_CFG0": 0x70, 
		"IN_CH_EN": 0x73, 
		"ASI_OUT_CH_EN": 0x74, 
		"PWR_CFG": 0x75, 
		"DEV_STS0": 0x76, 
		"DEV_STS1": 0x77, 
		"GP_ANA_STS": 0x78, 
		"GP_ANA0": 0x79, 
		"GP_ANA1": 0x7A, 
		"GP_DIG0": 0x7B, 
		"GP_DIG1": 0x7C, 
		"DEV_ID": 0x7D, 
		"I2C_CKSUM": 0x7E}

ti_384={"PAGE_CFG": 0x00,
		"SLEEP_CFG": 0x81,
		"ASI_CFG0": 0x70,
		"ASI_CH1": 0x00,
		"ASI_CH2": 0x01,
		"ASI_CH3": 0x02,
		"ASI_CH4": 0x20,
		"MST_CFG0": 0x87,
		"MST_CFG1": 0x74,	# 48:0x44, 96:0x54, 192:0x64, 384:0x74
		"CLKGEN_CFG0": 0x90,
		"MISC": 0x40,
		"GPIO_CFG0": 0xA2,
		"GPO_CFG0": 0x00,
		"GPI_CFG0": 0x00,
		"CH1_CFG0": 0x00,
		"CH1_CFG1": 0xA8,	# dB
		"CH1_CFG2": 0xC9,
		"CH2_CFG0": 0x00,
		"CH2_CFG1": 0x00,
		"CH2_CFG2": 0xC9,
		"CH3_CFG0": 0x00,
		"CH3_CFG1": 0x00,
		"CH3_CFG2": 0xc9,
		"CH4_CFG0": 0x00,
		"CH4_CFG1": 0xA8,	# dB
		"CH4_CFG2": 0xc9,
		"IN_CH_EN": 0x90,
		"ASI_OUT_CH_EN": 0x90,
		"PAGE_CFG": 0x00,
		"CLKGEN_CFG7": 0x82,
		"PDMCLK_CFG": 0xC0,
		"PWR_CFG": 0xE0}



def reset_ti():
        PIN_NO = 4
        chip=gpiod.Chip('gpiochip4')
        standby_pin=chip.get_line(PIN_NO)
        standby_pin.request(consumer="RESET",type=gpiod.LINE_REQ_DIR_OUT)

        standby_pin.set_value(1)
        time.sleep(1)

        standby_pin.set_value(0)
        time.sleep(1)

        standby_pin.set_value(1)
        time.sleep(10)


def config_ti():
        i2c = SMBus(1)
        adc_i2c_address = 0x4c
        for key, value in ti_384.items():
                i2c.write_byte_data(adc_i2c_address, ti_reg[key], value, force=True)



def check_cfg():
	file_exists = exists(path_to_file+cfg_file)
	if(not file_exists):
		config = configparser.ConfigParser()
		config['DEFAULT'] = {'Record' : 'no', 'Date': '01/09/2024', 'File_name': 'test_192Ks_32bits'}
		config['sound.format'] = {'Sampling': '192000', 'Bits': '32'}
		config['record.time'] = {'Total_time': '10', 'File_time': '10', 'Delay': '0', 'Index': '0'}
		with open(path_to_file+cfg_file, 'w') as configfile:
			config.write(configfile)


def check_record(config):
	rt = config['DEFAULT']
	if (rt['Record'] == 'no'):

		cmd = 'sudo systemctl stop rc-local.service'
		processes = []
		processes.append(Popen(cmd, shell=True))
		for p in processes: p.wait()
		exit()

		
	
def delay(config):
	rt = config['record.time']
	time.sleep(int(rt['Delay']))


def index_cfg(config):
	rt = config['record.time']
	rt['Index'] = str(int(rt['Index'])+1)
	with open(path_to_file+cfg_file, 'w') as configfile:
		config.write(configfile)

def print_cfg(config):
	print (config['DEFAULT']['Date'])
	print (config['DEFAULT']['File_name'])

	sf = config['sound.format']
	print(sf['Sampling'])
	print(sf['Bits'])

	rt = config['record.time']
	print(rt['Total_time'])
	print(rt['File_time'])
	print(rt['Delay'])
	print(rt['Index'])

def rec_cmd(config):
	sf = config['sound.format']
	rt = config['record.time']

	tm = time.strptime("{:s}".format(config['DEFAULT']['Date']), "%d/%m/%Y")
	time.clock_settime(0,time.mktime(tm))


	cmd = 'arecord -D hw:0,0 -d {:s} --max-file-time {:s} -c 2 -r {:s} -f S32_LE -t wav --use-strftime {:s}/%Y/%m/%d/{:s}_{:s}-%v.wav' \
		.format(rt['Total_time'],rt['File_time'],sf['Sampling'],path_to_file,config['DEFAULT']['File_name'],rt['Index'])
	#print(cmd)
	return cmd

def set_br(config):
	sf = config['sound.format']
	br = int(sf['Sampling'])

	# 48:0x44, 96:0x54, 192:0x64, 384:0x74
	if (br == 48000):
		ti_384['MST_CFG1'] = 0x44
	elif (br == 96000):
		ti_384['MST_CFG1'] = 0x54
	elif (br == 192000):
		ti_384['MST_CFG1'] = 0x64

def do_record(cmd):
	processes = []
	processes.append(Popen(cmd, shell=True))
	for p in processes: p.wait()

if __name__ == '__main__':
	#print(time.localtime(time.clock_gettime(0)))

	check_cfg()

	config = configparser.ConfigParser()
	config.read(path_to_file+cfg_file)

	check_record(config)
	
	delay(config)

	set_br(config)

	reset_ti()

	config_ti()

	index_cfg(config)

	rec_cmd(config)

	do_record(rec_cmd(config))

	#print(time.localtime(time.clock_gettime(0)))

