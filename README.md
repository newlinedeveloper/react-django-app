# react-django-app
User Registration application developed by using React js as frontend and Django as Backend
A simple integration between Django API and React App

This project is made up of two main ones:

1. the Django project containing the REST API, along with all the back-end code;
2. the React project, with all Node dependencies, configs, and front-end related stuff.

## Run it locally

In order to run the projects locally, you need to have Node, npm and Python installed on your machine.

### Running the Django project

Make sure you have python3 installed in your machine.

First, let's create the python virtual environment to isolate our projects:

```bash
python3 -m venv virtual
```

Then, activate it:

```bash
source virtual/bin/activate
```

Just then you can clone the project from GitHub. So, `cd` into the venv and run:

```bash
git clone https://github.com/newlinedeveloper/react-django-app.git
```

Now, add the needed Djano dependencies:

```bash
pip install django djangorestframework django-cors-headers
```



### Running the React project

First install node dependecies :

```bash
npm install
```

Then, you just need to run the app via:

```bash
npm run build
```

Great, just need to run the project now. 

```bash
python manage.py runserver
```
