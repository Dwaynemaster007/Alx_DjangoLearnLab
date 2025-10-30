# 🐍 ALX Django LearnLab - Introduction to Web Development

A comprehensive introduction to Django web framework covering project setup, models, database operations with ORM, and admin interface customization. Build robust web applications with Python's most powerful framework.

[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![ORM](https://img.shields.io/badge/Django_ORM-Database-092E20?style=for-the-badge)](https://docs.djangoproject.com/en/stable/topics/db/)

<div align="center">

### 🌟 From Zero to Django Hero - Master Web Development 🌟

*Build powerful web applications with Python's premier framework*

[Features](#-key-features) • [Quick Start](#-quick-start) • [Models](#-django-models) • [Admin](#-django-admin-interface)

</div>

---

## 📋 Project Overview

This project is part of the **ALX Back-End Web Development** curriculum, designed to teach Django fundamentals through hands-on practice. You'll build a **Library Management System**, learning essential concepts like models, ORM, CRUD operations, and admin interface customization.

### 🎯 Why Django?

Django powers some of the world's most popular websites:
- 📷 **Instagram** - Photo sharing platform
- 📰 **The Washington Post** - News website
- 🎵 **Spotify** - Music streaming
- 📺 **YouTube** - Video platform features
- 🛒 **Mozilla** - Firefox support site

**Django Philosophy:**
- ⚡ **Rapid Development** - Build faster with less code
- 🔒 **Security First** - Built-in protection against common attacks
- 🎯 **DRY Principle** - Don't Repeat Yourself
- 📚 **Batteries Included** - Everything you need out of the box

---

## 🌟 Key Features

### 🚀 Project Setup
- **Django Installation** - Modern Python web framework
- **Project Structure** - Well-organized file hierarchy
- **Development Server** - Hot reload for fast development
- **Settings Management** - Configuration best practices

### 📊 Database Models
- **ORM (Object-Relational Mapping)** - Python classes to database tables
- **Model Fields** - CharField, IntegerField, and more
- **Migrations** - Version control for database schema
- **Relationships** - Foreign keys and many-to-many

### 🔧 CRUD Operations
- **Create** - Add new records to database
- **Read** - Query and retrieve data
- **Update** - Modify existing records
- **Delete** - Remove data from database

### 👑 Admin Interface
- **Auto-Generated Admin** - Instant data management
- **Customization** - List display, filters, search
- **User Authentication** - Secure admin access
- **Data Visualization** - Clean, intuitive interface

---

## 📁 Project Structure

```
Alx_DjangoLearnLab/
└── Introduction_to_Django/
    └── LibraryProject/
        ├── LibraryProject/           # Project configuration
        │   ├── __init__.py
        │   ├── settings.py           # Project settings
        │   ├── urls.py               # URL routing
        │   ├── asgi.py               # ASGI config
        │   └── wsgi.py               # WSGI config
        ├── bookshelf/                # Django app
        │   ├── migrations/           # Database migrations
        │   │   └── __init__.py
        │   ├── __init__.py
        │   ├── admin.py              # Admin configuration
        │   ├── apps.py               # App configuration
        │   ├── models.py             # Database models
        │   ├── tests.py              # Test cases
        │   └── views.py              # View functions
        ├── db.sqlite3                # SQLite database
        ├── manage.py                 # Django management script
        ├── README.md                 # Project documentation
        ├── create.md                 # Create operation docs
        ├── retrieve.md               # Retrieve operation docs
        ├── update.md                 # Update operation docs
        └── delete.md                 # Delete operation docs
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+** installed
- **pip** package manager
- Basic Python knowledge
- Command line familiarity

### Installation & Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Dwaynemaster007/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/Introduction_to_Django

# 2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3️⃣ Install Django
pip install django

# 4️⃣ Navigate to project
cd LibraryProject

# 5️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

# 6️⃣ Create superuser (for admin access)
python manage.py createsuperuser

# 7️⃣ Start development server
python manage.py runserver
```

### Access the Application

**Development Server:**
```
http://127.0.0.1:8000/
```

**Admin Interface:**
```
http://127.0.0.1:8000/admin/
```

---

## 📚 Task Breakdown

### Task 0: Django Development Environment Setup 🛠️

**Objective:** Set up Django and create your first project.

#### Step 1: Install Django

```bash
# Ensure Python is installed
python --version

# Install Django
pip install django

# Verify installation
python -m django --version
```

#### Step 2: Create Django Project

```bash
# Create project
django-admin startproject LibraryProject

# Navigate to project
cd LibraryProject

# Create README
touch README.md  # Linux/Mac
# type nul > README.md  # Windows
```

#### Step 3: Run Development Server

```bash
# Start server
python manage.py runserver

# Server runs on http://127.0.0.1:8000/
# You should see Django's welcome page! 🎉
```

#### Step 4: Explore Project Structure

**Key Files:**

**`settings.py`** - Project configuration
```python
# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**`urls.py`** - URL routing
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

**`manage.py`** - Management commands
```bash
# Common commands
python manage.py runserver    # Start server
python manage.py makemigrations  # Create migrations
python manage.py migrate      # Apply migrations
python manage.py shell        # Django shell
python manage.py createsuperuser  # Create admin
```

**What You Learned:**
✅ Django installation process  
✅ Project creation with django-admin  
✅ Development server operation  
✅ Project structure and key files  
✅ Django's "batteries included" philosophy

---

### Task 1: Implementing Django Models 📊

**Objective:** Create a Django app with models and perform CRUD operations.

#### Step 1: Create the bookshelf App

```bash
# Create app
python manage.py startapp bookshelf
```

**Register app in `settings.py`:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # Add this line
]
```

#### Step 2: Define the Book Model

**File:** `bookshelf/models.py`

```python
from django.db import models

class Book(models.Model):
    """
    Model representing a book in the library.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
```

**Model Fields Explained:**
- **CharField** - Text field with max length
- **IntegerField** - Stores integers
- **__str__** - String representation of object
- **Meta class** - Model metadata (ordering, verbose names)

#### Step 3: Create and Apply Migrations

```bash
# Create migration files
python manage.py makemigrations bookshelf

# Output:
# Migrations for 'bookshelf':
#   bookshelf/migrations/0001_initial.py
#     - Create model Book

# Apply migrations to database
python manage.py migrate

# Output:
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions, bookshelf
# Running migrations:
#   Applying bookshelf.0001_initial... OK
```

**What Migrations Do:**
- Create database tables
- Modify existing tables
- Version control for database schema
- Keep database in sync with models

#### Step 4: CRUD Operations via Django Shell

**Open Django Shell:**
```bash
python manage.py shell
```

##### 🔹 CREATE Operation

**File:** `create.md`

```python
# Import the Book model
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Output:
# <Book: 1984 by George Orwell>

# Alternative creation method
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

**Documentation:**
```markdown
# Create Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
```

## Output:
```
<Book: 1984 by George Orwell>
```

## Explanation:
Successfully created a Book instance with title "1984", author "George Orwell", and publication year 1949. The book is automatically saved to the database.
```

##### 🔹 RETRIEVE Operation

**File:** `retrieve.md`

```python
# Retrieve all books
all_books = Book.objects.all()
print(all_books)
# Output: <QuerySet [<Book: 1984 by George Orwell>]>

# Retrieve specific book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.publication_year}")

# Output:
# Title: 1984
# Author: George Orwell
# Year: 1949

# Retrieve using filter
books = Book.objects.filter(author="George Orwell")
```

**Documentation:**
```markdown
# Retrieve Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
```

## Output:
```
Title: 1984, Author: George Orwell, Year: 1949
```

## Explanation:
Successfully retrieved the book with title "1984". All attributes (title, author, publication_year) are displayed correctly.
```

##### 🔹 UPDATE Operation

**File:** `update.md`

```python
# Get the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)
# Output: Nineteen Eighty-Four

# Alternative update method
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
```

**Documentation:**
```markdown
# Update Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
```

## Output:
```
Nineteen Eighty-Four
```

## Explanation:
Successfully updated the book's title from "1984" to "Nineteen Eighty-Four". Changes are persisted to the database using save().
```

##### 🔹 DELETE Operation

**File:** `delete.md`

```python
# Get the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Verify deletion
all_books = Book.objects.all()
print(all_books)
# Output: <QuerySet []>

# Alternative deletion method
Book.objects.filter(title="Nineteen Eighty-Four").delete()
```

**Documentation:**
```markdown
# Delete Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
all_books = Book.objects.all()
print(all_books)
```

## Output:
```
(1, {'bookshelf.Book': 1})
<QuerySet []>
```

## Explanation:
Successfully deleted the book from the database. The delete() method returns a tuple with the count of deleted objects. Subsequent query shows an empty QuerySet, confirming deletion.
```

**What You Learned:**
✅ Django app creation  
✅ Model definition with fields  
✅ Database migrations  
✅ CRUD operations with ORM  
✅ Django shell for testing  
✅ QuerySets and model methods

---

### Task 2: Django Admin Interface 👑

**Objective:** Register models and customize the admin interface.

#### Step 1: Register Book Model

**File:** `bookshelf/admin.py`

```python
from django.contrib import admin
from .models import Book

# Simple registration
# admin.site.register(Book)

# Custom admin class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Book model.
    """
    # Fields to display in list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters in sidebar
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')
    
    # Fields to display when editing
    fields = ('title', 'author', 'publication_year')
    
    # Number of items per page
    list_per_page = 20
```

**Admin Features:**

**1. List Display**
```python
list_display = ('title', 'author', 'publication_year')
# Shows these columns in admin list view
```

**2. List Filters**
```python
list_filter = ('author', 'publication_year')
# Adds filter sidebar for easy filtering
```

**3. Search Fields**
```python
search_fields = ('title', 'author')
# Adds search box to find books quickly
```

**4. Ordering**
```python
ordering = ['-publication_year']  # Newest first
# ordering = ['title']  # Alphabetical
```

**5. Date Hierarchy**
```python
# For DateField/DateTimeField
date_hierarchy = 'publication_date'
```

#### Step 2: Create Superuser

```bash
# Create admin account
python manage.py createsuperuser

# Enter details:
# Username: admin
# Email: admin@example.com
# Password: ********
# Password (again): ********

# Output:
# Superuser created successfully.
```

#### Step 3: Access Admin Interface

**URL:** `http://127.0.0.1:8000/admin/`

**Login** with your superuser credentials.

**Admin Features:**
- ✅ Add new books
- ✅ Edit existing books
- ✅ Delete books
- ✅ Search and filter
- ✅ Bulk actions
- ✅ Change history
- ✅ User management

**What You Learned:**
✅ Admin interface registration  
✅ Custom admin class creation  
✅ List display customization  
✅ Filters and search configuration  
✅ Superuser creation  
✅ Admin interface navigation

---

## 🎯 Django ORM Cheat Sheet

### Common QuerySet Operations

```python
# Get all objects
Book.objects.all()

# Get specific object
Book.objects.get(id=1)
Book.objects.get(title="1984")

# Filter objects
Book.objects.filter(author="George Orwell")
Book.objects.filter(publication_year__gte=1900)  # Greater than or equal

# Exclude objects
Book.objects.exclude(author="George Orwell")

# Order objects
Book.objects.order_by('title')
Book.objects.order_by('-publication_year')  # Descending

# Limit results
Book.objects.all()[:5]  # First 5

# Count objects
Book.objects.count()

# Check existence
Book.objects.filter(title="1984").exists()

# Create object
Book.objects.create(title="...", author="...", publication_year=...)

# Update objects
Book.objects.filter(author="Old Name").update(author="New Name")

# Delete objects
Book.objects.filter(id=1).delete()
```

### Field Lookups

```python
# Exact match
Book.objects.filter(title__exact="1984")

# Case-insensitive
Book.objects.filter(title__iexact="1984")

# Contains
Book.objects.filter(title__contains="Nineteen")

# Case-insensitive contains
Book.objects.filter(title__icontains="nineteen")

# Starts with
Book.objects.filter(title__startswith="The")

# Ends with
Book.objects.filter(title__endswith="Four")

# Greater than
Book.objects.filter(publication_year__gt=1950)

# Less than or equal
Book.objects.filter(publication_year__lte=2000)

# In list
Book.objects.filter(id__in=[1, 2, 3])

# Range
Book.objects.filter(publication_year__range=(1940, 1950))
```

---

## 🛠️ Available Commands

### Django Management Commands

```bash
# Start development server
python manage.py runserver
python manage.py runserver 8080  # Custom port

# Database operations
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
python manage.py sqlmigrate bookshelf 0001

# Django shell
python manage.py shell
python manage.py shell_plus  # Enhanced shell (requires django-extensions)

# Admin operations
python manage.py createsuperuser
python manage.py changepassword username

# Static files
python manage.py collectstatic

# Testing
python manage.py test
python manage.py test bookshelf

# Database
python manage.py dbshell
python manage.py dumpdata > backup.json
python manage.py loaddata backup.json

# App management
python manage.py startapp appname
```

---

## 📖 Django Concepts Explained

### Models
- Python classes representing database tables
- Each attribute is a database field
- ORM translates Python code to SQL
- Migrations track schema changes

### ORM (Object-Relational Mapping)
- Database abstraction layer
- Write Python instead of SQL
- Database-agnostic code
- QuerySets for lazy evaluation

### Admin Interface
- Auto-generated CRUD interface
- Customizable for any model
- Built-in authentication
- Perfect for content management

### Apps
- Modular components of Django project
- Each app has models, views, URLs
- Reusable across projects
- Follows separation of concerns

---

## 🎓 Learning Outcomes

After completing this project, you can:

### Django Fundamentals
✅ Install and configure Django  
✅ Create Django projects and apps  
✅ Understand project structure  
✅ Run development server

### Database Operations
✅ Define models with various fields  
✅ Create and apply migrations  
✅ Perform CRUD operations  
✅ Use Django ORM effectively  
✅ Query data with filters

### Admin Interface
✅ Register models with admin  
✅ Customize admin display  
✅ Add filters and search  
✅ Create superusers  
✅ Manage data via admin

### Development Skills
✅ Use Django shell for testing  
✅ Debug Django applications  
✅ Follow Django best practices  
✅ Document database operations

---

## 🌍 Real-World Applications

Django is used to build:

### Content Management
- 📰 **News Sites** - The Washington Post, The Guardian
- 📝 **Blogs** - WordPress alternatives
- 📚 **Documentation** - ReadTheDocs

### Social Platforms
- 📷 **Instagram** - Photo sharing
- 🎵 **Spotify** - Music streaming features
- 💬 **Disqus** - Comment system

### E-commerce
- 🛒 **Oscar Commerce** - E-commerce framework
- 💳 **Payment Systems** - Stripe integrations
- 📦 **Inventory Management**

### Enterprise Systems
- 📊 **CRM Systems** - Customer relationship management
- 💼 **ERP Solutions** - Enterprise resource planning
- 📈 **Analytics Platforms** - Data visualization

---

## 🔮 Next Steps

Ready to advance? Here's your learning path:

### Immediate Next Steps
1. **Views and URLs** - Handle HTTP requests
2. **Templates** - HTML rendering with Django
3. **Forms** - User input handling
4. **Static Files** - CSS, JavaScript, images

### Intermediate Topics
5. **Class-Based Views** - Reusable view logic
6. **Authentication** - User login/signup
7. **Relationships** - ForeignKey, ManyToMany
8. **File Uploads** - Handle media files

### Advanced Topics
9. **REST API** - Django REST Framework
10. **Testing** - Unit and integration tests
11. **Deployment** - Production servers
12. **Caching** - Redis, Memcached

---

## 📚 Recommended Resources

### Official Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django ORM](https://docs.djangoproject.com/en/stable/topics/db/)

### Learning Platforms
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Real Python Django](https://realpython.com/tutorials/django/)
- [MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

### Books
- "Django for Beginners" by William S. Vincent
- "Two Scoops of Django" by Daniel Roy Greenfeld
- "Django for APIs" by William S. Vincent

### Community
- [Django Forum](https://forum.djangoproject.com/)
- [Django Discord](https://discord.gg/xcRH6mN4fa)
- [r/django](https://www.reddit.com/r/django/)

---

## 🐛 Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
# Kill process on port 8000
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Migration Errors:**
```bash
# Reset migrations (development only!)
python manage.py migrate bookshelf zero
rm bookshelf/migrations/000*.py
python manage.py makemigrations bookshelf
python manage.py migrate
```

**Admin Not Loading:**
```bash
# Ensure app is in INSTALLED_APPS
# settings.py
INSTALLED_APPS = [
    ...
    'bookshelf',
]

# Collect static files
python manage.py collectstatic
```

**Import Errors:**
```bash
# Ensure you're in correct directory
cd LibraryProject

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
```

---

## 📄 License

This project is part of the **ALX Back-End Web Development Curriculum**.

© 2025 ALX Africa. All rights reserved.

---

## 👨‍💻 Author

**Thubelihle Dlamini (Dwaynemaster007)**

---

<div align="center">

### 💜 Built with Django Excellence by [Dwaynemaster007](https://github.com/Dwaynemaster007) 💜

*One Model at a Time, Building the Web* 🐍✨

[![GitHub](https://img.shields.io/badge/GitHub-Dwaynemaster007-181717?style=for-the-badge&logo=github)](https://github.com/Dwaynemaster007)
[![Django](https://img.shields.io/badge/Django-Master-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

---

**Tags:** `django` · `python` · `orm` · `models` · `admin-interface` · `crud-operations` · `web-framework` · `backend` · `database` · `sqlite` · `alx-backend` · `migrations` · `django-shell` · `web-development`

</div>