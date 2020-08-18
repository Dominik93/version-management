# Version management

Version management is a tool to help release application and bump.

## Getting Started

### Prerequisites

Python, version 3.8.0<br>
Maven, version 3.5.3<br>
Git, version 2.6.1


### Configuration:

All configuration is stored in config.ini file. Use config.ini.sample and create your own config.ini 

###### GIT

url - url to git, required

client - full path to git binary, required

###### MAVEN

client - full path to maven binary, required

###### BRANCH

mainBranch - branch name where main released version is, default master

## Use cases:

###  Release
Release module. Change version of module to given version, add tag and push changes.

### Additional options:

All options are available by running init.py -h or any other script with -h option

  --config-file CONFIG_FILE
                        Configuration file, default config.ini
                        
  --version VERSION     New version of module
    
  --debug-mode          Debug mode, don`t execute command like git push, mvn clean install
  
  --log-output          Log all executed command and messages into file log.txt


## FAQ:
