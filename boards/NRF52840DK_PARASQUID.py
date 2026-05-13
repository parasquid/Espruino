#!/bin/false
# Parasquid customisation of the upstream nRF52840 DK board definition.

from copy import deepcopy

import NRF52840DK

info = deepcopy(NRF52840DK.info)
chip = deepcopy(NRF52840DK.chip)
devices = deepcopy(NRF52840DK.devices)

if hasattr(NRF52840DK, "board"):
    board = deepcopy(NRF52840DK.board)
if hasattr(NRF52840DK, "boards"):
    boards = deepcopy(NRF52840DK.boards)

info["name"] = "nRF52840 Development Kit Parasquid"
info["boardname"] = "NRF52840DK"
info["binary_name"] = "espruino_%v_nrf52840_parasquid.hex"

chip["saved_code"]["flash_available"] = 1024 - ((38 + 8 + 2 + 10) * 4)
info["build"]["makefile"].extend(
    [
        "ESPR_BLUETOOTH_ANCS=1",
        "DEFINES += -DBLUETOOTH_NAME_PREFIX='\"nRF52840DK\"'",
    ]
)


def get_pins():
    return NRF52840DK.get_pins()
