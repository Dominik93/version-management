# Version management

Version management is a tool to help release application, bump version and creation of support branches.

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

merge_command - command used in merge branch develop to master, default "merge --strategy-option theirs"

merge_message - commit message added to merge, default "merge changes"

###### PROJECT

customer - name of customer, can be empty, act as prefix for branches and suffix for released version and tags, required

###### MAVEN

client - full path to maven binary, required

deploy_command - customize deploy command, default "deploy"

install_command - customize install command, default "clean install"

###### ENV

system - system under which command will be executed, available: windows, unix, required

###### BRANCH

master - branch name where main released version is, default master

develop - branch name where main and support development is, default develop

support - branch name for 'master' version of support, default support

## Use cases:

### Init customer:
Create empty branches customer/develop and customer/master.

<b>Example:</b>

Run:

    python init_customer.py module

Branches after init customer:

    customer/master           
    customer/develop          

###  Release
Release module from develop to master. After that action version in develop will be increased. Witch number will be increased can by specified in <i>bump-version</i> parameter. 

<b>Example:</b>

Version and tags in branches before release:

    Branch           Versions               Tags
    master           1.0.1                  1.0.0, 1.0.1
    develop          1.0.2-SNAPSHOT

Run:

    python release.py module

Version and tags in branches after release:

    Branch           Versions               Tags
    master           1.0.2                  1.0.0, 1.0.1, 1.0.2
    develop          1.0.3-SNAPSHOT

###  Create support version
Create support version from given version. 

<b>Example:</b>

Version and tags in branches before create support:
    
    Branch           Version                Tags
    master           1.5.0                  1.1.0, 1.2.0, ..., 1.5.0
    develop          1.5.1-SNAPSHOT 

Run:

    python create_support.py module --version=1.5.0

Version and tags in branches after create support:

    Branch           Versions               Tags
    master           1.5.0                  1.1.0, 1.2.0, ..., 1.5.0
    develop          1.5.1-SNAPSHOT
    support_1.5.0    1.5.0.0                1.5.0.0
    develop_1.5.0    1.5.0.1-SNAPSHOT

<br>
<br>

Version and tags in branches before create support:

    Branch           Versions               Tags
    support_1.8.2    1.8.2.4                1.8.2.0, 1.8.2.1, ..., 1.8.2.4
    develop_1.8.2    1.8.2.5-SNAPSHOT

Run:

    python create_support.py module --version=1.8.2.4

Version and tags in branche s after create support:

    Branch                  Versions               Tags
    support_1.8.2           1.8.2.4                1.8.2.0, 1.8.2.1, ..., 1.8.2.4
    develop_1.8.2           1.8.2.5-SNAPSHOT
    support_1.8.2.4         1.8.2.4.0              1.8.2.4.0
    develop_1.8.2.4         1.8.2.4.1-SNAPSHOT


### Release support version
Release support version from branch develop_X.X.X to support_X.X.X. After that action version in develop will be increased.

<b>Example:</b>

Version in branches before release support:

    Branch            Versions               Tags
    support_1.0.5     1.0.5.1                1.0.5.0, 1.0.5.1
    develop_1.0.5     1.0.5.2-SNAPSHOT

Run:

    python release_support.py module --version=1.0.5

Version in branches after release support:

    Branch            Versions               Tags
    support_1.0.5     1.0.5.2                1.0.5.0, 1.0.5.1, 1.0.5.2
    develop_1.0.5     1.0.5.3-SNAPSHOT

### Additional options:

All options are available by running init.py -h or any other script with -h option

  --config-file CONFIG_FILE
                        Configuration file, default config.ini
                        
  --version VERSION     Support version of module, needed only for support versions
  
  --maven-options MAVEN_OPTIONS
                        Options pass to maven, eg. "-DskipTests"
  
  --maven-profiles MAVEN_PROFILES
                        Profiles pass to maven, eg. "-Prelease"
  
  --bump-version {major,minor,incremental}
                        What version number will be bump, only for release
  
  --silent              Silent mode. Never ask user for input
  
  --debug-mode          Debug mode, don`t execute command like git push, mvn clean install
  
  --log-output          Log all executed command and messages into file log.txt


## FAQ:
