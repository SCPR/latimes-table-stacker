<pre><code>ooooooooooooo            .o8       oooo             .oooooo..o     .                       oooo
8'   888   `8           "888       `888            d8P'    `Y8   .o8                       `888
     888       .oooo.    888oooo.   888   .ooooo.  Y88bo.      .o888oo  .oooo.    .ooooo.   888  oooo   .ooooo.  oooo d8b
     888      `P  )88b   d88' `88b  888  d88' `88b  `"Y8888o.    888   `P  )88b  d88' `"Y8  888 .8P'   d88' `88b `888""8P
     888       .oP"888   888   888  888  888ooo888      `"Y88b   888    .oP"888  888        888888.    888ooo888  888
     888      d8(  888   888   888  888  888    .o oo     .d8P   888 . d8(  888  888   .o8  888 `88b.  888    .o  888
    o888o     `Y888""8o  `Y8bod8P' o888o `Y8bod8P' 8""88888P'    "888" `Y888""8o `Y8bod8P' o888o o888o `Y8bod8P' d888b    </code></pre>


What is this?
=============

Publish spreadsheets as interactive tables. And do it on deadline.


Table of Contents
=================

* [Assumptions](#assumptions)
* [Quickstart To Get Up And Running](#quickstart-to-get-up-and-running)
* [Features](#features)
* [Resources](#resources)
* [Building A Mac OS Python Dev Environment](#building-a-mac-os-python-dev-environment)


Quickstart To Get Up And Running
================================

* Clone this repo to wherever it is on your machine that you work on your projects

        git@github.com:SCPR/latimes-table-stacker.git

* Change into that directory

        cd latimes-table-stacker

* Create your virtualenv and install the project/application requirements using pip

        mkvirtualenv table-stacker
        pip install -r requirements.txt

* Create the project's database

        python manage.py syncdb
        python manage.py migrate

* Let's look at the databases we've already created. Jump back to your terminal window and run the ```build``` command. This instructs our application to bake out a static site using the instructions in settings.py and the table recipes in the yaml directory.

        python manage.py build

* Now let's Launch the static version of the site

        python manage.py buildserver

If everything clicked, you should see your demo site up and running with all the example tables at http://localhost:8000.

The [databases](http://projects.scpr.org/databases/) we've created with this tool include:

* http://projects.scpr.org/databases/2012-2013-kindergarten-immunizations/
* http://projects.scpr.org/databases/2013-2014-kindergarten-immunizations/
* http://projects.scpr.org/databases/2013-2014-lausd-graduation-rates/
* http://projects.scpr.org/databases/2013-api-scores-by-school/
* http://projects.scpr.org/databases/2014-2015-kindergarten-immunizations/
* http://projects.scpr.org/databases/2014-congressional-candidates/
* http://projects.scpr.org/databases/2015-2016-kindergarten-immunizations/
* http://projects.scpr.org/databases/2015-lausd-ag-college-prep/
* http://projects.scpr.org/databases/2015-lausd-budget/
* http://projects.scpr.org/databases/california-motor-carriers/
* http://projects.scpr.org/databases/school-district-dropout-rates/
* http://projects.scpr.org/databases/state-regulated-passenger-carriers/

Now you're ready to make your own using the well-written [table-stacker documentation](http://datadesk.github.com/latimes-table-stacker)

----

Features
========

* Convert a CSV file into an interactive HTML table that sorts, filters and paginates.
* Quickly publish as static files.
* Sync static files with Amazon S3 for instant publishing.
* Instantly syndicate data as CSV, XLS and JSON.
* Post an RSS feed and sitemap that promote the latest data.

----

Resources
=========

* Documentation at [http://datadesk.github.com/latimes-table-stacker](http://datadesk.github.com/latimes-table-stacker)
* Working demonstration at [http://table-stacker.s3-website-us-west-1.amazonaws.com/](http://table-stacker.s3-website-us-west-1.amazonaws.com/)

----

Building A Mac OS Python Dev Environment
========================================

* Assumming [homebrew](https://brew.sh/) is installed...

    * Install homebrew python

            cd /System/Library/Frameworks/Python.framework/Versions
            sudo rm Current
            brew install python
            brew doctor
            which python
            which pip
            pip install --upgrade setuptools
            pip install --upgrade distribute
            pip install virtualenv
            pip install virtualenvwrapper
            python --version
            source /usr/local/bin/virtualenvwrapper.sh
            sudo ln -s /usr/local/Cellar/python/2.7.8_2 /System/Library/Frameworks/Python.framework/Versions/Current

    * Configure $PATH variables for python, virtualenv

            # homebrew path
            export PATH="/usr/local/bin:$PATH"

            # virtualenvwrapper settings
            export WORKON_HOME=$HOME/.virtualenvs
            export PIP_VIRTUALENV_BASE=$WORKON_HOME
            export PIP_RESPECT_VIRTUALENV=true
            source /usr/local/bin/virtualenvwrapper.sh

    * Install MySQL via homebrew

            brew remove mysql
            brew cleanup
            launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist
            rm ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist
            sudo rm -rf /usr/local/var/mysql
            brew install mysql
            ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents

    * Getting mysql up and running

            mysql.server start
            mysql_secure_installation
            mysql -u root -p
            SHOW DATABASES;
            SET default_storage_engine=MYISAM;
