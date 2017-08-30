from shutil import copyfile

import os
import stat
import urllib.request


class Setup:


    def __init__(self):
        self.devkitPath = os.path.expanduser("~")+"/.devkit";
        self.binaryPath = "/usr/local/bin/devkit";


    def run(self):
        print("Installing the devkit...");
        # copy the installer to the local binary folder
        copyfile('./installer.py', self.binaryPath);
        # get current permissions of the devkit
        st = os.stat(self.binaryPath)
        # change permission to executable
        os.chmod(self.binaryPath, st.st_mode | stat.S_IEXEC)

        if not os.path.exists(self.devkitPath):
            print("Creating the devkit folder...");
            os.makedirs(self.devkitPath);


        print("Moving the ruleset to the devkit folder...");
        copyfile('./codesniffer/ruleset.xml', self.devkitPath+"/ruleset.xml");

        print("Downloading the phpcs.phar and moving it to the devkit folder...");
        urllib.request.urlretrieve("https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar", self.devkitPath+"/phpcs.phar")

        print("");
        print("Installation complete!");


setup = Setup();
setup.run();
