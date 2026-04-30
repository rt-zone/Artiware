MYROBOT_MOD_DIR := $(USERMOD_DIR)

SRC_USERMOD += \
    $(MYROBOT_MOD_DIR)/encoder.cpp

# Optional: expose qstr definitions
CFLAGS_USERMOD += -DMODULE_ENCODER_ENABLED=1
