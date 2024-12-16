# GrokServer
A docker based installation of zopefoundation/grok.

## Installation
Requires docker.

Directly from a git checkout from `https://github.com/prsephton/grokserver`.
```
cd grokserver
make develop
```
You should be prompted for a new principal (manager) user name and password.


## Running the server
After installation, the server will be running with a container name `gserver`.  A persistent environment will be created in a 
new directory (`runtime`), and a copy of the sample source will be available in `runtime/src`.

You can now access the server by pointing your browser at localhost:8080.  This shows an admin interface, where you can
install and navigate to the sample app.

## Developer Documentation
Documentation which describes writing software for the `grok` framework may be [found here](https://grok.readthedocs.io/en/latest/).
For a softer landing [try this](https://www.aptrackers.com/gfn).


## Running your own application
To run your own application, replace the `runtime/src/sample code` with your own, and edit the following files:
	-	runtime/setup.py                  - tailor this to your needs
	-	runtime/buildout.cfg              - wherever it references "sample", make it reference your own code instead
	-	runtime/parts/site.zcml           - replace i18n_domain names with your own, and rename the package
	
That is pretty much it.  run "make buildout" and you are done.
	
## Changing the password
The password is stored in hidden file, readable and writable only by the owner. It lives in `runtime/var/.gpasswd.cfg`.
A new password can be generated with `docker exec -it gserver /opt/gserver/bin/zpasswd` while the container is up.

Alternately, use the provided make rule `make password` or `bin/zpasswd` which do the same thing.

The resulting information may be included in `site.zcml`, or used to alter existing information.

## Building a production container
One may use prsephton/grokserver as the basis for a new container, copying your source into the new container (`/opt/gserver/src`),
overwriting the internal `setup.py` and `buildout.cfg` with your new one, and then mounting 
the `var` and `parts` folders on a persistent docker store.

