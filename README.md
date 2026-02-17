# Django REST API – TrimCloud

A Django REST Framework based API project managed with Poetry for dependency management.

This project demonstrates a clean architecture approach using:
- Poetry
- Django
- Django REST Framework
- SQLite (default)
- PyTest
---

## 🚀 Requirements

- Python 3.14.3
- Poetry 2.3.2

---

## 📦 Installation

### 1. Install dependencies

```bash
poetry install
```

### 2. Migrations

```bash
poetry run python manage.py migrate

```

### 3. Optional Create Super User 
_(for /admin)_
```bash
poetry run python manage.py createsuperuser
```

### 4. Runserver local
```bash
poetry run python manage.py runserver
```

### 4. Run Tests
```bash
poetry run pytest --cov=shortener
```
