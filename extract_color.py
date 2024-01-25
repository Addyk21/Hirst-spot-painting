import colorgram


def get_palette():
    rgb_color = []
    colors = colorgram.extract('Hirst_dot.png', 30)

    for values in colors:
        r = values.rgb.r
        g = values.rgb.g
        b = values.rgb.b
        new_color = (r, g, b)
        rgb_color.append(new_color)
    return rgb_color


