# Project Name

> This repository is for the label tool.
## Prerequest

`Python 2.7`, `virtualenv`, `node`

## backend Setup for local testing

``` bash
# initalize virtual env. NOTE: It is NOT a MUST to use virtualenv!!!
virtualenv venv

# activate virtual env
source ./venv/bin/activate

# install python dependencies
pip install -r requirements.txt

# run web server
python run.py

# More issues when run the backend on the server by using virtualenv
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
```

## Front End Setup for local testing

``` bash
# enter the front end sub-directory
cd ./client

# install front-end dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

## Backend Server Setup for deployment on server
``` bash
# go to the home folder of parenting_system then run:
python run.py >logs/log-backend.txt &
```


## tool usage
``` bash
1. set the imagepath in index.py
2. when label, click 'label' for each image and then click 'next'
3. click 'save' after label all the image to save the result
4. the result is in ./server/result/

# Done!
```
