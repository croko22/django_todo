# Django ToDo List App with UV

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
   uv pip install -r pyproject.toml
   ```

4. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. Run migrations:
   ```bash
   uv run python manage.py migrate
   ```

6. Create superuser:
   ```bash
   uv run python manage.py createsuperuser
   ```

## Running the App

Start development server:
```bash
uv run python manage.py runserver
```

Access the app at: http://localhost:8000

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/tasks/` | GET | List all tasks |
| `/tasks/create/` | POST | Create new task |
| `/tasks/<id>/` | PUT | Update task |
| `/tasks/<id>/` | DELETE | Remove task |

## License

MIT License - see [LICENSE](LICENSE) for details
```