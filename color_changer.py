from abc import ABC, abstractmethod
from termcolor import colored
from blinkstick import blinkstick
from colors import *


class ColorChanger(ABC):
    @abstractmethod
    def change(self, color):
        pass

    def print_color(self, color):
        if color not in mood_ring_colors:
            raise Exception('Unsupported color: ' + color)

        if color in termcolor_colors:
            if color == 'purple':
                font_color = 'blue'  # Blue on termcolor is purple
            else:
                font_color = color
            print('Color changed: ' + colored(text=color, color=font_color))
        else:
            print('Color changed: ' + color)


class BlinkstickColorChanger(ColorChanger):
    def change(self, color):
        super().print_color(color=color)
        blinkstick.find_first().set_color(hex=color)


class CommandLineColorChanger(ColorChanger):
    def change(self, color):
        super().print_color(color=color)


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
    for c in mood_ring_colors.keys():
        color_changer.change(color=c)
