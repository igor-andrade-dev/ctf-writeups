#!/usr/bin/env python3
"""Tormented Tanny - flag dividida em 3 metadados do PNG (tEXt, XMP, EXIF)."""
import re, sys
from PIL import Image

path = sys.argv[1] if len(sys.argv) > 1 else "TormentedTanny.png"
im = Image.open(path)

part1 = im.info["Title"]                                                   # chunk tEXt
xmp = im.info["XML:com.adobe.xmp"]                                         # chunk iTXt (XMP)
part2 = re.search(r"<rdf:li[^>]*>(.*?)</rdf:li>", xmp, re.S).group(1)
part3 = str(im.getexif()[0x010E])                                          # EXIF ImageDescription

print("tEXt Title :", part1)
print("XMP        :", part2)
print("EXIF       :", part3)
print("flag       :", part1 + part2 + part3)
