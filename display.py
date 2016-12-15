"""
+-------+-------+------+\n
| To do | Doing | Done |\n
+-------+-------+------+\n
|       |       |      |\n
|       |       |      |\n
|       |       |      |\n
+-------+-------+------+
"""

def display(num, names, heights, contents)
    num_of_areas = num # User input
    area_names = names # User input
    # Initialize widths of areas
    widths = [len(name) for name in area_names]
    sizes = heights # User input

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

if __name__ == "__main__":
    num_of_areas = 3
    area_names = ['To do', 'Doing', 'Done']
    sizes = [3, 3, 3]