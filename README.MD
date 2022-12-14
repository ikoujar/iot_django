# Introduction

The goal of this project is to provide a minimalistic API for an IoT Company.

The project is written with:
* python 3
* django 4.1
* DRF 3.13

### Main features

* CRUD **Company**
* CRUD **Device**
* Create a **Measurement** for a device
* Docker for easy deployments
* Postgres Database by default


# IOT Company (Django Rest Framework)

![](docs/swagger.png)

# Getting Started

First clone the repository from GitHub and switch to the new directory:
```bash
git clone git@github.com/ikoujar/iot_django.git
cd iot_django
```

## Local setup

### Requirements:
* Python >= 3.9
* Postgres Database
* Pip

### setup
Activate the virtualenv for your project.

```bash
virtualenv env
source env/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file and set your database connection information within `.env`:

```bash
cp .env.example .env
```

Then simply apply the migrations:

```bash
python manage.py migrate
```

You can now run the development server:

```bash
python manage.py runserver 0.0.0.0:8000
```

**[OPTIONAL]** Finally, you can generate sample data using the following command:

```bash
python manage.py db_seed
```

Open http://localhost:8000 with your browser to see the result.

## Docker setup

This setup includes (Django - Postgres - Nginx)

### Requirements:
* Docker engine
* Docker compose

### setup

Create your environment file:

```bash
cp .env.example .env
```

Start the project using docker-compose:

```bash
docker-compose up
```

**[OPTIONAL]** Finally, you can generate sample data using the following command:

```bash
docker-compose exec web python manage.py db_seed
```

Open http://localhost:8000 with your browser to see the result.

Open http://localhost:8000/swagger for APIs list.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

