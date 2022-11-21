# Setup for Words package
#
# [description]:
# create the word sorting directories for sorting words by n1 and n2 indexes
#

import os
import sys
import platform

print(sys.platform, "Detected")



def windows_install():
    alpha = "abcdefghijklmnopqrstuvwxyz"

    current_dir = os.getcwd()

    first_path = f"{current_dir}\\words"

    os.mkdir(f"{current_dir}\\words")

    print("[NEW DIR]", f"{current_dir}\\words")

    for char in alpha:

        subdir = f"{first_path}\\{char}"

        os.mkdir(subdir)

        for second in alpha:

            filename = f"{subdir}\\{char}{second}"

            with open(filename, "w") as wfile:
                wfile.close()
            print("[NEW FILE]", filename)


def linux_install():
    alpha = "abcdefghijklmnopqrstuvwxyz"

    current_dir = os.getcwd()

    first_path = f"{current_dir}/words"

    os.mkdir(f"{current_dir}/words")

    print("[NEW DIR]", f"{current_dir}/words")

    for char in alpha:

        subdir = f"{first_path}/{char}"

        os.mkdir(subdir)

        for second in alpha:

            filename = f"{subdir}/{char}{second}"

            with open(filename, "w") as wfile:
                wfile.close()
            print("[NEW FILE]", filename)





match sys.platform:
    case 'linux':
        linux_install()
    case 'windows':
        windows_install()
    case 'darwin':
        print("MacOS not currently supported")

