#!/usr/bin/env python
import subprocess
import matplotlib as mt

RGB_ORIGINAL = input(f"Colour name(leave blank for HEX code):\n> ")
RGB_ORIGINAL = RGB_ORIGINAL.lower().replace(" ", "")
try:
    RGB_ORIGINAL = mt.colors.cnames[RGB_ORIGINAL].replace("#", "")
except:
    RGB_ORIGINAL = ""

if RGB_ORIGINAL == "":
    RGB_ORIGINAL = input(f"RGB hex code (000000):\n> ")
    if RGB_ORIGINAL == "":
        RGB_ORIGINAL = "000000"
# print(f"#{RGB_ORIGINAL}")

r, g, b = (RGB_ORIGINAL[i : i + 2] for i in range(0, len(RGB_ORIGINAL), 2))
r, g, b = [a.upper() for a in [r, g, b]]
print(f"\033[48:2::{int(r,16)}:{int(g,16)}:{int(b,16)}m  {RGB_ORIGINAL}\033[49m")


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
A2:14:FF:{b}:{g}:{r},
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

# print(hexstuff)

subprocess.run(
    ["qdbus6", "org.kde.klipper", "/klipper", "setClipboardContents", hexstuff]
)
