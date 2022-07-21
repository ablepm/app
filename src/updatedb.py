import random, os, platform

# if it is the first time calling it, make a installed_packages.txt file
if not os.path.isfile("installed_packages.txt"):
    with open("installed_packages.txt", "w") as f:
        f.write("")

# random number
rnd = random.randint(0, 100)

# if, in the temporary directory, "/AblePm/db" does not exist, then make it
if not os.path.exists(os.path.join(os.getenv("TEMP"), "AblePm", "db")):
    os.makedirs(os.path.join(os.getenv("TEMP"), "AblePm", "db"))

# go to /temp/AblePm/db (or /var/tmp/AblePm/db)
os.chdir(os.path.join(os.getenv("TEMP"), "AblePm", "db"))

# clear the contents of the directory
for file in os.listdir():
    os.remove(file)

# download the database from github
os.system("git clone https://github.com/ablepm/db .")

# delete the readme.md file if it exists
if os.path.exists("readme.md"):
    os.remove("readme.md")

with open("installed_packages.txt", "r") as f:
    installed_packages = f.read()
    installed_packages = installed_packages.split("\n")
    installed_packages = list(filter(None, installed_packages))

# AblePM database is updated