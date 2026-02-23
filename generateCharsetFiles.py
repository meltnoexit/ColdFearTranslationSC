import csv
import json
from PIL import Image, ImageDraw, ImageFont


def generateCharSetFiles(target_name, chars):
    text_encodings_path = f"{target_name}/text_encodings.csv"
    with open(text_encodings_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["original_encoding", "encoding"])
        for idx, item in enumerate(chars):
            if idx != 0:
                writer.writerow([int(item), idx])

    cell_width = 20
    cell_height = 24
    char_per_row = 32
    char_per_col = len(chars) // char_per_row + (
        1 if len(chars) % char_per_row != 0 else 0
    )
    image_width = cell_width * char_per_row
    image_height = cell_height * char_per_col
    palette = [0, 0, 0, 0, 255, 255, 255, 255]
    img = Image.new("P", (image_width, image_height))
    img.putpalette(palette, "RGBA")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("ChillBitmap_16px.ttf", 16)

    font_coords_path = f"{target_name}/font_coords0.csv"
    with open(font_coords_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["x1", "y1", "x2", "y2"])
        for idx, char in enumerate(chars):
            if idx == 0 or idx == 1 or idx == 2 or idx == 10:
                writer.writerow([0, 0, 0, 0])
            else:
                bbox = font.getbbox(chr(char))
                row = idx // char_per_row
                col = idx % char_per_row
                x1 = col * cell_width + bbox[0]
                y1 = row * cell_height
                x2 = x1 + (bbox[2] - bbox[0]) + 2
                draw.text((x1, y1), chr(char), fill=1, font=font)
                writer.writerow(
                    [
                        x1 / image_width,
                        (y1 + 0) / image_height,
                        x2 / image_width,
                        (y1 + 18) / image_height,
                    ]
                )

    font_raster_path = f"{target_name}/font_raster0.png"
    img.save(
        font_raster_path, optimize=False, format="PNG", compress_level=0, bitdepth=8
    )


def main():
    target_names = ("fmv", "level", "menu")
    for target_name in target_names:
        chars_extend = set()
        with open(f"{target_name}/text_sections.json", "r", encoding="utf-8-sig") as f:
            text_sections = json.load(f)
            for section in text_sections:
                for char in section:
                    chars_extend.add(ord(char))
        sorted_chars_extend = sorted(chars_extend)
        chars_base = [
            0,9,13,33,34,35,38,39,40,41,10,44,45,46,58,59,63,65,66,67,68,
            69,70,71,72,73,74,75,76,77,78,79,32,80,81,82,83,37,84,85,86,87,
            88,89,90,93,95,47,48,49,50,51,52,53,54,55,56,57,97,98,99,100,101,
            102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,
            160,169,174,231,232,233,235,237,238,239,241,243,244,246,249,250,8211,8217,8220,8221,8230
        ]
        print(f"chars base: {len(chars_base)}")
        unique_chars_extend = [
            elem for elem in sorted_chars_extend if elem not in chars_base
        ]
        chars = list(chars_base) + unique_chars_extend
        print(f"{target_name} chars: {len(chars)}")
        generateCharSetFiles(target_name, chars)


if __name__ == "__main__":
    main()
