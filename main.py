# main module, handles initialization, termination, deletion, loading, and saving 
# of kanbans in infinite while loop with prompt statement

from kanban import *
import os
import sys
import datetime

def main():
    in_put = ['']
    # Create/load a kanban board
    kb = load_kanban(raw_input('Name of kanban board to create/load: '))
    while in_put[0].lower() not in ['q', 'quit']:
        in_put = (raw_input('>>> ')).split(';')
        # Check if kanban already loaded
        if in_put[0] == 'lod':
            try:
                kb_name = in_put[1]
                kb = load_kanban(kb_name)
            except IndexError:
                kb = load_kanban(raw_input('Name of kanban board to load: '))
            if not kb:
                log_errors('A kanban board with that name does not exist.')
        elif in_put[0] in ['q', 'quit']:
            if raw_input('Are you sure you want to quit? (Y/n) ').lower() in ['n', 'no', 'nah']:
                in_put = ['']
        # Check if kanban already loaded
        elif kb:
            if in_put[0] == 'prt':
                kb.print_display()
            elif in_put[0] == 'mov':
                try:
                    task_num = int(in_put[1])
                    to_area = in_put[2]
                    try:
                        kb.mov_task(task_num, to_area)
                    except AreaDoesNotExistError as e:
                        error = 'The area \'%s\' does not exist.' % e.area
                        log_errors(error)
                    except AreaOutOfSpaceError as e:
                        error = 'The area \'%s\' is out of space.' % e.area
                        log_errors(error)
                    except TaskDoesNotExistError as e:
                        error = 'The task numbered %d does not exist.' % e.num
                        log_errors(error)
                except IndexError:
                    error = 'Not enough arguments for \'mov\' command.'
                    log_errors(error)
            elif in_put[0] == 'add':
                try:
                    task_name = in_put[1]
                    try:
                        kb.add_task(task_name)
                    except AreaOutOfSpaceError as e:
                        error = 'The area \'%s\' is out of space.' % e.area
                        log_errors(error)
                except IndexError:
                    error = 'Not enough arguments for \'add\' command.'
                    log_errors(error)
            elif in_put[0] == 'rem':
                try:
                    task_num = int(in_put[1])
                    try:
                        kb.rem_task(task_num)
                    except TaskDoesNotExistError as e:
                        error = 'The task numbered %d does not exist.' % e.num
                        log_errors(error)
                except IndexError:
                    error = 'Not enough arguments for \'rem\' command.'
                    log_errors(error)
            elif in_put[0] == 'uld':
                kb = None
            elif in_put[0] == 'del':
                error = 'To use \'del\', please unload the kanban board.'
                log_errors(error)
            elif in_put[0] in ['del', 'cre']:
                print('Please unload the kanban board using \'uld\' to use the command \'%s\'.' % in_put[0])
            elif in_put[0] == 'clr':
                kb.clr_board()
            else:
                error = 'Command \'%s\' not recognized.' % in_put[0]
                log_errors(error)
        else:
            if in_put[0] == 'del':
                try:
                    kb_name = in_put[1]
                except IndexError:
                    kb_name = raw_input('Name of kanban board to delete: ')
                try:
                    delete_kanban(kb_name)
                except OSError:
                    error = 'The kanban board \'%s\' does not exist.' % kb_name
                    log_errors(error)
            elif in_put[0] == 'cre':
                try:
                    kb_name = in_put[1]
                except IndexError:
                    kb_name = raw_input('Name of kanban board to create: ')
                if os.path.isfile(kb_name):
                    error = 'A file with this name already exists.'
                    log_errors(error)
                else:
                    create_kanban(kb_name)
                    kb = kanban(kb_name)
            elif in_put[0] in ['prt', 'mov', 'add', 'rem', 'uld', 'clr']:
                print('Please load a kanban board using \'lod\' to use the command \'%s\'.' % in_put[0])
            else:
                error = 'Command \'%s\' not recognized.' % in_put[0]
                log_errors(error)

def log_errors(error):
    print(error)
    with open('error_log.txt', 'a') as f:
        dt = str(datetime.datetime.now())
        f.write(dt + '\t' + error + '\n' )

def create_kanban(kb_name):
    num_of_areas = input('Number of areas in new kanban board: ')
    with open(kb_name, 'w') as f:
        for i in range(num_of_areas):
            area_name = raw_input('Name of area %d: ' % (i + 1))
            area_size = input('Size of area %d: ' % (i + 1))
            f.write('%s|%d||\n' % (area_name, area_size))

def load_kanban(kb_name):
    if not os.path.isfile(kb_name):
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
    sys.exit(0)

# prt - print display
# cre - create kanban
# lod - load kanban
# mov - move task
# add - add task
# rem - remove task
# del - delete kanban
# uld - unload kanban
# clr - clear kanban of all tasks
# lst - LIST ALL KANBANS, check -nice.txt


