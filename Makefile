##------------------------------------------------------------------------------------------
##   The following rules are available:
##	help     		- This text
##	build     		- Build the container image
##	deploy    		- Deploy (push) the container to docker hub
##	debug			- Run the container in debug mode
##	production		- Run the container in production mode
##	clean			- Remove the runtime (persistent store)
##------------------------------------------------------------------------------------------

help:
	sed -ne '/@sed/!s/^##//p' $(MAKEFILE_LIST)

areyousure:
	@( read -p "Are you sure? [Y/N]: " rsp && case "$$rsp" in [yY]) true;; *) false;; esac )

build:
	bin/build

deploy:
	bin/deploy

debug:
	bin/run debug

production:
	bin/run deploy

clean: runtime areyousure
	rm -rf runtime
