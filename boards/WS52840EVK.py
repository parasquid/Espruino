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


"""
source ./scripts/provision.sh ALL
rm bin/*.hex
make clean && BOARD=WS52840EVK RELEASE=1 make
uf2conv.py ./bin/*.hex -c -f 0xADA52840
mv flash.uf2 ~/Desktop/
"""

import pinutils

info = {
    "name": "Waveshare NRF52840 Eval Kit",
    "link": ["https://www.waveshare.com/wiki/NRF52840_Eval_Kit"],
    "default_console": "EV_USBSERIAL",
    # 'default_console' : "EV_SERIAL1",
    # 'default_console_tx' : "D6",
    # 'default_console_rx' : "D7",
    # 'default_console_baudrate' : "9600",
    "variables": 14000,  # How many variables are allocated for Espruino to use. RAM will be overflowed if this number is too high and code won't compile.
    # 'bootloader' : 1,
    "binary_name": "espruino_%v_ws_nrf52840ek.hex",
    "build": {
        "optimizeflags": "-Os",
        "libraries": [
            "BLUETOOTH",
            #  'NET',
            "GRAPHICS",
            # 'NFC',
            "NEOPIXEL",
            "JIT",
        ],
        "makefile": [
            "DEFINES += -DCONFIG_GPIO_AS_PINRESET",  # Allow the reset pin to work
            "DEFINES += -DNRF_USB=1 -DUSB",
            "DEFINES += -DNEOPIXEL_SCK_PIN=0 -DNEOPIXEL_LRCK_PIN=1",  # nRF52840 needs LRCK pin defined for neopixel
            "DEFINES += -DBLUETOOTH_NAME_PREFIX='\"WS52840EVK\"'",
            "DEFINES += -DESPR_UNICODE_SUPPORT=1",
            "DEFINES += -DNRF_SDH_BLE_GATT_MAX_MTU_SIZE=131",  # 23+x*27 rule as per https://devzone.nordicsemi.com/f/nordic-q-a/44825/ios-mtu-size-why-only-185-bytes
            # "DEFINES += -DPIN_NAMES_DIRECT=1",
            "LDFLAGS += -Xlinker --defsym=LD_APP_RAM_BASE=0x2ec0",  # set RAM base to match MTU
            "NRF_SDK15=1",
        ],
    },
}


chip = {
    "part": "NRF52840",
    "family": "NRF52",
    "package": "AQFN73",
    "ram": 256,
    "flash": 1024,
    "speed": 64,
    "usart": 1,
    "spi": 1,
    "i2c": 2,
    "adc": 1,
    "dac": 0,
    "saved_code": {
        "address": ((0xF4 - 2 - 96) * 4096),  # Bootloader at 0xF4000
        "page_size": 4096,
        "pages": 96,
        "flash_available": 1024
        - (
            (0x26 + 0x20 + 2 + 96) * 4
        ),  # Softdevice 140 uses 38 pages of flash, bootloader 8, FS 2, code 10. Each page is 4 kb.
    },
}

# left-right, or top-bottom order
board = {}

devices = {
    "BTN1": {"pin": "D11", "pinstate": "IN_PULLUP", "inverted": 1},
    "LED1": {"pin": "D13"},  # Pin negated in software
    "LED2": {"pin": "D14"},
    "LED3": {"pin": "D41"},
    "LED4": {"pin": "D16"},
    "NFC": {"pin_a": "D9", "pin_b": "D10"},  # doesn't work on SDK15 yet
    "TX_PIN_NUMBER": {"pin": "D6"},
    "CTS_PIN_NUMBER": {"pin": "D7"},
    "RX_PIN_NUMBER": {"pin": "D8"},
    "RTS_PIN_NUMBER": {"pin": "D25"},
}


# schematic: https://www.waveshare.com/w/upload/f/f2/NRF52840-Eval-Kit-Schematic.pdf
def get_pins():
    pins = pinutils.generate_pins(0, 47)  # 48 General Purpose I/O Pins.

    pinutils.findpin(pins, "PD2", True)["functions"]["ADC1_IN0"] = 0
    pinutils.findpin(pins, "PD3", True)["functions"]["ADC1_IN1"] = 0
    pinutils.findpin(pins, "PD4", True)["functions"]["ADC1_IN2"] = 0
    pinutils.findpin(pins, "PD5", True)["functions"]["ADC1_IN3"] = 0
    pinutils.findpin(pins, "PD28", True)["functions"]["ADC1_IN4"] = 0
    pinutils.findpin(pins, "PD29", True)["functions"]["ADC1_IN5"] = 0
    pinutils.findpin(pins, "PD30", True)["functions"]["ADC1_IN6"] = 0
    pinutils.findpin(pins, "PD31", True)["functions"]["ADC1_IN7"] = 0

    pinutils.findpin(pins, "PD6", True)["functions"]["TXD"] = 0
    pinutils.findpin(pins, "PD7", True)["functions"]["CTS"] = 0
    pinutils.findpin(pins, "PD8", True)["functions"]["RXD"] = 0
    pinutils.findpin(pins, "PD25", True)["functions"]["RTS"] = 0

    pinutils.findpin(pins, "PD9", True)["functions"]["NFC1"] = 0
    pinutils.findpin(pins, "PD10", True)["functions"]["NFC2"] = 0

    pinutils.findpin(pins, "PD13", True)["functions"]["NEGATED"] = 0
    # LED1

    # everything is non-5v tolerant
    for pin in pins:
        pin["functions"]["3.3"] = 0

    return pins


# 0
# 1
# 2 AREF
# 3 A0
# 4 A1
# 5 LDR
# 6 TX
# 7 RX
# 8 CTS
# 9 NFC1
# 10 NFC2
# 11 BTN1
# 12 CS
# 13 LED1
# 14 LED2
# 15 BUZZER
# 16 LED4
# 17 CLK
# 18 RESET
# 19 rpi (TX)
# 20 MISO
# 21 rpi (RX)
# 22 rpi (SCL)
# 23 rpi (CE0)
# 24 MOSI
# 25 RTS
# 26 D14
# 27 D15
# 28 A2
# 29 A3
# 30 A4
# 31 A5
# 32 1.00 rpi (SDA)
# 33 1.01 D0
# 34 1.02 D1
# 35 1.03 D2
# 36 1.04 D3
# 37 1.05 D4
# 38 1.06 D5
# 39 1.07 D6
# 40 1.08 D7
# 41 1.09 LED3
# 42 1.10 D8
# 43 1.11 D9
# 44 1.12 D10
# 45 1.13 D11
# 46 1.14 D12
# 47 1.15 D13

# pinmapping = {
#     "D0": "PD33",
#     "D1": "PD34",
#     "D2": "PD35",
#     "D3": "PD36",
#     "D4": "PD37",
#     "D5": "PD38",
#     "D6": "PD39",
#     "D7": "PD40",
#     "D8": "PD42",
#     "D9": "PD43",
#     "D10": "PD44",
#     "D11": "PD45",
#     "D12": "PD46",
#     "D13": "PD47",
#     "D14": "PD26",
#     "D15": "PD27",
#     "A0": "PD3",
#     "A1": "PD4",
#     "A2": "PD28",
#     "A3": "PD29",
#     "A4": "PD30",
#     "A5": "PD31",
# }


# scripts/build_platform_config.py WS52840EVK gen/platform_config.h
