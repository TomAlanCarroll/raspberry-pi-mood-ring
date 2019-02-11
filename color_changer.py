import time

from abc import ABC, abstractmethod
from termcolor import colored
from blinkstick import blinkstick
from colors import *


class ColorChanger(ABC):
    @abstractmethod
    def change(self, name, hex):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def print_color(self, name, hex):
        if name not in mood_ring_colors:
            raise Exception('Unsupported color: ' + name)

        if name in termcolor_colors:
            if name == 'purple':
                font_color = 'blue'  # Blue on termcolor is purple
            else:
                font_color = name
            print('[INFO] Color changed: ' + colored(text=name + '(' + hex + ')', color=font_color))
        else:
            print('[INFO] Color changed: ' + name + '(' + hex + ')')


class BlinkstickColorChanger(ColorChanger):
    def change(self, name, hex):
        super().print_color(name=name, hex=hex)
        blinkstick.find_first().morph(hex=hex, duration=500)

    def turn_off(self):
        blinkstick.find_first().turn_off()
        print('[INFO] Turned off blinkstick')


class CommandLineColorChanger(ColorChanger):
    def change(self, name, hex):
        super().print_color(name=name, hex=hex)

    def turn_off(self):
        pass


color_changer = None

try:
    blinkstick.find_first()
    color_changer = BlinkstickColorChanger()
    print('[INFO] Using blinkstick')
except:
    color_changer = CommandLineColorChanger()
    print('[INFO] Unable to find blinkstick. Color changes will be in command line only.')

if __name__ == "__main__":
    # Test out the color changer
    for color_name, color_hex in mood_ring_colors.items():
        color_changer.change(name=color_name, hex=color_hex)
        time.sleep(3)  # seconds

    color_changer.turn_off()
