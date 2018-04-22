Python Microservice Sandbox
===========================

# Requirements

## Running
- [Docker](https://www.docker.com)

## Development 
- [Python 3](https://www.python.org/)
- [Virtualenv](http://pypi.python.org/pypi/virtualenv)

Dependencies are installed using [pip](https://pip.pypa.io/en/stable/)

# Run

```
❯ make run
```

This will build the docker image for the project and then will run it locally. After this request [http://localhost:8080](http://localhost:8080)


# Development

Use a virtual environment for python, don't mess up with the system version.

Check that you have `virtualenv` installed. If not install it
```
❯ virtualenv --version 
```

Prepare the virtual environment, this is only needed once after you get the code of the project.
```
❯ virtualenv -p /usr/local/bin/python3 flask-service-env
```

Activate the virtual environment.
```
❯ source flask-service-env/bin/activate
```

Install dependencies for the project
```
❯ pip install -r requirements.txt
```

Run the project
```
❯ python src/app.py
```

# References

- [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs)
