
# Configuration:

All configuration is stored in config.init file. Use config.ini.sample and create your own config.ini 

###### GIT

url - url to git

client - full path to git binary

###### PROJECT

customer - name of customer, can be empty, act as suffix for branches and prefix for released version and tags

###### MAVEN

client - full path to maven binary

###### ENV

system - system(windows, unix) under which command will be executed

# Additional options:

All options are available by running python init.py -h


# Usecase:

### Init customer:
Create empty branches customer/develop and customer/master.

<b>Example:</b>

running<br>
python init_customer.pl module<br>
will create customer/master and customer/develop branches<br>

###  Release
Release module from develop to master. After that action version in develop will be increased.

<b>Example:</b>

running<br>
python release.pl module<br>
will release develop into master<br>

###  Create support version
Create support version from given version. 

<b>Example:</b>

running<br>
python create_support.pl module -v 1.20.0<br>
will create customer/develop_1.20.0 and customer/support_1.20.0 from tag 1.20.0-customer

### Release support version
Release support version from branch develop_X.X.X to support_X.X.X. After that action version in develop will be increased.


<b>Example:</b>

running<br>
python release_support.pl module -v 1.20.0<br>
will release customer/develop_1.20.0 into customer/support_1.20.0

# FQA:
