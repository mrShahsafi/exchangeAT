# Exchanger
this is awesome, everything is going to run automatically.

## HOW TO RUN
only thing which you have to do is run the `run.sh` file with `a right parameter`. the parameter is depends on environment which you are on `Development` | `production` | `testing`.

it, First makes right `docker-compose.yml` config by running below commands:

```bash
./run.sh [options]

	-options are:
		deafult: production
		production
		development
```
this makes right conifg for your environment to run the whole project. 

then, it also runs `docker-compose run --build` command automatically to `build` and `run` all services.

ALSO, each project has a `Dockerfile` which is dependent on `environment` too, the `run.sh` also makes `Right Dockerfile configs` for each project. 


SO to run project in `development mode` just run:
```bash
./run.sh develoment

```

