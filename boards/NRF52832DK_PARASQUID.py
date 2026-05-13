#!/bin/false
# Parasquid customisation of the upstream nRF52832 DK board definition.

from copy import deepcopy

import NRF52832DK

info = deepcopy(NRF52832DK.info)
chip = deepcopy(NRF52832DK.chip)
devices = deepcopy(NRF52832DK.devices)

if hasattr(NRF52832DK, "board"):
    board = deepcopy(NRF52832DK.board)
if hasattr(NRF52832DK, "boards"):
    boards = deepcopy(NRF52832DK.boards)

info["name"] = "nRF52 Development Kit Parasquid"
info["boardname"] = "NRF52832DK"
info["binary_name"] = "espruino_%v_nrf52832_parasquid.hex"

makefile = info["build"]["makefile"]
makefile.append("DEFINES+=-DBLUETOOTH_NAME_PREFIX='\"nRF52832DK\"'")
for line in [
    "LDFLAGS += -nostartfiles",
    "ASFLAGS += -D__STARTUP_CLEAR_BSS -D__START=main",
]:
    if line in makefile:
        makefile.remove(line)


def get_pins():
    return NRF52832DK.get_pins()
