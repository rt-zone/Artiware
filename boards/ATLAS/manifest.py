include("$(PORT_DIR)/boards/manifest.py")

require("bundle-networking")

# Bluetooth
require("aioble")

# Custom frozen files
freeze("./modules")