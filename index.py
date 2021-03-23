
from sys import argv, exit
import os
import locale
import packages
locale.setlocale(locale.LC_ALL, '')


nodejs = packages.nodejs()

try:

    len(argv[2]) == 0

except:
    exit("You didn't enter any parameters")

try:
    if argv[1] == "update" or argv[1] == "install":
        for val in argv[2:]:
            function = f"{val}.{val}_{argv[1]}()"
            eval(function)
except:
    exit("Invalid Entry. Please Try again")
