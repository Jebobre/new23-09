__author__ = 'student'

#!/usr/bin/python3

from pyrob.api import *


@task
def example1():
    for i in range(9):
        if i==2:
            fill_cell()
        move_right()
        move_down()


if __name__ == '__main__':
    run_tasks()
