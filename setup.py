# Setup for Words package
#
# [description]:
# create the word sorting directories for sorting words by n1 and n2 indexes
#

import os

alpha = "abcdefghijklmnopqrstuvwxyz"

current_dir = os.getcwd()

first_path = f"{current_dir}\\words"

os.mkdir(f"{current_dir}\\words")

for char in alpha:

    subdir = f"{first_path}\\{char}"

    os.mkdir(subdir)

    for second in alpha:

        filename = f"{subdir}\\{char}{second}"

        with open(filename, "w") as wfile:
            wfile.close()
