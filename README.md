# My Awesome Project

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy my_awesome_project

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment






# MetroPark System

Welcome to the MetroPark system, a payment collection system for urban parking fines.

## User Guide

To use the application as a user, follow these steps:

1. Register for the application. Make sure to enter your ID number. It doesn't have to be your real ID number, but it must consist of exactly 9 digits.

2. After completing the registration and logging into the system, you will see a dashboard (`home.html`) displaying the details of fines associated with your ID number:

   - Fine number
   - ID number of the fine holder
   - Fine status (Open/Close)
   - Reason description
   - Fine amount

   Under each fine record, you can view the payment history, including:

   - Payment ID
   - Payment Type (Check/Cash/Credit)
   - Payment Amount
   - Date

3. If the fine status is "Open," you will have an available link. Clicking on the link will redirect you to the `payment.html` page, where you need to enter two fields:

   - Payment Type: Check, Credit Card, or Cash.
   - Payment Amount (in אגורות).

4. After completing the payment process, if the amount you entered does not exceed the maximum allowed payment for that fine (taking into account all previous payments you made), you will be redirected to the `success.html` page.

   On the `success.html` page, a link back to the dashboard will be provided, allowing you to view all the comprehensive data about your fines, their updated status, and the payments you made for each report.

## Running the Project Locally

To run the project on your personal computer, follow these steps:

1. Download all files from the `master` branch.

2. Contact the repository administrator to request the project keys: [tzurjob09@gmail.com](mailto:tzurjob09@gmail.com).

   Note: Django requires access to these keys for the project to run. Place the provided `.envs/` folder in the root of the project.

3. Create a virtual environment:

   - Run the command: `$ virtualenv venv`.
   - Activate the virtual environment: `$ source venv/bin/activate`.

4. The following instructions require you to use Docker:

   - Build the Docker image by running the following command in your terminal:
     ```
     $ docker-compose -f local.yml build
     ```

   - Create a container based on the image you just built:
     ```
     $ docker-compose -f local.yml up
     ```

5. Access the application by opening the following link in your web browser: [http://0.0.0.0:8000/](http://0.0.0.0:8000/)

   Now you can start using the application!

## Important Note

In this project, I used `cookiecutter-django` to create a project template. To gain a better understanding of how to navigate within the project, you can refer to the documentation of `cookiecutter-django`: [https://cookiecutter-django.readthedocs.io/en/latest](https://cookiecutter-django.readthedocs.io/en/latest).

## Executing Commands

To execute commands, use the following format: `$ python manage.py ...`

Whenever you want to perform one of the following commands:

```
$ python manage.py + (createsuperuser, makemigrations, migrate, startapp)
```

Write it in the terminal as follows:

```
$ docker-compose -f local.yml run --rm django + (createsuperuser, makemigrations, migrate, ...)
```

## Project Files

The core files of the project are located in the following

 directories:

- Most of the code and logic can be found in the `fines` directory:
  ```
  my_awesome_project/fines/
  ```

- All the models that define the database tables used in the project are located in:
  ```
  my_awesome_project/fines/models.py
  ```

- The forms created for handling payments are written in:
  ```
  my_awesome_project/fines/forms.py
  ```

- All the URL routes used in the project are defined in:
  ```
  config/urls.py
  ```

  Example routes:

  ```python
  path("", DashboardView.as_view(), name="home"),
  path("pay/<int:pk>/", PaymentView.as_view(), name="pay"),
  path("payment-complete/", TemplateView.as_view(template_name="pages/success.html"), name="payment-complete"),
  ```

- The logic behind each route is implemented in various views, all located in:
  ```
  my_awesome_project/fines/views.py
  ```

- Additionally, modifications were made to the user application to add the `israeli_id` field. The modification was made in the following file:
  ```
  my_awesome_project/users/views.py
  ```
The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
