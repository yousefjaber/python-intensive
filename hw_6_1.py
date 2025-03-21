import os
from PIL import Image, ImageDraw, ImageFont
from my_data_classes import Point


class ImageUpdater:
    def __init__(self, file_name: str) -> None:
        self.__source_file_name: str = file_name
        self.source_image: Image = None

    def __enter__(self) -> "ImageUpdater":
        self.source_image = Image.open(self.__source_file_name).convert("RGBA")
        return self

    def __exit__(self, type, value, tb) -> None:
        self.source_image.close()

    def draw_watermark(self, text_to_draw: str, background_color: str, text_color: str, position: Point) -> None:
        font_path = os.path.join("assets", "fonts", "AdobeVFPrototype.ttf")
        try:
            font = ImageFont.truetype(font_path, size=20)
        except IOError:
            font = ImageFont.load_default()
        
        draw = ImageDraw.Draw(self.source_image)
        rect_width, rect_height = 200, 100
        draw.rectangle(
            xy=[position.to_tuple(), (position.x + rect_width, position.y + rect_height)], 
            fill=background_color
        )
        draw.text((position.x + 20, position.y + 25), text_to_draw, fill=text_color, font=font)

    def save_changes(self, output_file_name: str) -> None:
        self.source_image.save(output_file_name, "PNG")


if __name__ == "__main__":
    positions = [Point(50, 50), Point(300, 50), Point(150, 200)]
    configs = [
        ("We are learning\nPython", "black", "white", positions[0], "black.png"),
        ("We are learning\nPython", "yellow", "black", positions[1], "yellow.png"),
        ("We are learning\nPython", "blue", "white", positions[2], "blue.png")
    ]
    
    for text, bg_color, text_color, pos, output in configs:
        with ImageUpdater(file_name=os.path.join("assets", "images", "salvador.jpeg")) as updater:
            updater.draw_watermark(text_to_draw=text, background_color=bg_color, text_color=text_color, position=pos)
            updater.save_changes(output_file_name=output)
