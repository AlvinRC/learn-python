from shapes.circle import area, circumference, big_pie
from string_formatter import prettify

if __name__ == '__main__':
    r = int(input('Radius: '))

    area_str = prettify(area(r))
    circ_str = prettify(circumference(r), 3)
    bpie_str = prettify(big_pie, 7)

    print(f'Area: {area_str}')
    print(f'Circumference: {circ_str}')
    print(f'Big Pie: {bpie_str}')
