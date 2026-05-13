#!/bin/false
# Parasquid customisation of the upstream ESP32 board definition.

from copy import deepcopy

import ESP32

info = deepcopy(ESP32.info)
chip = deepcopy(ESP32.chip)
devices = deepcopy(ESP32.devices)

if hasattr(ESP32, "board"):
    board = deepcopy(ESP32.board)
if hasattr(ESP32, "boards"):
    boards = deepcopy(ESP32.boards)

info["name"] = "ESP32 Parasquid"
info["boardname"] = "ESP32"
info["binary_name"] = "espruino_%v_esp32_parasquid.bin"

libraries = info["build"]["libraries"]
if "FLASHFS" not in libraries:
    libraries.insert(libraries.index("BLUETOOTH"), "FLASHFS")


def get_pins():
    return ESP32.get_pins()
