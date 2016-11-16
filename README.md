# Flask uWsgi NGINX Upstart Template

This is a template for starting any new production-ready flask app, using uwsgi,
served over Nginx, deployed on an Ubuntu server, launched on startup using
upstart.

**Read this entire file, as it contains several instructions for parts of these files that need to be changed and files that need to be moved.**

## Files In This Repository

#### router.py
This is the python application we are deploying.  Feel free to change the name or hide it in a subdirectory; if you do, just modify the import in wsgi.py to properly import the application.

#### wsgi.py
This is the python application that serves as uwsgi's interface to our webapp.  It just needs to contain the flask app, and **it must be called `application`**.  Run this with python (`python wsgi.py`) to test your application using flask's dev server. **Note: the call to `app.run()` has the `host='0.0.0.0'` parameter, meaning the application will be public while testing.** Remove this parameter to only serve to localhost.

#### app.ini
This is the wsgi configuration file.  It is often called *your_project_name*.ini, but this is not necessary.  If you change the name of this file, also modify the reference to it in the upstart configuration.  Modify line 8 of this file to be /path/to/your/project/app.sock. Note that app.sock does not currently exist here.  This line is telling uwsgi where to create the unix socket which will be used to communicate between nginx and uwsgi.

#### PROJECTNAME.conf
This is the upstart configuration.  This is the standard way of actually *running* your application and not having it just be a subprocess of your shell (which will end when you terminate your ssh connection).

Change line 6 to contain the user that owns your application (probably the user you're currently running as). Change line 11 to contain the path to the root directory of this project.  If your `uwsgi` binary is not at `/usr/loca/bin/uwsgi` (you can check by running `which uwsgi`), change that part of line 12.

Next, if you are not yet using a virtualenv, create a virtualenv for this project, and change the path in line 9 to be the path of the bin directory in your virtualenv. Also, make sure to install flask in your virtualenv!

Rename the file to be more descriptive of your project, and `sudo mv` it to /etc/init/.  Run `sudo start PROJECTNAME`, where `PROJECTNAME` is the name of the .conf file, not including the `.conf`.

#### nginx.conf
I'm assuming you already have Nginx running.  If not, do that first.

Change line 3 to contain the server name or IP address at which you'd like to serve this application.  Change line 7 to contain the path to the unix socket you specifed in line 8 of app.ini.

Then add the contents of this file to the end of your nginx installation's config file, and restart Nginx.

### Conclusion
Tada! You should now have a running server, being served by nginx through uwsgi on your ubuntu server.  Also, any time your server restarts, your application will automatically start up.

If you had to make any modifications to anything I said in this document, please let me know by email at chrisshroba@ gmail or by twitter @chrisshroba.

Good luck!