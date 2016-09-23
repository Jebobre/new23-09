__author__ = 'student'
#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while not wall_is_on_the_right():
        if not wall_is_above():
            move_up()
            fill_cell()
            move_down()
            move_right()
            if not wall_is_beneath():
                move_down()
                fill_cell()
                move_up()
                move_right()
        elif not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()
            move_right()
        else:
            move_right()
    if not wall_is_above():
        move_up()
        fill_cell()
        move_down()
    elif not wall_is_beneath():
        move_down()
        fill_cell()
        move_up()


if __name__ == '__main__':
    run_tasks()
