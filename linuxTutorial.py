#!/usr/bin/env python3

import os
import re
#import sys

commands = {"list" : 'ls', 'long-list': 'ls -ltr', 'pwd' : 'pwd', 'change-dir':'cd', 'create-dir': 'mkdir', 'delete': 'rm',
        'display':'cat', 'rename': 'mv', 'copy' : 'cp', 'modify_perm':'chmod'}
commands_learned = []
separator = "\n-------------------------------------------------------------------------\n[testconsole]:$ "
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\x1b[6;30;42m'#92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Navigation:
    def listing(self):
        try:
            print("First command is 'ls'\n")
            ri = input("Type 'ls' " + separator + colors.OKGREEN)
            if ri == commands['list']:
                os.system(ri)
            else:
                print(colors.ENDC+"Please check the command you typed\n")
                raise()
            print(colors.ENDC)
        except:
            print(colors.ENDC + "Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.listing()
            else:
                pass

    def long_listing(self):
        try:
            ri = input("Type 'ls -ltr' " + separator + colors.OKGREEN)
            if ri == commands['long-list']:
                os.system(ri)
                print(colors.ENDC + "\n\nDid you notice, the 'd' in front of the listing? This means they are directories.\nBut in Linux everything is file.\nMore on this in Advanced Linux :) !!!\n")
            else:
                print(colors.ENDC + "Please check the command you typed")
                raise()
        except:
            print(colors.ENDC + "Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break

            if ri.lower() == 'yes':
                self.long_listing()
            else:
                pass
    
    def pwd(self):
        try:
            ri = input("Type 'pwd'" + separator + colors.OKGREEN)
            if ri == commands['pwd']:
                os.system(ri)
                print(colors.ENDC)
            else:
                print(colors.ENDC + "Please check the command you typed")
                raise()
        except:
            print(colors.ENDC+"Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.pwd()
            else:
                pass
    
    def chdir(self):
        try:
            ri = input("Type 'cd' followed by the directory you want to check into! Example 'cd Downloads'"+ separator + colors.OKGREEN)
            search_str = ri
            res = re.search('(cd)\s+(\w*)', search_str)
            if res.group(1) != commands['change-dir']:
                raise
            os.system(ri)
            print(colors.ENDC)
            if res.group(2) == '':
                print(colors.ENDC+"\nHave you been pushed into the root directory!! :)\nCheck if you entered the directory name or not!!\n")
        except:
            print(colors.ENDC+"Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.chdir()
            else:
                pass
    
    def create_dir(self):
        try:
            ri = input("Type 'mkdir' followed by the directory you want to create. ex: 'mkdir foo'"+ separator + colors.OKGREEN)
            search_str = ri
            res = re.search('(mkdir)\s+(\w+)', search_str)
            if res.group(1) != commands['create-dir'] or res.group(2) == '':
                raise
            os.system(ri)
            print(colors.ENDC)
        except:
            print(colors.ENDC + "Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.create_dir()
            else:
                pass

    def remove_file(self):
        try:
            ri = input("Type 'rm' followed by the directory/file you want to delete. Use -r for removing a directory. Example 'rm x.txt' for removing a file. and 'rm -r foo' for removing a directory."+ separator + colors.OKGREEN)
            search_str = ri
            res = re.search('(rm)\s+(\w*)', search_str)
            if res.group(1) != commands['delete']:
                raise
            os.system(ri)
            print(colors.ENDC)
        except:
            print(colors.ENDC+"Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.remove_file()
            else:
                pass

    def all(self):
        self.listing()
        commands_learned.append('ls')
        print("\n\nNow let's check the time of creation of these files, permissions and more...")
        self.long_listing()
        commands_learned.append('ls -ltr')

        print("\n\nCheck your current working directory")
        self.pwd()
        commands_learned.append('pwd')

        print("\n\nYou want to change the directory?")

        self.chdir()
        commands_learned.append('cd')
    
        print("\n\nLet's create a directory!!")
        
        self.create_dir()
        commands_learned.append('mdkir')
        print("\nNow you can use 'cd' command to go into this directory\n")
        self.remove_file()
        commands_learned.append('rm')


class FileManipulations:
    print("Ok, so you learnt how to navigate into the Linux files!!\n")
    print("Let's learn some file manipulations")
    def cat_file(self):
        print("You want to check the content of the file?\n")
        try:
            ri = input("Type 'cat' followed by the filename. Ex: 'cat foo.txt'"+ separator + colors.OKGREEN)
            search_str = ri
            res = re.search('(cat)\s+(\w+)', search_str)
            if res.group(1) != commands['display']:
                print(colors.ENDC+"Wrong command!")
                raise()
            os.system(ri)
            print(colors.ENDC)
        except:
            print(colors.ENDC + "Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.cat_file()
            else:
                pass


    def copy_file(self):
        print("\n\nYou want to edit the file? Use any of the system editor like 'vi' or 'nano' or 'emacs'")
        print("To know the usage of the editors, check the man pages. Ex: man nano or man vi\n")

        print("Let's try to copy one file to another.")
        try:
            ri=input("Type 'cp <source file name> <destination file name>' Ex: cp foo.txt bar.txt"+ separator + colors.OKGREEN)
            search_str = ri
            #res = re.search('(cp)\s+(\W+)\s+(\W+)', search_str)
            #if res.group(1) != commands['copy']:
            #    print(colors.ENDC+"Wrong command!")
            #    raise()
            os.system(ri)
            print(colors.ENDC)
        except:
            print(colors.ENDC + "Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.copy_file()
            else:
                pass

    def rename_file(self):
        print("\n\nLet's try to rename file.")
        try:
            ri=input("Type 'mv <original file name> <new file name>' Ex: mv foo.txt bar.txt"+ separator + colors.OKGREEN)
            search_str = ri
            res = re.search('(mv)\s+(\w+)\s+(\w+)', search_str)
            if res.group(1) != commands['rename']:
                print(colors.ENDC+"Wrong command!")
                raise()
            os.system(ri)
            print(colors.ENDC)
        except:
            print(colors.ENDC + "Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.rename_file()
            else:
                pass

    def change_file_permission(self):
        print("\n\nChange the file permissions")
        print("Please check the man page of 'chmod'. [man chmod]")
        print("Let's change the file permissions and make the file as executable")
        try:
            ri = input("Type 'chmod +x <File name>'. Ex. chmod +x foo.py"+ separator + colors.OKGREEN)
            search_str = ri
            res = re.search('(chmod)\s+', search_str)
            if res.group(1) != commands['modify_perm']:
                print(colors.ENDC+"Wrong command!")
                raise()
            os.system(ri)
            print(colors.ENDC)
        except:
            print(colors.ENDC + "Something went wrong!\n")
            while(1):
                ri=input("If you want to continue exploring last command, press 'Yes' else 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                self.change_file_permission()
            else:
                pass
        try:
            while(1):
                ri = input("You want to check the permission for your file? Press 'Yes' or 'No'\n")
                if not (ri.lower() == 'yes' or ri.lower() == 'no'):
                    print("[%s] You didn't enter Yes or no, Please try again", ri)
                else:
                    break
            if ri.lower() == 'yes':
                n = Navigation()
                n.long_listing()
            else:
                pass
        except:
            print("Oops!!")
            pass


    def all(self):
        self.cat_file()
        commands_learned.append('cat')
        self.copy_file()
        commands_learned.append('copy')
        self.rename_file()
        commands_learned.append('mv')
        self.change_file_permission()
        commands_learned.append('chmod')
#
def main():
    print("===============================================================================\n")
    print("\tThis is very basic hands-on tutorial of Linux.\n")
    print("\tIt will just make you understand initial basic commands.\n")
    print("\tBest way to learn is explore. If you want to explore more about a command\n")
    print("\tsimply use \"man <command name>\". And yes, you have \"man man\" too!!!")
    print("\tHave Fun!!!!\n")
    print("===============================================================================\n")
    print("After you log into your system, open 'Terminal'\n")
    print("Hopefully you will be landed into your 'home' sweet home'\n")
    n = Navigation()
    n.all()
    m = FileManipulations()
    m.all()
    print("Hope you enjoyed and learnt some basics!!")
    print("Just to recap, here is the list of commands you learnt:\n", commands_learned)

if __name__ == "__main__":
    main()

