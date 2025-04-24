# Django ToDo List App

A simple yet powerful task management application built with Django.

## Features

- ✅ Create, read, update, and delete tasks
- 📝 Mark tasks as complete

## Requirements

- Python 3.12+
- Django 5.2+
- SQLite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/croko22/django_todo.git
   cd django-todo
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment:
   ```bash
   cp .env.example .env
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Load fixture data:
   ```bash
   python manage.py loaddata tasks_fixture.json
   ```

## Running the App

Start development server:
```bash
python manage.py runserver
```

Access the app at: http://localhost:8000