from kb_errors import *

class kanban(object):
    """
    class docstring
    """
    def __init__(self, file_name):
        """
        Initializes instance of `kanban` class, given a file name.

        Inputs:
            file_name: File name of file containing data for a kanban board.
        Outputs:
            ---NONE---
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
                try:
                    self.tasks.append(filter(None, temp[2:len(temp)-1]))
                except IndexError:
                    self.tasks.append([])
        self.display = ''
        self.generate_display()
        self.store_display()

    def store_data(self):
        """
        Stores data in interpretable format into file with the name `self.name`.

        Inputs:
            ---NONE---
        Outpus:
            ---NONE---
        """
        with open(self.name, 'w') as f:
            for i in range(self.num_of_areas):
                [an, s, t] = [self.area_names[i], self.sizes[i], self.tasks[i]]
                line = an + ('|%d|' % s) + '|'.join(t) + '|' + '\n'
                f.write(line)

    def generate_display(self):
        """
        Generates the display from the data of an instance of this class. Stores 
        generated display in `self.display`.

        Inputs:
            ---NONE---
        Outputs:
            ---NONE---
        """
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
            contents += h_div + '\n'
        self.display = title + contents

    def store_display(self):
        """
        Writes the display in `self.display` to a text file with '-nice.txt' 
        appended to the file name.

        Inputs:
            ---NONE---
        Outputs:
            ---NONE---
        """
        with open((self.name + '-nice.txt'), 'w') as f:
            f.write(self.display)

    def print_display(self):
        """
        Prints the display in `self.display`.

        Inputs:
            ---NONE---
        Outputs:
            ---NONE---
        """
        generate_display()
        print(self.display)
        store_display()

    def add_task(self, task_name):
        """
        Add a task to first area in this kanban if there is space. Otherwise, 
        raise an AreaOutOfSpaceError.

        Inputs:
            task_name: Name of the task to be added
        Outputs:
            new_task_num: Number of the added task
        """
        # Take first available task number
        task_nums = [int(tk.split(' ')[0]) for tks in self.tasks for tk in tks]
        filt_fun = lambda n : n not in task_nums
        if task_nums != []
            new_task_num = filter(filt_fun, range(1, max(task_nums) + 2))[0]
        else:
            new_task_num = 1

        # Check to see that size of first area is not exceeded
        if len(self.tasks[0]) < self.sizes[0]:
            self.tasks[0].append(str(new_task_num) + ' ' + task_name)
            self.store_data()
        else:
            raise AreaOutOfSpaceError(self.area_names[0])
        return new_task_num

    def rem_task(self, task_num):
        """
        Remove a task from the kanban board specified by the task number if it 
        exists. Otherwise, raise a TaskDoesNotExistError.

        Inputs:
            task_num: Number of task to be removed
        Outputs:
            ---NONE---
        """
        task_nums = [int(tk.split(' ')[0]) for tks in self.tasks for tk in tks]
        if task_num in task_nums:
            for i in range(len(self.tasks)):
                for tk in self.tasks[i]:
                    if int(tk.split(' ')[0]) is task_num:
                        area_index = i
                        area = self.area_names[area_index]
                        task = tk
            choice = raw_input('Do you want to remove task \'%s\' from area \'%s\'? (Y/n) ' % (task, area))
            if choice in ['', 'y', 'Y', 'yes', 'ye', 'yea', 'ok', 'yeah']:
                self.tasks[area_index].remove(task)
                self.store_data()
            elif choice in ['n', 'N', 'no', 'nah']:
                print('Task \'%s\' in area \'%s\' was not removed.' % (task, area))
            else:
                print('Apologies, I could not interpret your response.')
        else:
            raise TaskDoesNotExistError(task_num)

    def mov_task(self, task_num, to_area):
        """
        Moves a task in the kanban board specified by the task number to another 
        area of the kanban board. If the specified destination error does not 
        exist, raise an AreaDoesNotExistError. If the specified destination area
        is out of space, raise an AreaOutOfSpaceError. If the specified task 
        does not exist, raise a TaskDoesNotExistError.

        Inputs:
            task_num: Number of task to be moved
            to_area: Area for task to be moved to
        Outputs:
            ---NONE---
        """
        # Find index of destination area if it exists; otherwise, raise an
        # AreaDoesNotExistError
        try:
            to_area_index = self.area_names.index(to_area)
        except ValueError:
            raise AreaDoesNotExistError(to_area)
        # Check to see adding the task does not exceed size of destination area
        if self.sizes[to_area_index] < (len(self.tasks[to_area_index]) + 1):
            raise AreaOutOfSpaceError(to_area)
        task_nums = [int(tk.split(' ')[0]) for tks in self.tasks for tk in tks]
        if task_num in task_nums:
            for i in range(len(self.tasks)):
                for tk in self.tasks[i]:
                    if int(tk.split(' ')[0]) is task_num:
                        area_index = i
                        area = self.area_names[area_index]
                        task = tk
            choice = raw_input('Do you want to move task \'%s\' to area \'%s\'? (Y/n)' % (task, to_area))
            if choice in ['', 'y', 'Y', 'yes', 'ye', 'yea', 'ok', 'yeah']:
                # Append the task to be moved to destination area task list
                self.tasks[to_area_index].append(task)
                # Remove the task to be moved from the origin area task list
                self.tasks[area_index].remove(task)
                self.store_data()
            elif choice in ['n', 'N', 'no', 'nah']:
                print('Task \'%s\' was not moved to area \'%s\'.' % (task, to_area))
            else:
                print('Apologies, I could not interpret your response.')
        else:
            raise TaskDoesNotExistError(task_num)
