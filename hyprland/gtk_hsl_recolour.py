import argparse
from pathlib import Path

import re
import colorsys

from PIL import Image

HEX_RE = re.compile(r"#[0-9a-fA-F]{6}")

RGBA_RE = re.compile(
    r"rgba\(\s*"
    r"(\d+)\s*,\s*"
    r"(\d+)\s*,\s*"
    r"(\d+)\s*,\s*"
    r"([0-9]*\.?[0-9]+)"
    r"\s*\)",
    re.IGNORECASE,
)


def handle_png(path_to_png, h_offset=0, s_offset=0, l_offset=0):
    img = Image.open(path_to_png).convert("RGBA")
    pixels = img.load()

    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]

            h, l, s = rgb_to_hls(r, g, b)

            h = (h + h_offset) % 1.0
            s = clamp(s + s_offset)
            l = clamp(l + l_offset)

            nr, ng, nb = hls_to_rgb(h, l, s)

            pixels[x, y] = nr, ng, nb, a

    img.save(path_to_png)


def clamp(value, low=0.0, high=1.0):
    return max(low, min(high, value))


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*(round(c * 255) for c in rgb))

def adjust_hex_hsl(hex_color, h_offset=0, s_offset=0, l_offset=0):
    # RGB values are 0..1
    rgb = hex_to_rgb(hex_color)

    # colorsys uses HLS order: H, L, S (not HSL!)
    h, l, s = colorsys.rgb_to_hls(*rgb)

    # relative adjustment
    h = (h + h_offset) % 1.0
    s = clamp(s + s_offset)
    l = clamp(l + l_offset)

    rgb = colorsys.hls_to_rgb(h, l, s)

    return rgb_to_hex(rgb)

def transform_hex_colors(text, h_offset=0, s_offset=0, l_offset=0):
    return HEX_RE.sub(
        lambda match: adjust_hex_hsl(
            match.group(0),
            h_offset,
            s_offset,
            l_offset,
        ),
        text,
    )


RGBA_RE = re.compile(
    r"rgba\(\s*"
    r"(\d+)\s*,\s*"
    r"(\d+)\s*,\s*"
    r"(\d+)\s*,\s*"
    r"([0-9]*\.?[0-9]+)"
    r"\s*\)",
    re.IGNORECASE,
)


def rgb_to_hls(r, g, b):
    return colorsys.rgb_to_hls(
        r / 255,
        g / 255,
        b / 255,
    )


def hls_to_rgb(h, l, s):
    rgb = colorsys.hls_to_rgb(h, l, s)
    return tuple(round(c * 255) for c in rgb)


def adjust_rgba_hsl(
    rgba,
    h_offset=0,
    s_offset=0,
    l_offset=0,
):
    match = RGBA_RE.fullmatch(rgba)

    if not match:
        return rgba

    r, g, b = map(int, match.group(1, 2, 3))
    alpha = match.group(4)

    # colorsys uses HLS: H, L, S
    h, l, s = rgb_to_hls(r, g, b)

    h = (h + h_offset) % 1.0
    s = clamp(s + s_offset)
    l = clamp(l + l_offset)

    r, g, b = hls_to_rgb(h, l, s)

    return f"rgba({r}, {g}, {b}, {alpha})"


def transform_rgba_colors(
    text,
    h_offset=0,
    s_offset=0,
    l_offset=0,
):
    return RGBA_RE.sub(
        lambda match: adjust_rgba_hsl(
            match.group(0),
            h_offset,
            s_offset,
            l_offset,
        ),
        text,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Recoloring of existing gtk themes by adjusting HSL values relatively"
    )
    parser.add_argument("src_theme")
    parser.add_argument("dest_theme")

    parser.add_argument("h")
    parser.add_argument("s")
    parser.add_argument("l")

    args = parser.parse_args()

    src_theme = Path(args.src_theme)
    dest_theme = Path(args.dest_theme)
    h = float(args.h)
    s = float(args.s)
    l = float(args.l)

    if not src_theme.exists():
        print(f"Folder at {src_theme} does not exist! Aborting!")
        return

    # Handling destination directory
    if dest_theme.exists():
        print(f"Folder at {dest_theme} exists.")
        response = ""
        while response.lower() == "y" or response.lower() == "n":
            response = input(
                "Do you want to delete its contents (if not, this will abort)? [Y/n]: "
            )
            if response == "":
                response == "y"
        if response.lower() == "y":
            # remove directory
            print(f"Removing {dest_theme}!")
            dest_theme.rmdir()
        elif response.lower() == "n":
            # abort
            print("Not changing anything. Aborting!")
            return
    dest_theme.mkdir(parents=True, exist_ok=True)

    # copying everything to the new destination
    for f in src_theme.glob("*"):
        print(f"Copying {f}")
        Path(f).copy_into(dest_theme)

    # gtk 3.0 and 4.0 css changing
    css_files = dest_theme.rglob("*.css")
    for css_file in css_files:
        print(f"Adjusting {css_file}")
        css_text = css_file.read_text()
        css_text = transform_hex_colors(
            css_text,
            h_offset=h,
            s_offset=s,
            l_offset=l,
        )
        css_text = transform_rgba_colors(
            css_text,
            h_offset=h,
            s_offset=s,
            l_offset=l,
        )
        css_file.write_text(css_text)  # replaces contents

    # png changing
    png_files = dest_theme.rglob("*.png")
    for png_file in png_files:
        print(f"Adjusting {png_file}")
        png_file_path = Path(png_file)
        handle_png(png_file_path, h_offset=h, s_offset=s, l_offset=l)

    # svg changing
    svg_files = dest_theme.rglob("*.svg")
    for svg_file in svg_files:
        print(f"Adjusting {svg_file}")
        svg_file_path = Path(svg_file)
        svg_text = svg_file_path.read_text()
        svg_text = transform_hex_colors(
            svg_text,
            h_offset=h,
            s_offset=s,
            l_offset=l,
        )
        svg_text = transform_rgba_colors(
            svg_text,
            h_offset=h,
            s_offset=s,
            l_offset=l,
        )
        svg_file_path.write_text(svg_text)  # replaces contents


if __name__ == "__main__":
    main()
