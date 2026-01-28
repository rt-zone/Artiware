MP_PATH ?= ../micropython
BOARD ?= PiBody
MP_PORT := $(MP_PATH)/ports/rp2
BOARD_DIR := $(PWD)/boards/$(BOARD)
BUILD_DIR := $(PWD)/build/$(BOARD)

all:
	$(MAKE) -C $(MP_PORT) \
		BOARD_DIR=$(BOARD_DIR) \
		BUILD=$(BUILD_DIR)

clean: 
	$(RM) -rf $(BUILD_DIR)

deploy: all
	sudo picotool load -x $(BUILD_DIR)/firmware.uf2

