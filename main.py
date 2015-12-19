import cairo
import math
import random

WIDTH = 2560
HEIGHT = 1440
SIZE = 80

FIRENZE = ['468966', 'FFF0A5', 'FFB03B', 'B64926', '8E2800']
NEUTRAL_BLUE = ['FCFFF5', 'D1DBBD', '91AA9D', '3E606F', '193441']
PHAEDRA = ['FF6138', 'FFFF9D', 'BEEB9F', '79BD8F', '00A388'][1:]
VITAMIN_C = ['004358', '1F8A70', 'BEDB39', 'FFE11A', 'FD7400']
PEAR_LEMON_FIZZ = ['04BFBF', 'CAFCD8', 'F7E967', 'A9CF54', '588F27']
BEETLE_BUS = ['730046', 'BFBB11', 'FFC200', 'E88801', 'C93C00']
JAPANESE_GARDEN = ['D8CAA8', '5C832F', '284907', '382513', '363942']
THIS_GREEN = ['00261C', '044C29', '167F39', '45BF55', '96ED89'][1:]
PURPLE_RAIN = ['25064C', '36175E', '553285', '7B52AB', '9768D1']
RED_HOT = ['450003', '5C0002', '94090D', 'D40D12', 'FF1D23']
ORANGE_CRUSH = ['EF5411', 'FA5B0F', 'FF6517', 'FF6D1F', 'FF822E']

PALETTES = [
    FIRENZE,
    NEUTRAL_BLUE,
    PHAEDRA,
    VITAMIN_C,
    PEAR_LEMON_FIZZ,
    BEETLE_BUS,
    JAPANESE_GARDEN,
    THIS_GREEN,
    PURPLE_RAIN,
    RED_HOT,
    ORANGE_CRUSH,
]

def parse_color(x):
    r = int(x[0:2], 16) / 255.0
    g = int(x[2:4], 16) / 255.0
    b = int(x[4:6], 16) / 255.0
    return (r, g, b)

def render(width, height, size, colors):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    dc = cairo.Context(surface)
    nx = width / size
    ny = height / size
    ox = (width - nx * size) / 2
    oy = (height - ny * size) / 2
    half = size / 2
    for i in range(-1, nx + 1):
        for j in range(-1, ny + 1):
            c1, c2 = random.sample(colors, 2)
            x, y = ox + i * size, oy + j * size
            dc.set_source_rgb(*parse_color(c1))
            dc.rectangle(x, y, size, size)
            dc.fill()
            dc.save()
            dc.translate(x + half, y + half)
            dc.rotate(math.pi / 2 * random.randint(0, 3))
            dc.translate(-half, -half)
            dc.set_source_rgb(*parse_color(c2))
            dc.move_to(0, 0)
            dc.arc(0, 0, size, 0, math.pi / 2)
            dc.fill()
            dc.restore()
    return surface

def common_factors(a, b):
    a = [x for x in range(1, a + 1) if a % x == 0]
    b = [x for x in range(1, b + 1) if b % x == 0]
    return sorted(set(a) & set(b))

def main():
    print 'WIDTH  = %d' % WIDTH
    print 'HEIGHT = %d' % HEIGHT
    print 'SIZE   = %d' % SIZE
    print 'GOOD_SIZES = %s' % common_factors(WIDTH, HEIGHT)
    for index, palette in enumerate(PALETTES):
        surface = render(WIDTH, HEIGHT, SIZE, palette)
        surface.write_to_png('out%03d.png' % index)

if __name__ == '__main__':
    main()
