#! /usr/bin/env python3

"""
This module contains a simple function, similar to running hello('world').
Use the module and function by executing the following on the command line, for example:
    $ python3
    >>> import ray_doue
    >>> help(ray_doue)
    or 
    >>> ray_doue.say_hello('<optional string parameter>')
    >>> exit()
"""
# Add an import for fun and learning (not used)
import sys


# Unsure whether to return to None because this is kind of a no-operation function.
def say_hello(name='Reuven Lerner'):
    """This function prints a greeting to the user when provided one input, or prints a greeting to the default user. 
    It then executes some simple print statements with information about US Major League Baseball and cricket in 
    Israel. The function returns None, although this is not likely required.
    Expects: An optional string argument, typically a name.
    Returns: None
    """
    print(f'In honor of Willie Mays (1931 - 2024), Say Hey {name}!')
    print(
        f'And don\'t forget, Dave Parker was inducted into the Major League Baseball Hall of Fame on 27 Jul 2025 along '
        f'with other players including Billy Wagner, CC Sabathia, Dick Allen, and Ichiro Suzuki.')
    print(
        f'Of course, Israel has cricket.  According to the Israel Cricket Association, "The first All Israeli match '
        f'took place in 1956 in Tel-Hashomer, between teams representing Tel Aviv and the Negev desert town Be\'er '
        f'Sheva."')

    return None
