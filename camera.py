import datetime

from os import mkdir
from os.path import join
from abc import ABC, abstractmethod

# Timestamp for this run
timestamp = datetime.datetime.now().strftime("%Y_%m_%dT%H_%M_%S")
folder_path = join('home', 'pi', str(timestamp))
mkdir(folder_path)


class Camera(ABC):
    @abstractmethod
    def capture(self, base_filename):
        pass


class PiCamera(Camera):
    def __init__(self):
        import picamera
        # Initializes PI camera.
        self.camera = picamera.PiCamera()

    def capture(self, base_filename):
        import picamera
        file_name = join(folder_path, str(base_filename) + '.jpg')
        # Takes picture.
        self.camera.capture(file_name)
        print('The picture has been stored in ' + folder_path)
        return file_name

# TODO: Add implementation of Mac OS web camera


camera = PiCamera()
