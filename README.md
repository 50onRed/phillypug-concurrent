#50onRed Philly PUG

This repository contains the code examples from the January 2013 Philadelphia
Python User Group meetup talk on concurrent Python programming.

###Running the examples
The examples were all written for Python 2.7. You will need to make some small
edits for some of them to work properly. Included in the repo is a
requirements.txt file that can be used with pip. I recommend using
[virtualenv](http://pypi.python.org/pypi/virtualenv) and once you have your
virtual environment setup and activated you can run
pip install -r requirements.txt to install all the dependencies.

####Changes for examples in cpu_bound folder
These examples will read gzipped files line by line from a folder on your local
machine. You will need to change the path given to the glob method to a path
on your local machine that has some gzipped files. It defaults to the 
cpu_bound folder.


####Examples in simple folder
 * blocking_io.py uses the standard python socket module to get a list of host
 ip addresses by hostname.
 *non_blocking_io.py uses gevent to monkey patch the standard python modules
 and uses non-blocking io to resolve the hostnames.


####Examples in io_bound folder
These examples utilize the [instagram api](http://instagram.com/developer/)
to request a list of popular image urls. The examples then download the images
from the urls and write them to disc. Each example writes the images to a different
subfolder. **Please note:** I left an instram api client id in the code so please be kind and
don't abuse it. It was created specifically for this talk, but still be nice. If you want to
use the code in the examples for anything else you need to create a new client id.

 * phillpug.py uses no concurrency and downloads each image sequential
 * phillypug_async.py uses gevent to asynchrounously download the images
 * phillypug_asyc_requests.py is the same as the previous example, but uses
 the requests module instead of urllib
 * phillypug_multi.py a truly concurrent example that uses the python
 multiprocessing module to spawn subprocesses to concurrently download the
 images
 * phillypug_threading.py uses the python threading module to download the
   images.
 * clean.sh a script to clean up the downloaded images from the subfolders


####Examples in the cpu_bound folder (you will need to edit these)
These examples count the number of lines in plain text gzipped files within
a folder. You will need to edit this files with and provide a path to gzipped plain text files.

 * gzip_sequential.py nothing fancy just counts the lines in all the files using no concurrency.
 * gzip_gevent.py uses gevent. Gevent does not monkey patch file i/o so this exmaples should run just about as fast
 as the previous one.
 * gzip_threading.py uses the python threading module. Demonstrates that because of the GIL, using the threading
 module for CPU bound tasks can actually be slower than using no threading.
 * gzip_multiprocessing.py uses the python multiprocessing module to concurrently process the files.


