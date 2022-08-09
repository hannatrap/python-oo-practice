"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        '''generate an incrementing serial number'''
        self.start = self.next = start


    def generate(self):
        '''generate the next number in the pattern'''
        self.next += 1
        return self.next -1

    def reset(self):
        """reset to start"""
        self.next = self.start