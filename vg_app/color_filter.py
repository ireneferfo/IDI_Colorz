from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

def color_is_near(picture, color):
    valid = False
    for x in picture.Color.all()[:5]:
        if distance(x.Color, color) < 20:
            valid = True
    return valid

def distance(color1, color2):
    color1_rgb = sRGBColor(*hex_to_rgb(color1))
    color2_rgb = sRGBColor(*hex_to_rgb(color2))
    color1_lab = convert_color(color1_rgb, LabColor)
    color2_lab = convert_color(color2_rgb, LabColor)
    delta_e = delta_e_cie2000(color1_lab, color2_lab)
    return delta_e

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))