from PIL import Image
import random
import string
import os

class AndrewBased:

    def __init__(self):
        """"""
        self.base_image = Image.open('base.png')
        self.output_file_name = self._random_file_name(7)

    def get_overlay_image(self, image):
        self.overlay_image = Image.open(image)
        return self

    def convert_image(self):
        """"""
        self.overlay_image = self.overlay_image.resize((60,45), Image.ANTIALIAS)
        self.overlay_image = self.overlay_image.rotate(20)
        self.base_image.paste(self.overlay_image,(45, 100))

        self.base_image.save(self.output_file_name, quality=95)
        return self

    def builder(self, image):
        self.get_overlay_image(image).convert_image()
        return self.output_file_name

    def delete_file(self, overlay_image=None):
        os.remove(self.output_file_name)
        if overlay_image != None:
            os.remove(overlay_image)

    def _random_file_name(self, file_name_length: int):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(file_name_length)) + '.png'

