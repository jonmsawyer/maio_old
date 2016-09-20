# Maio: Media All-in-One

Version: development, super-pre-alpha, not-even-ready-for-testing

## Installing Maio

So far, Maio has only been developed and installed on Linux. Official Windows and Mac support will follow.

### Get Django!

`$ sudo pip install Django==1.5.4`

Also see https://www.djangoproject.com/download/

### Get Dependencies!

 * Python-Magic: `$ sudo pip install python-magic` - for mime type calculations
 * Python Imaging Library: `$ sudo pip install pillow` - for image manipulation
 * MySQL-Python: `$ sudo pip install MySQL-python` - for MySQL (if you choose to use it)
 * psycopg2: `$ sudo pip install psycopg2` - for PostgreSQL (if you choose to use it)
 * pysqlite: `$ sudo pip install pysqlite` - for SQLite3 (if you choose to use it)

#### In One Line
 * PostgreSQL: `sudo pip install psycopg2 python-magic pillow`
 * MySQL: `sudo pip install MySQL-python python-magic pillow`
 * SQLite3: `sudo pip install pysqlite python magic pillow`

#### Using PIP's Requirements File (Assumes PostgreSQL)
 * `cd /path/to/maio`
 * `pip install -r scripts/requirements.pip`
   * To use a different database, edit this requirements file and change it to the appropriate database of your choice using the databases listed above.

#### You will also need ####
 * MySQL if you are going to use MySQL
 * PostgreSQL if you are going to use PostgreSQL
 * SQLite3 if you are going to use SQLite3
 * Python 2.6 or newer

### Get the Maio source code!

~~~
$ mkdir /path/to/install
$ cd /path/to/install
$ git clone https://github.com:jonmsawyer/maio.git
~~~

### Set up your database!

 * Using one of `MySQL`, `PostgreSQL`, or `SQLite3`, create your database, user, and password for Maio.
 * Change settings.py:

~~~
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', or 'sqlite3'.
    'NAME': 'maio', # Or path to database file if using sqlite3.
    'USER': 'maio',
    'PASSWORD': 'maio',
    'HOST': 'localhost',
    'PORT': '',
  }
}
~~~

Change the to the database driver, username, and password you have set for yourself. DON'T USE THESE SETTINGS ON A PRODUCTION WEB SERVER!

 * Change the secret key:

~~~
SECRET_KEY = '+&-8p_beejspfe!8#b_q&eiw%zw-^_96^h=3gvt7%_^9m$z+=a'
~~~

Change this to something else. DON'T USE THIS KEY ON A PRODUCTION WEB SERVER!

 * Change the thumbnail path:

~~~
MAIO_SETTINGS = {
  'thumbnail_directory': '/var/maio/thumbnails',
}
~~~

Change this to a path you have read/write access to.

### Sync the database tables!

 * Now run a Django command to create your database structure:

~~~
$ cd /path/to/maio
$ ./manage.py syncdb
~~~

### Get Images! (Audio and Video not supported yet)

 * First create your thumbnail directory (it does not already exist):

~~~
$ mkdir /path/to/maio/thumbnails
~~~

This should be the same directory as you have configured above in your `MAIO_SETTINGS['thumbnail_directory']` setting.

 * Get the images!

~~~
$ cd /path/to/maio
$ cd scripts
$ ./getpics.py /path/to/the/pictures/you/want/to/add/to/maio
~~~

### Run the server!

~~~
$ cd /path/to/maio
$ ./manage.py runserver 8080
~~~

### Run Maio!

In your browser, go to http://localhost:8080/ and enjoy!
