#  A docker container with https://github.com/zopefoundation/groktoolkit installed

## The `gserver` container source
The container source is available in https://github.com/prsephton/grokserver/gserver

This directory contains the essential source for the gserver container.  The provided `Dockerfile` may be used to build the 
container, using `docker build <tagname> .`

Part of the build process downloads and runs `zc.buildout` which downloads and installs `grok`, and produces a working
`grok` server environment.

The resulting container may be run with
`docker run --rm --name gserver -p 8080:8080 <tagname> deploy`
and one may then connect one's browser to localhost:8080.

To connect to the admin interface, use a *blank* username and password.  Then in the entry box, type "sample" and click on "create".
The installed sample application can be reached through the provided navigation link.

Of course, the sample application does not provide a persistent storage, and any installed applications disappear every time
the container is restarted.

##  Persistent storage
At a minimum, the internal container folders 
```
	/opt/gserver/var and
	/opt/gserver/parts
``` 
must be mapped to a persistent docker storage or mounted volume, if your application requires persistence between restarts.

##  Development, using gserver as a base
Please see https://github.com/prsephton/grokserver

