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
                    self.tasks.append(temp[2:len(temp)-1])
                except IndexError:
                    self.tasks.append([])
        self.display = ''
        self.generate_display()
        self.store_display()

    """
    def get_tasks(self):
        """
        Returns a dictionary of task numbers : task names.

        Inputs:
            ---NONE---
        Outputs:
            tasks_dict: a dictionary of task numbers : task names of tasks in 
                this kanban board
        """
        tasks_dict = {}
        for tasks in self.tasks:
            for task in tasks:
                temp = task.split(' ')
                tasks_dict[int(temp[0])] = ' '.join(temp[1:len(temp)])
        return tasks_dict
    """

    def store_data(self):
        """
        function docstring
        """
        with open(self.name, 'w') as f:
            for i in range(self.num_of_areas):
                [an, s, t] = [self.area_names[i], self.sizes[i], self.tasks[i]]
                line = an + ('|%d|' % s) + '|'.join(t) + '|'
                if i is not (self.num_of_areas-1):
                    line += '\n'
                f.write(line)

    def generate_display(self):
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
        function docstring
        """
        with open((self.name + '-nice.txt'), 'w') as f:
            f.write(self.display)

    def print_display(self):
        """
        function docstring
        """
        print(self.display)

    def add_task(self, task_name):
        """
        Add a task to first area in this kanban if there is space. Otherwise, 
        raise an AreaOutOfSpaceError.

        Inputs:
            task_name: Name of the task to be added
        Outputs:
            new_task_num: Number of the added task
        """
        # Return task number
        num_of_tasks = sum(len(task) for task in self.tasks)
        new_task_num = num_of_tasks + 1
        # Check to see that size of first area is not exceeded
        if len(self.tasks[0]) < self.sizes[0]:
            self.tasks[0].append(new_task_num + ' ' + task_name)
            store_data()
        else:
            raise AreaOutOfSpaceError(self.tasks[0])

    def rem_task(self, task_num):
        """
        function docstring
        remove task
        """
        tasks_nums = [int(tk.split(' ')[0]) for tks in self.tasks for tk in tks]
        if task_num in tasks_nums:
            for i in range(len(self.tasks))
                for tk in self.tasks[i]:
                    if int(tk.split(' ')[0]) is task_num:
                        area_index = i
                        area = area_names[area_index]
                        task = tk
            choice = raw_input('Remove task %s from area %s?' % (task, area))
            if choice is 'y':
                self.tasks[area_index].remove(task)
            elif choice is 'n':
                print('Never mind.')
            else:
                print('Sorry, did not recognize')
        else:
            raise TaskDoesNotExistError(task_num)
        store_data()

    def mov_task(self, task_num, ):
        """
        function docstring
        Move task
        """
        store_data()

# Definition of errors
class Error(Exception):
    pass

class AreaOutOfSpaceError(Error):
    def __init__(self, area):
        self.area = area

class TaskDoesNotExistError(Error):
    def __init__(self, num):
        self.num = num

