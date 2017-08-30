#!/usr/local/bin/python

import os.path as path

class Installer:

	def __init__(self):
		self.devkitPath = path.expanduser("~")+'/.devkit';


	""" Show all possible options"""
	def run(self):
		print("------------ DEVKIT ------------");

		self.showMenu();

		while 1:
			command = raw_input("Enter a command: ");

			if command == 'q':
				return;
			elif command == 'c':
				print("Starting codesniffer installation...");
				rulesetExists = path.isfile(self.devkitPath+'/ruleset.xml');
				phpcsExists = path.isfile(self.devkitPath+'/phpcs.phar');

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


installer = Installer();
installer.run();