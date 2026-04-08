from machine import PWM as _PWM

class PWM(_PWM):
    """Normalized duty_u16 function. Returns current duty value normalized when no value argument given. Sets duty value from 0 to 1. Silently maps values from 0 to 1, if incrrect value were  given."""
    def duty(self, value = None):
        if value == None:
            return self.duty_u16() / 65535
        value = min(1, value)
        value = max(0, value)
        self.duty_u16(int(value * 65535))