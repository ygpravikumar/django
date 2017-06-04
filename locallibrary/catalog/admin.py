from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


class BookInline(admin.TabularInline):
    model = Book

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
admin.site.register(Book, BookAdmin)

class GenreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Genre, GenreAdmin)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
admin.site.register(BookInstance, BookInstanceAdmin)

admin.site.register(Language)
