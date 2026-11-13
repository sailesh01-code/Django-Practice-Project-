
# Django Practice Projects

A collection of small Django projects built while learning Python and Django. Each project explores a different part of web development, from URL routing and templates to forms, models, cookies, and sessions.

## Projects

| Folder | Topics |
| --- | --- |
| `001_WishProject` | Django project and views |
| `002-MultipleApp with Multile view` | Multiple apps and views |
| `003-Application Level URL` | App-level URL routing |
| `004-Create templates in django` | Django templates |
| `005-Student Info` | Student information forms |
| `006-StaticFile` | Static files |
| `007-Models` | Django models |
| `008-Employee Registration Form` | Registration forms |
| `009 - Form + Model` | Forms backed by models |
| `010 - Model Based Form` | Model forms |
| `011 - Minor Project - Task Management System` | Task management |
| `Project 12 - 16 - state management` | Cookie, session, student information, and cart examples |

The project folders are independent examples. Each Django project has its own `manage.py` file inside its folder.

## Run a project

Clone the repository, then move into a folder that contains `manage.py`. For example:

```bash
git clone https://github.com/sailesh01-code/Django-Practice-Project-.git
cd Django-Practice-Project-
cd "001_WishProject/WishProject"
python -m venv .venv
```

Activate the virtual environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS or Linux
source .venv/bin/activate
```

Install Django and run the project:

```bash
python -m pip install Django
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. Install any additional packages needed by the project you choose. There is no repository-wide `requirements.txt` file.

## Learning topics

- Django models, forms, and the ORM
- Views, templates, and URL routing
- Static files
- Registration and CRUD workflows
- Cookies and sessions

## Author

[sailesh01-code](https://github.com/sailesh01-code)
