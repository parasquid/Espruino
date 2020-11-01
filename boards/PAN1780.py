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

import pinutils;

info = {
 'name' : "PAN1780 Evaluation Kit",
 'link' :  [ "https://na.industrial.panasonic.com/products/wireless-connectivity/evaluation-kits/lineup/pan1780-series-evaluation-kit" ],
 'espruino_page_link' : '',
  # This is the PCA10056
 'default_console' : "EV_SERIAL1",
 'default_console_tx' : "D6",
 'default_console_rx' : "D8",
 'default_console_baudrate' : "9600",
 'variables' : 12500, # How many variables are allocated for Espruino to use. RAM will be overflowed if this number is too high and code won't compile.
# 'bootloader' : 1,
 'binary_name' : 'espruino_%v_pan1780.hex',
 'build' : {
   'optimizeflags' : '-Os',
   'libraries' : [
     'BLUETOOTH',
     'NET',
     'GRAPHICS',
#     'NFC',
     'NEOPIXEL'
   ],
   'makefile' : [
     'DEFINES += -DCONFIG_GPIO_AS_PINRESET', # Allow the reset pin to work
     'DEFINES += -DBOARD_PCA10056',
     'DEFINES += -DNRF_USB=1 -DUSB',
     'DEFINES += -DNEOPIXEL_SCK_PIN=22 -DNEOPIXEL_LRCK_PIN=23', # nRF52840 needs LRCK pin defined for neopixel
     'DEFINES += -DBLUETOOTH_NAME_PREFIX=\'"PAN1780"\'',
     'NRF_SDK15=1'
   ]
 }
};


chip = {
  'part' : "NRF52840",
  'family' : "NRF52",
  'package' : "AQFN73",
  'ram' : 256,
  'flash' : 1024,
  'speed' : 64,
  'usart' : 2,
  'spi' : 3,
  'i2c' : 2,
  'adc' : 1,
  'dac' : 0,
  'saved_code' : {
    'address' : ((246 - 10) * 4096), # Bootloader takes pages 248-255, FS takes 246-247
    'page_size' : 4096,
    'pages' : 10,
    'flash_available' : 1024 - ((38 + 8 + 2 + 10)*4) # Softdevice 140 uses 38 pages of flash, bootloader 8, FS 2, code 10. Each page is 4 kb.
  },
};

devices = {
  'BTN1' : { 'pin' : 'D11', 'pinstate' : 'IN_PULLDOWN' }, # Pin negated in software
  'BTN2' : { 'pin' : 'D12', 'pinstate' : 'IN_PULLDOWN' }, # Pin negated in software
  'BTN3' : { 'pin' : 'D24', 'pinstate' : 'IN_PULLDOWN' }, # Pin negated in software
  'BTN4' : { 'pin' : 'D25', 'pinstate' : 'IN_PULLDOWN' }, # Pin negated in software
  'LED1' : { 'pin' : 'D13' }, # Pin negated in software
  'LED2' : { 'pin' : 'D14' }, # Pin negated in software
  'LED3' : { 'pin' : 'D15' }, # Pin negated in software
  'LED4' : { 'pin' : 'D16' }, # Pin negated in software
  'RX_PIN_NUMBER' : { 'pin' : 'D8'},
  'TX_PIN_NUMBER' : { 'pin' : 'D6'},
  'CTS_PIN_NUMBER' : { 'pin' : 'D7'},
  'RTS_PIN_NUMBER' : { 'pin' : 'D5'},
  # Pin D22 is used for clock when driving neopixels - as not specifying a pin seems to break things
};

def get_pins():
  pins = pinutils.generate_pins(0,47) # 48 General Purpose I/O Pins.
  pinutils.findpin(pins, "PD0", True)["functions"]["XL1"]=0; # NC
  pinutils.findpin(pins, "PD1", True)["functions"]["XL2"]=0; # NC
  pinutils.findpin(pins, "PD2", True)["functions"]["ADC1_IN0"]=0;
  pinutils.findpin(pins, "PD3", True)["functions"]["ADC1_IN1"]=0;
  pinutils.findpin(pins, "PD4", True)["functions"]["ADC1_IN2"]=0; # NC
  pinutils.findpin(pins, "PD5", True)["functions"]["RTS"]=0;
  pinutils.findpin(pins, "PD6", True)["functions"]["TXD"]=0;
  pinutils.findpin(pins, "PD7", True)["functions"]["CTS"]=0;
  pinutils.findpin(pins, "PD8", True)["functions"]["RXD"]=0;
  pinutils.findpin(pins, "PD9", True)["functions"]["NFC1"]=0;
  pinutils.findpin(pins, "PD10", True)["functions"]["NFC2"]=0;
  pinutils.findpin(pins, "PD11", True)["functions"]["NEGATED"]=0; # BTN1
  pinutils.findpin(pins, "PD12", True)["functions"]["NEGATED"]=0; # BTN2
  pinutils.findpin(pins, "PD13", True)["functions"]["NEGATED"]=0; # LED1
  pinutils.findpin(pins, "PD14", True)["functions"]["NEGATED"]=0; # LED2
  pinutils.findpin(pins, "PD15", True)["functions"]["NEGATED"]=0; # LED3
  pinutils.findpin(pins, "PD16", True)["functions"]["NEGATED"]=0; # LED4
#   pinutils.findpin(pins, "PD17", False)
#   pinutils.findpin(pins, "PD18", False) # neopixel SCK # NC
#   pinutils.findpin(pins, "PD19", False)
#   pinutils.findpin(pins, "PD20", False)
#   pinutils.findpin(pins, "PD21", False)
#   pinutils.findpin(pins, "PD22", False)
#   pinutils.findpin(pins, "PD23", False) # neopixel LRCK # NC
#   pinutils.findpin(pins, "PD26", False)
#   pinutils.findpin(pins, "PD27", False)
  pinutils.findpin(pins, "PD24", True)["functions"]["NEGATED"]=0; # BTN3
  pinutils.findpin(pins, "PD25", True)["functions"]["NEGATED"]=0; # BTN4
  pinutils.findpin(pins, "PD28", True)["functions"]["ADC1_IN4"]=0;
  pinutils.findpin(pins, "PD29", True)["functions"]["ADC1_IN5"]=0;
  pinutils.findpin(pins, "PD30", True)["functions"]["ADC1_IN6"]=0;
  pinutils.findpin(pins, "PD31", True)["functions"]["ADC1_IN7"]=0;
#   pinutils.findpin(pins, "PD32", False) # 1.00 # NC
#   pinutils.findpin(pins, "PD33", False) # 1.01
#   pinutils.findpin(pins, "PD34", False) # 1.02
#   pinutils.findpin(pins, "PD35", False) # 1.03 # NC
#   pinutils.findpin(pins, "PD36", False) # 1.04 # NC
#   pinutils.findpin(pins, "PD37", False) # 1.05 # NC
#   pinutils.findpin(pins, "PD38", False) # 1.06 # NC
#   pinutils.findpin(pins, "PD39", False) # 1.07 # NC
#   pinutils.findpin(pins, "PD40", False) # 1.08 # NC
#   pinutils.findpin(pins, "PD41", False) # 1.09 # NC
#   pinutils.findpin(pins, "PD42", False) # 1.10 # NC
#   pinutils.findpin(pins, "PD43", False) # 1.11 # NC
#   pinutils.findpin(pins, "PD44", False) # 1.12
#   pinutils.findpin(pins, "PD45", False) # 1.13
#   pinutils.findpin(pins, "PD46", False) # 1.14
#   pinutils.findpin(pins, "PD47", False) # 1.15

  # everything is non-5v tolerant
  for pin in pins:
    pin["functions"]["3.3"]=0;
  #The boot/reset button will function as a reset button in normal operation. Pin reset on PD21 needs to be enabled on the nRF52832 device for this to work.
  return pins
