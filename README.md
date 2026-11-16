# 🐍 ALX Django LearnLab

Seven Django projects from the **ALX ProDev Backend** programme, from a first `startproject` to a token-authenticated social media REST API.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-A30000?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

## Projects

| # | Project | What I built | Key concepts |
| --- | --- | --- | --- |
| 1 | [Introduction to Django](Introduction_to_Django/) | `LibraryProject` with a `Book` model managed in the admin | Project and app setup, models, migrations, ORM CRUD in the shell, admin customisation |
| 2 | [Django Models](django-models/) | Library system with `Author`, `Book`, `Library`, `Librarian` and `UserProfile` | `ForeignKey`, `ManyToMany` and `OneToOne` relationships, function- and class-based views, login, logout and registration, role-based access (Admin, Librarian, Member) |
| 3 | [Advanced Features & Security](advanced_features_and_security/) | Hardened version of the library app | Custom user model, custom permissions with `permission_required`, groups, CSRF protection, secure headers, HTTPS settings (`SECURE_SSL_REDIRECT`, HSTS) |
| 4 | [API Project](api_project/) | First REST API for books | Django REST Framework serializers, `ModelViewSet`, routers, token authentication (`api-token-auth/`), permissions |
| 5 | [Advanced API Project](advanced-api-project/) | Author and book API with nested serializers | Generic views, custom validation, filtering, `SearchFilter`, `OrderingFilter`, unit tests |
| 6 | [Django Blog](django_blog/) | A full blog site | Authentication and profiles, post CRUD with class-based views, comments, tags (`django-taggit`), search |
| 7 | [Social Media API](social_media_api/) | Social network REST API | Custom user with followers, posts and comments, a personalised feed, likes and notifications, token auth, pagination and search |

## Run a project

Each folder is its own Django project. For example:

```bash
git clone https://github.com/Dwaynemaster007/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install django djangorestframework django-filter django-taggit
python manage.py migrate
python manage.py runserver
```

Use `cd` to switch to whichever project you want. Folders with a nested `LibraryProject/` keep their `manage.py` inside it.

> **Note:** these are learning projects, so the `SECRET_KEY` values in `settings.py` are development keys. Load secrets from environment variables before deploying anything.

## Author

**Thubelihle Dlamini**, [GitHub](https://github.com/Dwaynemaster007) · [LinkedIn](https://linkedin.com/in/thubelihledlamini)
