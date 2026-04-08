from machine import Pin as _Pin

class Pin(_Pin):
    def read(self):
        """Alias for .value() method. Doesn't allow write function, for writing use .value()"""
        return self.value()