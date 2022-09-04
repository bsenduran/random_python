# 04 September 2022
from PIL import Image

image = Image.open('dragon48.jpg')
pixel = image.load()

ascii_chars = 'Ñ@#W$9876543210?!abc;:+=-,._   ' # https://play.ertdfgcvb.xyz/


def interpolate(x, actual_range, map_range):
    actual_lenght = actual_range[1] - actual_range[0]
    d = x  - actual_range[0]
    map_lenght = map_range[1] - map_range[0]
    return int(d * map_lenght / actual_lenght)


def get_ascii_chars_index_for_rgb(rgbtuple):
    gray_scale_value = (rgbtuple[0] + rgbtuple[1]  +rgbtuple[2] ) / 3
    interpolated_value = interpolate(gray_scale_value, (0,255), (0,len(ascii_chars)-1))
    return interpolated_value


for j in range(0,image.size[1]):
    for i in range(0,image.size[0]):
        print(ascii_chars[get_ascii_chars_index_for_rgb(pixel[i,j])], end=' ')
    print()



