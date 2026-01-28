# Generate PIO header
pico_generate_pio_header(usermod ${CMAKE_CURRENT_LIST_DIR}/encoder.pio)

# Add encoder.cpp to MicroPython's usermod build
target_sources(usermod INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/encoder.cpp
)

# Include directory
target_include_directories(usermod INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}
)

# Link needed Pico SDK libraries
target_link_libraries(usermod INTERFACE
    hardware_pio
    hardware_irq
    pico_stdlib
)
