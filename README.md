# Guy's Tribe Terminology Server (prototype)

## Installation

We use ```pipenv``` to setup the environment. See https://pipenv.pypa.io/en/latest/ for instructions to load the libraries required for this project.

First, install pipenv
> pip install --user pipenv
> pipenv install
> source <your working directory>/guy_tribe_term_server/.venv/bin/activate

## To start the server
> uvicorn main:app --reload --port 8000

## To access the terminology service endpoints
Open a browser and access [http://localhost:8000/docs#/](http://tbook.local:8000/docs#/)