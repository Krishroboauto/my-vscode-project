import colorgram

colors = colorgram.extract("18.Day18/damien-hirst-l-isoleucine-2018-auction.jpg", 30)
#print(colors)

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r,g,b))
print(color_list)