import datetime

from os import mkdir, sep
from os.path import join, exists
from abc import ABC, abstractmethod

# Timestamp for this run
timestamp = datetime.datetime.now().strftime("%Y_%m_%dT%H_%M_%S")
image_folder_path = join(sep, 'home', 'pi', 'mood-ring-photos')
if not exists(image_folder_path):
    mkdir(image_folder_path)
timestamp_folder_path = join(image_folder_path, str(timestamp))
mkdir(timestamp_folder_path)


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
        file_name = join(timestamp_folder_path, str(base_filename) + '.jpg')
        # Takes picture.
        self.camera.capture(file_name)
        print('The picture has been stored in ' + timestamp_folder_path)
        return file_name

# TODO: Add implementation of Mac OS web camera


camera = PiCamera()
