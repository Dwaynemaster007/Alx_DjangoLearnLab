from django.shortcuts import render
from .models import Author, Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import UserProfile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import LoginView, LogoutView

def list_books(request):
	books = Book.objects.all()
	return render(request, "relationship_app/list_books.html", {'books': books})

class LibraryDetailView(DetailView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = SignUpForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
	
def is_admin(user):
    profile = getattr(user, 'userprofile', None)
    return profile is not None and profile.role == 'Admin'

def is_librarian(user):
    profile = getattr(user, 'userprofile', None)
    return profile is not None and profile.role == 'Librarian'

def is_member(user):
    profile = getattr(user, 'userprofile', None)
    return profile is not None and profile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author, _ = Author.objects.get_or_create(name=request.POST.get('author', '').strip())
        publication_year = request.POST.get('publication_year') or None

        book = Book(title=title, author=author, publication_year=publication_year)
        book.save()
        return redirect('list_books')  
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author, _ = Author.objects.get_or_create(name=request.POST.get('author', '').strip())
        book.publication_year = request.POST.get('publication_year') or None
        book.save()
        return redirect('list_books')  
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')  

    return render(request, 'relationship_app/delete_book.html', {'book': book})