# Board specific version of the frozen manifest
set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)

# Enable user C modules
set(USER_C_MODULES
    ${CMAKE_CURRENT_LIST_DIR}/cmodules
)

