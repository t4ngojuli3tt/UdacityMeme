import os
from PIL import Image, ImageDraw, ImageFont
from random import randint, random, uniform


class MemeEngine:
    """A class to create  memes."""

    def __init__(self, output_dir: str, font_path: str = 'MemeGenerator/font.ttf'):
        """A init method that set two attrributes:
        output_dir - path to directory where new memes will be created;
        font_path - path to font that will be use to write quotes in memes. 
        """

        self.output_dir = output_dir
        self.font_path = font_path

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """ Method to creat memems 
        """
        if img_path.split('.')[-1] != 'jpg':
            raise Exception('Required path to jpg image!')

        name = img_path.split('/')[-1]
        path = self.output_dir+'/'+name
        if os.path.isfile(path):
            x = 2
            while os.path.isfile(path):
                path = self.output_dir+'/' + \
                    name.split('.')[0] + f'v{x}'+'.' + name.split('.')[1]
                x += 1

        with Image.open(img_path) as im:
            if im.width > width:
                new_width = width
                new_height = int(new_width/im.width * im.height)
                im = im.resize((new_width, new_height))

            draw = ImageDraw.Draw(im)

            font_size = int(uniform(30, 45))
            font = ImageFont.truetype(self.font_path, font_size)

            quote = f'{text}\n      - {author}'
            text_width, text_height = draw.textsize(quote, font=font)

            text_x = uniform(5, im.width - text_width)
            text_y = uniform(5, im.height - text_height)
            draw.text((text_x, text_y), quote,
                      fill=(255, 255, 255, 128), font=font)

            im.save(path)

        return path
