# Django REST API – TrimCloud

This project is a minimal URL shortener API built with Django REST Framework. 
It allows users to create shortened links from long URLs and automatically redirects to the original URL when the short link is accessed.

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
