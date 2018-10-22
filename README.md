
# Y-Space API

Simple application for an API for some datasets available [here](https://github.com/y-space/y-s-datasets)

The API is available here: http://api.y-space.pw

## Running

Clone the project including the datasets submodule:

    $ git clone --recursive https://github.com/y-space/y-s-api.git

Build the Docker image:

    $ docker build -t y-s-api:latest .

Run the container:

    $ docker run -d --rm -p 7799:7799 y-s-api

