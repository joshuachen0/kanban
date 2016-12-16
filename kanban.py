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
        self.contents = []
        with open(file_name, 'r') as f:
            for line in f:
                self.num_of_areas += 1
                temp = line.split('|')
                self.area_names.append(temp[0])
                self.sizes.append(int(temp[1]))
                self.contents.append(temp[2:len(temp)-1])
    def store_data(self):
        """
        """
        with open(self.name, 'w') as f:
            for i in range(self.num_of_areas):
                [an, s, c] = [area_names[i], sizes[i], contents[i]]
                line = an + ('|%d|' % s) + '|'.join(c) + '|'
                if i is not self.num_of_areas:
                    line += '\n'
                f.write(line)
    def store_display(self):
        """
        """
        with open((self.name + '-nice'), 'w') as f:
            # Number of areas
            num_of_areas = self.num_of_areas
            # Names of areas
            area_names = self.names
            # Initialize widths of areas
            widths = [len(nm) for nm in area_names]
            # Number of spaces available in each area
            sizes = heights
    def print_display(self):
        """
        """