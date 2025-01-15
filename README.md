# Django Installation Guide

This guide provides step-by-step instructions to set up a Django project, including creating a virtual environment, installing dependencies, and starting a new project.

---

## Prerequisites

Before setting up Django, ensure the following tools are installed on your system:

1. **Python (3.8 or higher)**
   - Download and install Python from [python.org](https://www.python.org/).
2. **Pip** (Python's package installer)
   - Comes pre-installed with Python.
3. **Git**
   - Download and install Git from [git-scm.com](https://git-scm.com/).

---

## Step 1: Create a Virtual Environment

A virtual environment (venv) isolates your Python dependencies for a specific project.

### Commands to Create and Activate a Virtual Environment:

1. **Create the virtual environment**:
   ```bash
   python -m venv env
   ```
   This creates a folder named `env` in your project directory.

2. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source env/bin/activate
     ```

3. **Verify activation**:
   After activation, your terminal prompt will show `(env)` at the beginning.

---

## Step 2: Install Django

Once the virtual environment is active, install Django using pip.

### Command:
```bash
pip install django
```

You can verify the installation by checking the Django version:
```bash
python -m django --version
```

---

## Step 3: Create a Django Project

1. **Start a new Django project**:
   ```bash
   django-admin startproject myproject
   ```
   Replace `myproject` with your desired project name.

2. **Navigate to the project folder**:
   ```bash
   cd myproject
   ```

3. **Run initial migrations**:
   ```bash
   python manage.py migrate
   ```
   This sets up the default database.

4. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000` to see the default Django welcome page.

---

## Step 4: Create a Django App

To create a new app within your project:
```bash
python manage.py startapp myapp
```
Replace `myapp` with the name of your app.

---

## Step 5: Additional Commands

- **Install additional dependencies** (if needed):
  ```bash
  pip install <package_name>
  ```
  Example:
  ```bash
  pip install djangorestframework
  ```

- **Freeze dependencies to a file**:
  ```bash
  pip freeze > requirements.txt
  ```

- **Install dependencies from `requirements.txt`**:
  ```bash
  pip install -r requirements.txt
  ```

- **Run the development server**:
  ```bash
  python manage.py runserver
  ```
  Access the server at `http://127.0.0.1:8000/`.

- **Make migrations for database changes**:
  ```bash
  python manage.py makemigrations
  ```

- **Apply migrations to the database**:
  ```bash
  python manage.py migrate
  ```

- **Create a superuser for admin access**:
  ```bash
  python manage.py createsuperuser
  ```

- **Check for potential issues in the project**:
  ```bash
  python manage.py check
  ```

- **Run tests for the project**:
  ```bash
  python manage.py test
  ```

---

## Deactivating the Virtual Environment

To deactivate the virtual environment, run:
```bash
deactivate
```

---

Congratulations! You have successfully set up Django in a virtual environment. 🎉
