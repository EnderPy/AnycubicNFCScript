#!/usr/bin/env python
import subprocess
import sys
import matplotlib as mt
import pyperclip

clipboard = False
print_output = True
has_colour_data = False
has_material_data = False


def hex_to_rgba(RGB_ORIGINAL: str) -> tuple:
    if len(RGB_ORIGINAL) == 8:
        t, r, g, b = (RGB_ORIGINAL[i : i + 2] for i in range(0, 8, 2))
    else:
        t = "FF"
        r, g, b = (RGB_ORIGINAL[i : i + 2] for i in range(0, 6, 2))
    r, g, b, t = [a.upper() for a in [r, g, b, t]]
    return t, r, g, b


def name_to_rgb(name: str) -> tuple:
    RGB_ORIGINAL = mt.colors.cnames[name].replace("#", "")
    return hex_to_rgba(RGB_ORIGINAL)


for index, item in enumerate(sys.argv):
    if item == "--copy":
        clipboard = True
    if item == "--no-print":
        print_output = False
    if item == "--hex":
        has_colour_data = True
        RGB_ORIGINAL = sys.argv[index + 1].lstrip("#")
        t, r, g, b = hex_to_rgba(RGB_ORIGINAL)
    if item == "--colour" or item == "-color":
        has_colour_data = True
        t, r, g, b = name_to_rgb(sys.argv[index + 1])
    if item == "--material":
        has_material_data = True
        MATERIAL = sys.argv[index + 1]


if not has_colour_data:
    while True:
        RGB_ORIGINAL = input("Colour name (leave blank for HEX code):\n> ")
        if RGB_ORIGINAL == "":
            break
        try:
            t, r, g, b = name_to_rgb(RGB_ORIGINAL)
            break
        except:
            continue
    while True:
        RGB_ORIGINAL = input("RGB hex code (with optional transparency, e.g., #66000000 or #123123):\n> ")
        RGB_ORIGINAL = RGB_ORIGINAL.lstrip("#")
        if RGB_ORIGINAL == "":
            continue
        if len(RGB_ORIGINAL) not in [6, 8]:
            print("Not the right length (6 or 8)")
            continue
        t, r, g, b = hex_to_rgba(RGB_ORIGINAL)
        break


if print_output:
    print(f"\033[48:2::{int(r,16)}:{int(g,16)}:{int(b,16)}m  {RGB_ORIGINAL}\033[49m")
if not has_material_data:
    MATERIAL = input(f"Material type (length<=4) (PLA+)\n>")
    if MATERIAL == "":
        MATERIAL = "PLA+"
M = list(MATERIAL)
# for m in M:
#     m.encode("utf-8").hex().upper()
M = [m.encode("utf-8").hex().upper() for m in M]
if len(M) <= 20:
    M += ["00"] * (20 - len(M))
# print(M)

# A2:02:A1:A3:00:00,
# A2:03:E1:10:12:00,
hexstuff = f"""A2:04:7B:00:65:00,
A2:05:41:48:50:4C,
A2:06:50:42:57:2D,
A2:07:31:30:32:00,
A2:08:00:00:00:00,
A2:09:00:00:00:00,
A2:0A:41:43:00:00,
A2:0B:00:00:00:00,
A2:0C:00:00:00:00,
A2:0D:00:00:00:00,
A2:0E:00:00:00:00,
A2:0F:{M[0]}:{M[1]}:{M[2]}:{M[3]},
A2:10:{M[4]}:{M[5]}:{M[6]}:{M[7]},
A2:11:{M[8]}:{M[9]}:{M[10]}:{M[11]},
A2:12:{M[12]}:{M[13]}:{M[14]}:{M[15]},
A2:13:{M[16]}:{M[17]}:{M[18]}:{M[19]},
A2:14:{t}:{b}:{g}:{r},
A2:15:00:00:00:00,
A2:16:00:00:00:00,
A2:17:32:00:64:00,
A2:18:CD:00:D7:00,
A2:19:00:00:00:00,
A2:1A:00:00:00:00,
A2:1B:00:00:00:00,
A2:1C:00:00:00:00,
A2:1D:32:00:3C:00,
A2:1E:AF:00:4A:01,
A2:1F:E8:03:00:00,
A2:20:00:00:00:00,
A2:21:00:00:00:00,
A2:22:00:00:00:00,
A2:23:00:00:00:00,
A2:24:00:00:00:00,
A2:25:00:00:00:00,
A2:26:00:00:00:00,
A2:27:00:00:00:00,
A2:28:00:00:00:BD,
A2:29:04:00:00:04,
A2:2A:47:00:00:00,
A2:2B:00:00:00:00,
A2:2C:00:00:00:00"""


if print_output:
    print("\n" + hexstuff + "\n")


if clipboard:
    pyperclip.copy(hexstuff)
