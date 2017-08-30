#!/usr/bin/env python
from shutil import copyfile
import os
import stat

class Installer:

    def __init__(self):
        self.devkitPath = os.path.expanduser("~")+'/.devkit';
        self.currentDir = os.getcwd();


    """ Show all possible options"""
    def run(self):
        print("------------ DEVKIT ------------");

        self.showMenu();

        while 1:
            command = raw_input("Enter a command: ");

            if command == 'q':
                return;
            elif command == 'c':
                self.initCodesniffer();
                return;
            elif command == 'm':
                self.showMenu();
            else:
                print("Command ("+command+") not found!");
                print("");


    """ Show devkit menu"""
    def showMenu(self):
        print("The following options are currently available");
        print("");
        print("(c) Install codesniffer into the current project");
        print("(m) Show the devkit menu");
        print("(q) Exit the devkit");
        print("");


    """ Install codesniffer into the current project"""
    def initCodesniffer(self):
        print("Starting codesniffer installation...");
        rulesetExists = os.path.isfile(self.devkitPath+'/ruleset.xml');
        phpcsExists = os.path.isfile(self.devkitPath+'/phpcs.phar');

        if not rulesetExists:
            print("");
            print("The file 'ruleset.xml' was not found!");
            print("Run the setup.py to solve this problem!")

            return;

        if not phpcsExists:
            print("");
            print("The file 'phpcs.phar' was not found!");
            print("Run the setup.py to solve this problem!")

            return;

        print("");

        if not os.path.exists(self.currentDir+'/.git'):
            print("ERROR: This is not the root folder of an git repository");

            return;

        if not os.path.exists(self.currentDir+'/.git/hooks'):
            print("Creating the hooks directory...");
            os.makedirs(self.currentDir+'/.git/hooks');

        print("Copping files...");
        copyfile(self.devkitPath+'/pre-commit', self.currentDir+'/.git/hooks/pre-commit');
        copyfile(self.devkitPath+'/config', self.currentDir+'/.git/hooks/config');


        print("Making the pre-commit file executable...");
        # get current permissions of the devkit
        st = os.stat(self.currentDir+"/.git/hooks/pre-commit");
        os.chmod(self.currentDir+"/.git/hooks/pre-commit", st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH);

        print("");
        print("Done!");


installer = Installer();
installer.run();