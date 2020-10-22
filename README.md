
<h1 align="center">Gazelle 🦌</h1>


![Test Actions Status](https://github.com/guanes/gazelle-br-cft/workflows/CI/badge.svg)
![Build Image Actions Status](https://github.com/guanes/gazelle-br-cft/workflows/google/badge.svg)

<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="[https://twitter.com/guaneAI](https://twitter.com/guaneAI)" target="_blank">
    <img alt="Twitter: GuaneAI" src="https://img.shields.io/twitter/follow/guaneAI.svg?style=social" />
  </a>
</p>

***

Gazelle is the platform for the cognitive assistant for brokers. It is composed of many microservices built on the hexagonal architecture and Test-driven development (TDD) scheme.

---
<h1 align="left">CFT business rule</h1>


## **Features**

* **FastAPI**: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. ([https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi))
* **Pydantic**: Data validation and settings management using Python type hinting. ([https://github.com/samuelcolvin/pydantic/](https://github.com/samuelcolvin/pydantic/))
* **PostgreSQL**: PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance. ([https://www.postgresql.org/](https://www.postgresql.org/))
* **Tortoise**: Tortoise is an easy-to-use `asyncio` ORM _(Object Relational Mapper)_ inspired by Django. ([https://github.com/tortoise/tortoise-orm](https://github.com/tortoise/tortoise-orm))
* **Docker**: Docker is a container creation technology that allows the creation and use of containers. ([https://www.docker.com/](https://www.docker.com/))
* **Docker-compose**: Compose is a tool for defining and running multi-container Docker applications. ([https://docs.docker.com/compose/](https://docs.docker.com/compose/))
* **Pipenv**: Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. ([https://github.com/pypa/pipenv](https://github.com/pypa/pipenv))
* **Pre-commit**: Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. ([https://pre-commit.com/](https://pre-commit.com/)) 
* **Pytest**: The `pytest` framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. ([https://github.com/pytest-dev/pytest](https://github.com/pytest-dev/pytest))

---
 ## Requirements
 
* Git
* A python 3.8 environment (You can create a virtual environment with python 3.8 using conda `conda create --name=venv_name python=3.8`) 
* Docker
* Docker-compose
* Pipenv (Install with `pip install pipenv`)
* Pre-commit (Install with `pip install pre-commit`)

---
## How to use it

**1.** Enter the new virtual environment with the command `pipenv shell`.

**2.** From the python 3.8 environment, run `pipenv install` .

**3.** Then run `pre-commit install` to install the hooks into the .git file.

**4.** Finally run `docker-compose -f Docker-compose.dev.yml up --build` to run CFT business rule and Postgres containers.

**5.** Go to http://localhost:8051/docs to access the swagger documentation.

---

## Tests 

To run the tests, run `docker-compose -f Docker-compose.dev.yml exec cft python -m pytest`.

To measure the coverage of the tests on the code run this command `docker-compose -f Docker-compose.dev.yml exec cft python -m pytest --cov="."`.

---
## Commit and push

When you do a `git add` . and a `git commit -m "First commit"`, it automatically runs the pre-commit script, which will apply the styles and code formatting defined in Isort, Black and Flake8.
If there are any style or formatting errors, isort, black and flake8 will correct them. 

**Note:** You have to redo the `git add .` and the `git commit -m "First commit"` before you can `push`. 

---

 ## Content 
 
This section explains the project by folder:  

 - **app/:**
	- `api/endpoints/`: Endpoints that the CFT business rule will have.
	- `api/api.py`:  Creation of the router object and inclusion of the endpoint routers.
	- `core/`: This directory contains the engine of CFT business rule.
	- `crud/`: Base interface to connect the crud with any ORM.
	- `infra/`: CRUD and models for each database .
	- `schema/`: Pydantic models.
	- `services/`: This module contains the agnostic implementations of a CRUD for each entity. 
	- `config.py`: Configuration of environmental variables.
	- `db.py`: It contains `register_tortoise function` which sets up Tortoise-ORM on startup and cleans up on teardown.
	- `main.py`: CFT business rule entrypoint.

- **elasticsearch/**:
- **extensions/**:
- **kibana/**:
- **logstash/**:
- **storage/**:
	- It contains any file (csv, excel, .json, etc) that CFT business rule needs.

- **test/**
	- `api/`: Unit tests to the API using pytest.
	- `conftest.py`: Environment variables and general settings for the tests.
- `.flake8`: This is the flake8 configuration file (rules to be ignored, maximum line length, etc).
- `.isort.cfg`: It is the isort configuration file, which organizes the imports (third party libraries, maximum line length, etc).
- `.pre-commit-config.yaml`: This is the configuration file that is executed when the hook is activated by a commit.
- `docker-compose-elk.yml`:
- `Docker-compose.dev.yml`: Docker compose to create the containers from the CFT business rule image, connects it to the database service, in this case postgres.
- `docker-stack-elk.yml`:
- `Dockerfile`: Dockerfile to generate the image of the CFT business rule.
- `entrypoint.sh`: Script to wait for the postgres service to be active.
- `Pipfile`:  Packages and modules needed for CFT business rule to be installed using pipenv.
- `requirements.txt`: Modules required for project execution.
 ---
## File and directory structures

```
.
├── app
│   ├── api
│   │   ├── api.py
│   │   ├── endpoints
│   │   │   ├── cft.py
│   │   │   ├── __init__.py
│   │   │   └── root.py
│   │   └── __init__.py
│   ├── config.py
│   ├── core
│   │   ├── __init__.py
│   │   └── logging.py
│   ├── crud
│   │   ├── base.py
│   │   └── __init__.py
│   ├── db.py
│   ├── infra
│   │   ├── http
│   │   │   ├── get.py
│   │   │   ├── __init__.py
│   │   │   ├── post.py
│   │   │   ├── put.py
│   │   │   └── timeout.py
│   │   └── postgres
│   │       ├── crud
│   │       │   ├── base.py
│   │       │   ├── cft.py
│   │       │   └── __init__.py
│   │       ├── __init__.py
│   │       └── models
│   │           ├── cft.py
│   │           └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── schemas
│   │   ├── cft.py
│   │   └── __init__.py
│   ├── services
│   │   ├── cft.py
│   │   └── __init__.py
│   └── utils
│       └── numeric_values_extractor.py
├── Docker-compose.ci.yml
├── Docker-compose.dev.yml
├── docker-compose-elk.yml
├── Dockerfile
├── Dockerfile.prod
├── docker-stack-elk.yml
├── elasticsearch
│   ├── config
│   │   └── elasticsearch.yml
│   └── Dockerfile
├── entrypoint.sh
├── extensions
│   ├── apm-server
│   │   ├── apm-server-compose.yml
│   │   ├── config
│   │   │   └── apm-server.yml
│   │   ├── Dockerfile
│   │   └── README.md
│   ├── curator
│   │   ├── config
│   │   │   ├── curator.yml
│   │   │   └── delete_log_files_curator.yml
│   │   ├── curator-compose.yml
│   │   ├── Dockerfile
│   │   ├── entrypoint.sh
│   │   └── README.md
│   ├── enterprise-search
│   │   ├── config
│   │   │   └── enterprise-search.yml
│   │   ├── Dockerfile
│   │   ├── enterprise-search-compose.yml
│   │   └── README.md
│   ├── logspout
│   │   ├── build.sh
│   │   ├── Dockerfile
│   │   ├── logspout-compose.yml
│   │   ├── modules.go
│   │   └── README.md
│   └── README.md
├── kibana
│   ├── config
│   │   └── kibana.yml
│   └── Dockerfile
├── locust.py
├── logstash
│   ├── config
│   │   └── logstash.yml
│   ├── Dockerfile
│   └── pipeline
│       └── logstash.conf
├── Pipfile
├── Pipfile.lock
├── pyproject.toml
├── README.md
├── storage
│   └── README.md
├── tests
│   ├── api
│   │   ├── test_cft.py
│   │   └── test_root.py
│   ├── conftest.py
│   └── __init__.py
└── VERSION

31 directories, 74 files
```
 --- 

## Release Notes

### Latest Changes
#### 0.0.7:
* Update input to check carriers from float to string.
* Add asynchronous method to extract the value of the entity.
#### 0.0.6:
* Add files and settings for continuous display (CD) when pushing a new tag. The images are saved in the google cloud registry
* Modified method for obtaining available carriers, now includes carriers exempted from the business rule. 
* Add default values to the creation of carriers for the business rule, the default values are: lower_limit = [1], upper_limit = [1], fee = [0], is_active = False.
* Add develop branch to CI github actions.
#### 0.0.5:
* Add configuration and files needed for continuous integration (CI) with github actions.
#### 0.0.4: 
* Ignore flake88 rule W503.
* Add responses with more informative codes for when something goes wrong with the request.
* Changed the structure of the database template, to allow the entry of lists in the fields of lower_limit, upper_limit and fees in order to allow ranges.
* Fix isort and black configuration to avoid incompatibilities.
#### 0.0.3: 
* Add read me.
* Add validations to endpoint route parameters.
* The schemes are generated when the microservice starts.
#### 0.0.2: 
* Stable version of the seed.
#### 0.0.1: 
* Initial project structure.

---
## Authors
👤 **Arley Berrío Arroyave**
👤 **Daniel Torres González**
👤 **Daniel Santa Rendón**
👤 **Yoana Caro Taborda**
👤 **Hector Mauricio Guerra Londoño**


***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
