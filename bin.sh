#!/bin/bash
make clean && BOARD=$1 make
mv *.bin *.hex *.zip /espruino/builds
