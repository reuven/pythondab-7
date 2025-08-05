#! /usr/bin/env python3

# Add an import for fun and learning (not used)
import sys


# We have to have at least one Python file.
# Setting return to None because this is kind of a no-operation function.
def say_hello(name='Reuven Lerner'):
    print(f'In honor of Willie Mays (1931 - 2024), Say Hey {name}!')
    print(f'Adding a second print statement to signal a file modification.')
    print(
        f'And don\'t forget, Dave Parker was inducted into the Major League Baseball Hall of Fame on 27 Jul 2025 along '
        f'with others including Billy Wagner, CC Sabathia, Dick Allen, and Ichiro Suzuki.')

    return 'Executed some print statements.'
