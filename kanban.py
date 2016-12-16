class kanban(object):
    """
    """
    def __init__(self, file_name):
        """
        """
        self.name = file_name
        self.num_of_areas = 0
        self.area_names = []
        self.sizes = []
        self.tasks = []
        with open(file_name, 'r') as f:
            for line in f:
                self.num_of_areas += 1
                temp = line.split('|')
                self.area_names.append(temp[0])
                self.sizes.append(int(temp[1]))
                self.tasks.append(temp[2:len(temp)-1])
        self.display = ''
    def store_data(self):
        """
        """
        with open(self.name, 'w') as f:
            for i in range(self.num_of_areas):
                [an, s, t] = [self.area_names[i], self.sizes[i], self.tasks[i]]
                line = an + ('|%d|' % s) + '|'.join(t) + '|'
                if i is not (self.num_of_areas-1):
                    line += '\n'
                f.write(line)
    def store_display(self):
        """
        """
        with open((self.name + '-nice.txt'), 'w') as f:
            # Find width of each area
            widths = []
            for i in range(len(self.tasks)):
                lengths = [len(task) for task in self.tasks[i]]
                width = max(lengths + [len(self.area_names[i])])
                widths.append(width)
            # Generate horizontal divider
            h_div = ''
            for i in range(len(widths)):
                width = widths[i]
                h_div += '+' + (width+2) * '-'
                if i is (len(widths)-1):
                    h_div += '+'
            # Generate table title display
            title = h_div + '\n'
            for i in range(self.num_of_areas):
                name = self.area_names[i]
                width = widths[i]
                title += '| ' + name + (width-len(name)+1) * ' '
                if i is self.num_of_areas-1:
                    title += '|\n'
            title += h_div + '\n'
            # Generate table contents display
            contents = h_div + '\n'
            for i in range(max(self.sizes)):
                for j in range(self.num_of_areas):
                    width = widths[j]
                    # A task exists
                    if i < len(self.tasks[j]):
                        task = self.tasks[j][i]
                        contents += '| ' + task + (width-len(task)+1) * ' '
                    # This area still has spaces available
                    elif i >= len(self.tasks[j]) and i < self.sizes[j]:
                        contents += '|' + (width+2) * ' '
                    # This area is full
                    else:
                        contents += '|' + (width+2) * '~'
                    # End of row - new line
                    if j is self.num_of_areas-1:
                        contents += '|\n'
                contents += h_div
                if i is not max(self.sizes)-1:
                    contents += '\n'
            self.display = title + contents
            f.write(self.display)
    def print_display(self):
        """
        """
        print(self.display)
    def add_task(self, task):
        """
        Add task
        """
        # Return task number
        store_data()
    def rem_task(self, task):
        """
        """
        store_data()
