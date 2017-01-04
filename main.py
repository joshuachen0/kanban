# main module, handles initialization, termination, deletion, loading, and saving 
# of kanbans in infinite while loop with prompt statement

from kanban import kanban
import os

def main():
    in_put = ''
    # Create/load a kanban board
    kb = load_kanban(raw_input('Name of kanban board to create/load: '))
    while in_put.lower() not in ['q', 'quit']:
        in_put = raw_input('Enter your command: ')
        in_put = in_put.split(';')
        #Check if kanban already loaded
        if kb:
            if in_put[0] == 'prt':
                kb.print_display()
            elif in_put[0] == 'lod':
                kb = load_kanban(raw_input('Name of kanban board to load: '))
            elif in_put[0] == 'mov':
                try:
                    task_num = in_put[1]
                    to_area = in_put[2]
                except IndexError:
                    
                    kb.mov_task(task_num, to_area)
            elif in_put[0] == 'add':
                task_name = in_put[1]
                kb.add_task(task_name)
            elif in_put[0] == 'rem':
                task_num = in_put[1]
                kb.rem_task(task_num)
            elif in_put[0] == 'del':

            else:
                pass
        else:
            if in_put[0] == 'del':
                try:
                    kb_name = raw_input('Name of kanban board to delete: ')
                    delete_kanban(kb_name)
                except OSError:
                    with open('error_log.txt', 'a') as f:
                        f.write('The kanban board \'kb.name\' cannot be deleted.')


def create_kanban(kb_name):
    num_of_areas = input('Number of areas in new kanban board: ')
    with open(kb_name, 'w') as f:
        for i in range(num_of_areas):
            area_name = raw_input('Name of area %d: ' % (i + 1))
            area_size = raw_input('Size of area %d: ' % (i + 1))
            f.write('%s|%d||\n' % (area_name, area_size))

def load_kanban(kb_name):
    if not os.path.isfile(kb_name)
        print('A kanban board called %s does not exist.' % kb_name)
        choice = raw_input('Would you like to create one with that name? (y/N) ')
        if choice.lower() in ['y', 'yes', 'ye', 'yea', 'ok', 'yeah']:
            create_kanban(kb_name)
        else:
            return
    return kanban(kb_name)

def delete_kanban(kb_name):
    os.remove(kb_name)
    os.remove(kb_name + '-nice.txt')


if __name__ == '__main__':
    main()

# prt - print display
# cre - create kanban
# lod - load kanban
# mov - move task
# add - add task
# rem - remove task
# del - delete kanban