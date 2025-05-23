STM32=1

DEFINES += -DSTM32 -DUSE_STDPERIPH_DRIVER=1 -D$(CHIP) -D$(STLIB)
INCLUDE += -I$(ROOT)/targets/stm32
ifndef BOOTLOADER
 SOURCES +=                              \
 targets/stm32/main.c                    \
 targets/stm32/jshardware.c              \
 targets/stm32/stm32_it.c                
 ifdef USE_BOOTLOADER
  BUILD_LINKER_FLAGS+=--using_bootloader
  # -k applies bootloader hack for Espruino 1v3 boards
  ifdef MACOSX
    STM32LOADER_FLAGS+=-k -p /dev/tty.usbmodem*
  else
    STM32LOADER_FLAGS+=-k -p /dev/ttyACM0
  endif
  BASEADDRESS=$(shell python scripts/get_board_info.py $(BOARD) "hex(0x08000000+common.get_espruino_binary_address(board))")
 endif # USE_BOOTLOADER
else # !BOOTLOADER
 ifndef USE_BOOTLOADER
 $(error Using bootloader on device that is not expecting one)
 endif
 DEFINES+=-DSAVE_ON_FLASH # hack, as without link time optimisation the always_inlines will fail (even though they are not used)
 BUILD_LINKER_FLAGS+=--bootloader
 PROJ_NAME=$(BOOTLOADER_PROJ_NAME)
 WRAPPERSOURCES =
 SOURCES = \
 targets/stm32_boot/main.c \
 targets/stm32_boot/utils.c
endif # BOOTLOADER

# ==============================================================
include make/common/ARM.make

proj: $(PROJ_NAME).lst $(PROJ_NAME).bin

flash: $(PROJ_NAME).bin
ifdef USE_DFU
	sudo dfu-util -a 0 -s 0x08000000 -D $(PROJ_NAME).bin
else ifeq ($(BOARD),OLIMEXINO_STM32_BOOTLOADER) 
	@echo Olimexino Serial bootloader
	dfu-util -a1 -d 0x1EAF:0x0003 -D $(PROJ_NAME).bin
else ifdef NUCLEO
	if [ -d "/media/$(USER)/NUCLEO" ]; then cp $(PROJ_NAME).bin /media/$(USER)/NUCLEO;sync; fi
	if [ -d "/media/NUCLEO" ]; then cp $(PROJ_NAME).bin /media/NUCLEO;sync; fi
else
	@echo "-- ST-Link flash: reset the target, then immediately press any key to proceed";
	@if read -n 1 -s && st-flash --reset write $(PROJ_NAME).bin $(BASEADDRESS); then \
		echo "ST-Link flashed OK"; \
	else \
		echo "-- J-Link flash"; \
		echo "USB\nconnect\nloadfile $(PROJ_NAME).bin $(BASEADDRESS)\nexit" > JLinkCommands.txt; \
		JLinkExe -device $(CHIP) -if SWD -speed 4000 -CommandFile JLinkCommands.txt; \
		rm JLinkCommands.txt; \
	fi
endif

serialflash: all
	@echo STM32 inbuilt serial bootloader, set BOOT0=1, BOOT1=0
	python2.7 scripts/stm32loader.py -b 460800 -a $(BASEADDRESS) -ew $(STM32LOADER_FLAGS) $(PROJ_NAME).bin
#	python2.7 scripts/stm32loader.py -b 460800 -a $(BASEADDRESS) -ewv $(STM32LOADER_FLAGS) $(PROJ_NAME).bin


