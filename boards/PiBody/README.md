# PiBody Firmware
This repository contains the **custom MicroPython firmware and its files** for the PiBody robot.

It includes:
- Python modules installed into the firmware `modules/` directory
- Custom C module for the ST7789 Display Driver by russhughes installed into the  `cmodules/` directory

## Firmware Versioning
The firmware version string is defined in the MicroPython build system.

To change the firmware version name, edit the following parameter in
`makeversionhdr.py`:

```python
git_tag = "v1.26.1-atlas.v1.0.0"
```

## Building the Firmware
```bash
cd ~/micropython/ports/rp2
rm -f -rf build-RPI_PICO_W/
make clean
make BOARD=RPI_PICO_W USER_C_MODULES=cmodules
```


