def install_required_packages():
        file = open("/home/pi/menu_project/requirements.txt", "r")
        for line in file:
            print(line)
        file.close()

install_required_packages()