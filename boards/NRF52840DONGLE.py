#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------
# also see https://gist.github.com/fanoush/c081c1d7c8eb2a4562785bbb684f661e
#
# # BUILD it:
# > make clean && BOARD=NRF52840DONGLE RELEASE=1 make


import pinutils;

info = {
 'name' : "NRF52840 Dongle",
 'link' :  [ "https://www.nordicsemi.com/Software-and-tools/Development-Kits/nRF52840-Dongle" ],
# 'default_console' : "EV_BLUETOOTH",
 'default_console' : "EV_USBSERIAL",
 'variables' : 14000, # How many variables are allocated for Espruino to use. RAM will be overflowed if this number is too high and code won't compile.
# 'bootloader' : 1,
 'binary_name' : 'espruino_%v_52840dongle.hex',
 'build' : {
   'optimizeflags' : '-Os',
   'libraries' : [
     'BLUETOOTH',
#     'NET',
     'GRAPHICS',
#     'NFC',
#     'NEOPIXEL'
   ],
   'makefile' : [
     'DEFINES += -DCONFIG_GPIO_AS_PINRESET', # Allow the reset pin to work
     'DEFINES += -DBOARD_PCA10059 -DNRF_SDH_BLE_GATT_MAX_MTU_SIZE=131', #59 77 131 104
     'LDFLAGS += -Xlinker --defsym=LD_APP_RAM_BASE=0x2ec0',#2bf0 0x3058#37f8 0x3720
     'DEFINES += -DBLUETOOTH_NAME_PREFIX=\'"Dongle"\'',
     'DFU_PRIVATE_KEY=targets/nrf5x_dfu/dfu_private_key.pem',
     'DFU_SETTINGS=--application-version 0xff --hw-version 52 --sd-req 0xa9,0xae,0xb6', #S140 6.0.0
     'BOOTLOADER_SETTINGS_FAMILY=NRF52840',
     'DEFINES += -DNRF_USB=1 -DUSB',
#     'DEFINES += -DUART1_ENABLED=1 -DRNG_CONFIG_POOL_SIZE=64',
#     'DEFINES+=-DNEOPIXEL_SCK_PIN=9 -DNEOPIXEL_LRCK_PIN=10',
     'DEFINES += -DNO_DUMP_HARDWARE_INITIALISATION',
     'DEFINES += -DNRF_BL_DFU_INSECURE=1',
     'NRF_SDK15=1'
   ]
 }
};


chip = {
  'part' : "NRF52840",
  'family' : "NRF52",
  'package' : "QFN48",
  'ram' : 256,
  'flash' : 1024,
  'speed' : 64,
  'usart' : 1, #2
  'spi' : 1, #3
  'i2c' : 2,
  'adc' : 1,
  'dac' : 0,
  'saved_code' : {
    'address' : ((0xe0 - 2 - 96) * 4096), # Bootloader at 0xE0000
    'page_size' : 4096,
    'pages' : 96,
    'flash_available' : 1024 - ((0x26 + 0x20 + 2 + 96)*4) # Softdevice uses 38 pages of flash (0x26000/0x100), bootloader 0x100-0xe0=0x20, FS 2, code 96. Each page is 4 kb.
  },
};

devices = {
  'BTN1' : { 'pin' : 'D38', 'pinstate' : 'IN_PULLDOWN' }, # Pin negated in software
#RGB LED
  'LED1' : { 'pin' : 'D6' }, # Pin negated in software
  'LED2' : { 'pin' : 'D8' }, # Pin negated in software
  'LED3' : { 'pin' : 'D41' }, # Pin negated in software
  'LED4' : { 'pin' : 'D12' }, # Pin negated in software
#  'RX_PIN_NUMBER' : { 'pin' : 'D8'},
#  'TX_PIN_NUMBER' : { 'pin' : 'D6'},
#  'CTS_PIN_NUMBER' : { 'pin' : 'D7'},
#  'RTS_PIN_NUMBER' : { 'pin' : 'D5'},

};

# left-right, or top-bottom order
board = {
};

def get_pins():
  pins = pinutils.generate_pins(0,47) # 48 General Purpose I/O Pins.
  pinutils.findpin(pins, "PD0", True)["functions"]["XL1"]=0;
  pinutils.findpin(pins, "PD1", True)["functions"]["XL2"]=0;
#  pinutils.findpin(pins, "PD5", True)["functions"]["RTS"]=0;
#  pinutils.findpin(pins, "PD6", True)["functions"]["TXD"]=0;
#  pinutils.findpin(pins, "PD7", True)["functions"]["CTS"]=0;
#  pinutils.findpin(pins, "PD8", True)["functions"]["RXD"]=0;
  pinutils.findpin(pins, "PD9", True)["functions"]["NFC1"]=0;
  pinutils.findpin(pins, "PD10", True)["functions"]["NFC2"]=0;
  pinutils.findpin(pins, "PD2", True)["functions"]["ADC1_IN0"]=0;
  pinutils.findpin(pins, "PD3", True)["functions"]["ADC1_IN1"]=0;
  pinutils.findpin(pins, "PD4", True)["functions"]["ADC1_IN2"]=0;
  pinutils.findpin(pins, "PD5", True)["functions"]["ADC1_IN3"]=0;
  pinutils.findpin(pins, "PD28", True)["functions"]["ADC1_IN4"]=0;
  pinutils.findpin(pins, "PD29", True)["functions"]["ADC1_IN5"]=0;
  pinutils.findpin(pins, "PD30", True)["functions"]["ADC1_IN6"]=0;
  pinutils.findpin(pins, "PD31", True)["functions"]["ADC1_IN7"]=0;
  # Make buttons and LEDs negated
  pinutils.findpin(pins, "PD6", True)["functions"]["NEGATED"]=0;
  pinutils.findpin(pins, "PD8", True)["functions"]["NEGATED"]=0;
  pinutils.findpin(pins, "PD12", True)["functions"]["NEGATED"]=0;
  pinutils.findpin(pins, "PD38", True)["functions"]["NEGATED"]=0;
  pinutils.findpin(pins, "PD41", True)["functions"]["NEGATED"]=0;

  # everything is non-5v tolerant
  for pin in pins:
    pin["functions"]["3.3"]=0;
  return pins
