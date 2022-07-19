import os, sys, platform, random

os = platform.system()

# download the database and store it in the temp/AblePm/db folder
os.system("python updatedb.py")

# by default, if no argument is passed, the program will just tell you to do -h to see the help menu
if len(sys.argv) == 1:
    print("See the help menu by typing -h")

# if the user provides -h, then the help menu will be displayed
if sys.argv[1] == "-h":
    print("""
    Usage:
    python3 main.py [option]
    
    Options:
    
    For packages:
        -i [package name] to install a package
        -u [package name] to update a package
        -r [package name] to remove a package
        -l to list all installed packages
    
    For databases:
        -u to update the database
    
    For help:
        -h to display this help menu
    """)

# if the user provides -i without a package name, then the program will tell you to provide a package name
if sys.argv[1] == "-i" and len(sys.argv) == 2:
    print("Please provide a package name")

# if the user provides -i with a package name, then the program will get the install.py file from the database and run it
if sys.argv[1] == "-i" and len(sys.argv) == 3:
    # update the database
    os.system("python3 updatedb.py")
    # get the /[package name]/install.py file from the database
    os.system("python3 ./temp/AblePm/db/" + sys.argv[2] + "/install.py")


# if the user provides -u without a package name, then the program will tell you to provide a package name
if sys.argv[1] == "-u" and len(sys.argv) == 2:
    print("Please provide a package name")

# if the user provides -u with a package name, then the program will uninstall the package, update the database, and then install the package again
if sys.argv[1] == "-u" and len(sys.argv) == 3:
    # uninstall the package
    os.system("python3 remove.py " + sys.argv[2])
    # update the database
    os.system("python3 updatedb.py")
    # install the package
    os.system("python3 install.py " + sys.argv[2])

# if the user provides -r without a package name, then the program will tell you to provide a package name
if sys.argv[1] == "-r" and len(sys.argv) == 2:
    print("Please provide a package name")

# if the user provides -r with a package name, then the program will uninstall the package and update the database
if sys.argv[1] == "-r" and len(sys.argv) == 3:
    # uninstall the package
    os.system("python3 remove.py " + sys.argv[2])
    # update the database
    os.system("python3 updatedb.py")

# if the user provides -l, then the program will list all installed packages
if sys.argv[1] == "-l":
    # get the list of installed packages
    os.system("python3 list.py")
