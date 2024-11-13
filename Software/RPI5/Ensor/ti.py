#!/usr/bin/env python3

import sys
import csv

import gpiod
from smbus2 import SMBus
import time

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

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ('Usage: %s <ti.csv> [0|1]' % sys.argv[0])
        sys.exit(1)

    rw = 0
    if (len(sys.argv) == 3) & (sys.argv[2] != '0'):
        rw = 1

    i2c = SMBus(1)
    adc_i2c_address = 0x4c

    #adc_wp()

    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['Register Address'], row['Register Name'], row['Register Value'])
            ad = int(row['Register Address'],16)
            val = int(row['Register Value'],16)
            if rw == 0:
                data = i2c.read_byte_data(adc_i2c_address, ad, force=True)
                print(row['Register Address'], row['Register Name'], "{:02X}".format(data))
            else:
                i2c.write_byte_data(adc_i2c_address, ad, val, force=True)
                print(row['Register Address'], row['Register Name'], row['Register Value'])

