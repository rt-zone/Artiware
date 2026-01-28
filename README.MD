# Artisan's Unified Firmware Builder

This folder contains config files to make a firmware for: 

- **PiBody**
- **ATLAS**

And any upcoming future Artisan's products.

## How to use it?

* Install micropython alongisde this repository (should be neighboring directories, don't forget to do all preparatory steps like mpy-cross and make submodules for ports/rp2)
* In case of different location of micropython please update Makefile's `MP_PATH` accordingly, or specify it during Makefile build
* Default target platform is **PiBody**, you need to specify board name (i.e. `BOARD=ATLAS`) to target other platforms for the next commands
* Run `make` to build a firmware
* Build file is located at **build/_board name_/firmware.uf2** folder 
* Run `make deploy` to upload the buildfile to an **MCU** 
* Run `make clean` to delete build folder