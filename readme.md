# DEVKIT

## Intoduction

The devkit is a toolbox which makes it easy to install codesniffer into your projects.   
The kit also alows you to manage your ruleset.xml in one location for all your projects.  

## Getting started

### Setting up the project

**Clone the project**   
It might be a good idea to clone the project in your home directory, in that way you are sure you have the right permissions and the project will be easy to find.   

``` git clone git@bitbucket.org:codedocs/devkit.git ```   


### Changing the phpcs ruleset

There are many different ways to write code, the current ruleset.xml is just an example and contains some basic rules.   
If you want to change the ruleset.xml and use it on multiple systems I would recommend to fork this repository so that you can commit the changes.   

For more information about rulesets: http://pear.php.net/manual/en/package.php.php-codesniffer.annotated-ruleset.php   


### Installing the devkit

**Go into the project folder and run the setup.py**    

``` sudo python3 ./setup.py ```

If everything went right you should see the following:

```
Installing the devkit...
Creating the devkit folder...
Moving the default files to the devkit folder...
Downloading the phpcs.phar and moving it to the devkit folder...

Installation complete!
```

If not please create a ticket with the given error message.


### Using the devkit

**Activating phpcs for a project**

1. use your terminal and navigate to the root directory of the project (the project must be an git repository)
2. when you are in the root of your project execute the following command in your terminal (in the root there must be an .git folder, you can verify this by typing ls -la)

``` devkit ```

After you typed the devkit command you will see a simple menu, to install codesniffer into the current project type ```c``` and press enter.   

Now when you try to commit an .php file which contains code that is in violation with your ruleset, you will see an error.

Thats it!


### Updating the devkit

When a newer version is available you can update the devkit by running the following commands

``` git pull origin master && sudo python3 ./setup.py ```


------------------------------------------

Note: when you want to create a custom ruleset, fork this project!
