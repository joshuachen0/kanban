"""
+-------+-------+------+\n
| To do | Doing | Done |\n
+-------+-------+------+\n
|       |       |      |\n
|       |       |      |\n
|       |       |      |\n
+-------+-------+------+
"""

def display(num, names, heights, contents):
    # Number of areas
    num_of_areas = num
    # Names of areas
    area_names = names
    # Initialize widths of areas
    widths = [len(name) for name in area_names]
    # Number of spaces available in each area
    sizes = heights

    # Generate textual display of kanban
    h_div = ''
    for width in widths:
        h_div += '+' + (width+2) * '-'
        if width is widths[len(widths)-1]:
            h_div += '+'

    display = ''
    display += h_div + '\n'
    for name in area_names:
        display += '| ' + name + ' '
        if name is area_names[len(area_names)-1]:
            display += '|\n'
    display += h_div + '\n'
    for _ in xrange(max(sizes)):
        for width in widths:
            display += '|' + (width+2) * ' '
            if width is widths[len(widths)-1]:
                display += '|\n'
    display += h_div
    print(display)

if __name__ == "__main__":
    num_of_areas = input('Number of areas: ')
    #area_names = ['To do', 'Doing', 'Done']
    area_names = []
    sizes = []
    for i in range(num_of_areas):
        area_names.append(raw_input('Name of area %d: ' % (i+1)))
        sizes.append(input('Size of area %d: ' % (i+1)))
    #sizes = [3, 3, 3]