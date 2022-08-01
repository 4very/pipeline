# Pipeline

Pipeline was originally created for use for by [_The Rensselaer Polytechnic_](https://poly.rpi.edu), 
the school newspaper for [Rensselaer Polytechnic Institute](https://www.rpi.edu/) by [Sidney Kochman](https://github.com/kochman) and _The Polytechnic_ team. This repository generalizes and documents a way for other News Organizations to repurpose the site with their own branding. 


Pipeline is [_The Rensselaer Polytechnic_](https://poly.rpi.edu)'s next
website. It will enable rapid development of new article layouts and
interactive features. In the long term, it will provide a solid platform for
our content over the coming decade and support _The Poly_'s focus on
online-first journalism.

# System Requirements
**OS**: Preferred unix-based operating system (Ubuntu, Debian, MacOS...etc).

**RAM**: At least 2GB, preferred 4GB.

**Core**: At least 2 cores, preffered 4 cores.

# Getting Started
The easiest and most straightforward way to host Pipeline is to use docker. The first half of this guide will assume that you have already docker installed, you can find instructions for your operating system [here](https://docs.docker.com/engine/install/).

## Step 0: Installing nessicary programs
This guide isn't going to cover the specifics for each operating system but it will include links where you can learn how to install it on your system. The following programs are assumed to be installed on your device:

- Any kind of terminal program
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - We will use this to get the source code to your system
- [Docker](https://docs.docker.com/engine/install/) - This is what we are going to use to run the programs
- Docker Compose


## Step 1: Clone the git repository
---
Open a terminal window and naviate to the folder in which you want to store the Pipeline source code. Run the following command
```sh
git clone https://github.com/4very/pipeline.git
```
This command will create a subfolder called `Pipeline` in which all of the source code will be.

## Step 2: Populating the .env files
---
The .env file at the root of this folder will hold a majority of your configuration settings for your site. You can view all of the things that you can configure [here](). Keep this file private as it will contain secrets that are meant to protect your site. As a start the following are required for you to run the program:
```sh
# The title of your site
# This will also apear as the header if you do not configure an image url
SITE_TITLE = 

# Auto generated sections
SECTION_NEWS = true
SECTION_FEATURES = true
SECTION_OPINION = true
SECTION_SPORTS = true

# Self configured sections
SECTION_CONTACT = true
SECTION_ABOUT = true
SECTION_SUBMIT = true

# This is the color of the header and various other accent's around the site
COLOR_BRAND = 

COLOR_BACKGROUND = 
COLOR_TEXT_MAIN = 
COLOR_TEXT_SUBMAIN = 

# Admin login, used to create other user accounts
ADMIN_USERNAME = 
ADMIN_EMAIL =
ADMIN_PASSWORD =

```
Note: You can change most of these values later, but you will need to manually add/delete sections if you wish to change them after your first run.

## Step 3: Starting the containers
---
In the root of the project folder run the following command:
```sh
(cd ./docker/prod/ && docker-compose up -d)
```
It is normal for this command to take a while, so go grab yourself some snacks and a drink while it's running. After it's done you should see this inside of the terminal:
<pre style="color:rgb(99,110,187)">
[+] Running 6/6
 ⠿ Network pipeline-prod_django-nginx     Created
 ⠿ Volume "pipeline-prod_django-static"   Created
 ⠿ Volume "pipeline-prod_postgres-data"   Created
 ⠿ Container pipeline-prod-postgres-1     Started
 ⠿ Container pipeline-prod-django-1       Started
 ⠿ Container pipeline-prod-nginx-1        Started
</pre>

You now should be able to connect to your new site with the url [localhost:8000](http://localhost:8000). If that doesn't work you can verify that your containers are up and healthy by running the command:

```sh
docker container ls --format "table {{.ID}}\t{{.Names}}\t{{.Status}}" --filter name="pipeline-prod*"
```
You should see 3 containers that start with `pipeline-prod`. If you see none or less than 3 try running
```sh
$ (cd ./docker/prod/ && docker-compose down)
```
and then run the command above again.

## Step 4: Logging in and editing your site
---
Navigate to [localhost:8000/admin](http://localhost:8000/admin) and log in with the credentials that you put in your `.env` file. Here you can create new articles.

---
## Requirements

Ensure these are installed before continuing.

- [Python 3.7](https://www.python.org) or Python 3.6
- [Pipenv](https://docs.pipenv.org)
- [npm](https://www.npmjs.com/get-npm)
- [Postgres](https://www.postgresql.org)

You can change Pipeline's settings to use SQLite instead of Postgres, but this is not recommended because Pipeline relies on Postgres's full-text search features.

## Getting started

Pipeline is written in Python. It uses Sass and PostCSS on the frontend with webpack to glue them together. For new users working within a virtual machine, it is strongly recommended to use Ubuntu. 

#### Note about Postgres

Pipeline expects to be able to connect to a Postgres database named `pipeline`. To set this up on macOS:

```
brew install postgresql
brew services start postgresql
createdb pipeline
```

To setup Postgres on [Arch Linux](https://www.archlinux.org/):

```
sudo pacman -Syu # Optional, to refresh and update packages
sudo pacman -S postgresql
sudo -u postgres initdb --locale en_US.UTF-8 -D /var/lib/postgres/data
sudo systemctl start postgresql
```

To setup Postgres on [Ubuntu](https://ubuntu.com/):

```
// Install
sudo apt-get update
sudo apt-get -y install postgresql postgresql-contrib
// Setup
sudo -i -u postgres
psql
CREATE USER postgres WITH PASSWORD 'postgres'
\q
*reopen terminal*
sudo -u postgres psql
\password postgres // Enter 'postgres' twice
\q
*reopen terminal*
sudo systemctl start postgresql
```

The default dev database, defined in `settings/dev.py` uses the following postgres url: `postgresql://postgres:postgres@127.0.0.1:5432/pipeline` make sure that your database is configured to these settings. The pipeline database must exist, and the user `postgres` must exist with password `postgres`. Read more about postgres urls [here](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING).

Read about creating a user [here](https://www.postgresql.org/docs/10/role-attributes.html). You will probably want postgres to be a superuser.

### Installing with pipenv

```
git clone https://github.com/thepoly/pipeline.git
cd pipeline
npm install
npx webpack --config webpack.development.config.js
pipenv install --dev
pipenv run python manage.py createcachetable
```

On Ubuntu:
```
git clone git@github.com:thepoly/pipeline.git
cd pipeline
sudo apt install npm
npx webpack --config webpack.development.config.js // Type "yes" when prompted
npm audit fix
sudo apt install pipenv
pipenv install --dev
pipenv run python manage.py createcachetable
```

If you have issues with `pipenv`, you should use `virtualenv`. Installation varies by dev environment.

#### Running with pipenv

```
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If you have issues with the database, ensure that Postgres is running and you have created a database named `pipeline`.

### Installing with virtualenv

```bash
git clone https://github.com/thepoly/pipeline.git
cd pipeline
npm install
npx webpack --config webpack.development.config.js
virtualenv pipeline-env # Enter the virtual environment
source pipeline-env/bin/activate
pip install -r requirements.txt
python manage.py createcachetable
```

#### Running with virtualenv 

```sh
source pipeline-env/bin/activate # If not in the enviroment
python manage.py migrate # run migrations
python manage.py createsuperuser
python manage.py runserver
```

#### Docker

Pipeline can also be run in its production configuration with Docker. It requires three containers: one for running the Django project with gunicorn, another to put nginx in front of it and additionally serve static files, and finally a Postgres container.

```docker-compose up```

Ensure that the `SECRET_KEY` environment variable is set. Additionally, run the following inside of the `django` container (e.g. `docker-compose exec django bash`):

```
python manage.py migrate
python manage.py createsuperuser
```

Pipeline will be available at port 8000 on localhost.

### Standards

Make sure you format your code with [Black](https://github.com/python/black) and use [Flake8](http://flake8.pycqa.org/en/latest/) to find problems.

## Status

Many of the following features are partially complete, but this isn't indicated. Talk to Sid if you need to know where something is right now.

- [ ] Articles
  - [x] Index pages
  - [ ] Article pages
    - [x] Basic layout
    - [ ] Section-specific layouts
    - [x] Editor previews
  - [x] Summaries
  - [x] Kickers
    - [x] Autocomplete
  - [x] Subdecks
  - [ ] Archive pages
  - [ ] WordPress importer
  - [ ] Old site importer
  - [x] Related to authors
- [ ] Photos
  - [x] Uploads
  - [x] Captions
  - [x] Bylines
  - [x] Multiple per article
  - [x] Galleries
- [ ] Syndication
  - [x] RSS feed
  - [x] Sitemap
  - [x] Facebook tags
  - [x] Twitter tags
  - [ ] oEmbed
  - [ ] Apple News
- [ ] Home page
  - [x] Basic article prioritization
  - [ ] Full user control of column layout
- [ ] Staff
  - [x] Index page
  - [ ] Individual pages
    - [x] Authored articles
    - [ ] Bylined photos
  - [x] Positions/terms
  - [x] Staff photos
- [ ] Contact
  - [x] Email addresses on staff pages
- [ ] Users
  - [x] Basic publish permission level
  - [x] Fine grained permissions
  - [ ] G Suite authentication
- [ ] Search
  - [x] Basic headline search
  - [x] Search all fields of articles
  - [ ] Search non-article pages
- [ ] Instrumentation
  - [x] Basic Prometheus metrics
  - [ ] DB metrics
  - [ ] HTTP Basic auth
