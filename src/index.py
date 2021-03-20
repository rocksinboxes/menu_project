
from sys import argv
from subprocess import run
import file_download


class main_menu:

    Title = "Main menu:"
    opt1 = ("1: Install Nodejs")
    
        


main = main_menu()
run("clear")
print(main_menu.Title)
print (main_menu.opt1)

def menu_input():
    menu_input= input("Enter Your Choice:")
    while menu_input !="q":
        if menu_input == '1':
            nodejs = file_download.download_file("https://deb.nodesource.com/setup_15.x")
            nodejs.download_installer()
            run(["clear"])
        print(main_menu.Title)
        print (main_menu.opt1)
        menu_input= input("Enter Your Choice:")
        run(["clear"])
menu_input()