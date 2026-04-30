from machine import Pin, SPI
import st7789
from . import vga2_8x16
from . import vga2_10x20
from . import vga2_12x24
from . import vga2_16x32 

DISPLAY_BUF_SIZE = 80 * 80 * 2
BAUDRATE = 60_000_000
WIDTH = 240
HEIGHT = 320

class DisplayBase(st7789.ST7789):
    font_small = vga2_8x16
    font_medium = vga2_10x20
    font_large = vga2_12x24
    font_bold = vga2_16x32
    
    # Singleton instance
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DisplayBase, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        super().__init__(
            SPI(1, baudrate=BAUDRATE, sck=Pin("DISPLAY_SCK"), mosi=Pin("DISPLAY_MOSI")),
            WIDTH, HEIGHT,
            reset=Pin("DISPLAY_RESET", Pin.OUT),
            dc=Pin("DISPLAY_DC", Pin.OUT),
            cs=Pin("DISPLAY_CS", Pin.OUT),
            rotation=2,
            options=0,
            buffer_size=DISPLAY_BUF_SIZE)
        super().init()    
        
        self.width = WIDTH
        self.height = HEIGHT

    
    def text(self, text, x, y, font=font_small, fg=st7789.WHITE, bg=st7789.BLACK):
        super().text(font, text, x, y, fg, bg)


    def hsv(self, h, s, v):
        """
            Analogous to color() method, but uses hue, saturation, value as inputs.
            h: 0-360, 
            s: 0-1, 
            v: 0-1
        """
        if s == 0:
            r = g = b = int(v * 255)
        else:
            h %= 360
            i = int(h / 60)
            f = (h / 60) - i
            p = int(v * (1 - s) * 255)
            q = int(v * (1 - s * f) * 255)
            t = int(v * (1 - s * (1 - f)) * 255)
            v = int(v * 255)
            r, g, b = [
                (v, t, p),
                (q, v, p),
                (p, v, t),
                (p, q, v),
                (t, p, v),
                (v, p, q),
            ][i]

        return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
