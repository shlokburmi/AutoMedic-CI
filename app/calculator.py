from sys import modules
modules['__main__'].calculate = {'add': lambda a, b: a + b}