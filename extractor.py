#!/usr/bin/env python3

import argparse
import os
import pathlib
import typing as tp

import tabulate
from PIL import ExifTags
from PIL import Image

mode_to_bpp = {'1': 1, 'L': 8, 'P': 8, 'RGB': 24, 'RGBA': 32, 'CMYK': 32, 'YCbCr': 24, 'I': 32, 'F': 32}


def get_image_info(path: str) -> tp.Tuple[tp.Optional[str], ...]:
    image = Image.open(path)

    return (
        image.filename,
        f"{image.size[0]}x{image.size[1]}",
        image.info.get('dpi', (0, 0))[0],
        f"{image.mode} ({mode_to_bpp[image.mode]})",
        image.info.get('compression')
    )


def get_exif(img: Image) -> tp.Dict[str, str]:
    info = img._getexif()
    exif_obj = {}
    if info is not None:
        for tag, value in info.items():
            decoded = ExifTags.TAGS.get(tag, tag)
            exif_obj[decoded] = value

    return exif_obj


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Metadata extractor")
    parser.add_argument("-d", "--directory", action="store", default="./",
                        type=pathlib.Path, help="directory with images")

    root = parser.parse_args().directory
    for dirname, _, files in os.walk(root, followlinks=False):
        print(f"Directory: {dirname}")

        table = []
        for file in files:
            path = os.path.join(dirname, file)

            try:
                table.append(get_image_info(path))
            except IOError:
                pass

        if table:
            print(tabulate.tabulate(
                table,
                headers=("filename", "size", "dpi", "channels (depth)", "compression"),
                tablefmt="grid")
            )
        else:
            print("No images found")

    print("Press Enter to continue ...")
    input()
