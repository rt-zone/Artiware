from machine import ADC as _ADC


class ADC(_ADC):
    """ADC Extension class, only purpose is to add .read() function that returns normalized value"""
    def read(self):
        """Returns ADC value normalized from 0 to 1. Note, that ADC is normally 16 bytes"""
        return self.read_u16() / 65535