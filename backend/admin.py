from django.contrib import admin
from django.utils.html import format_html

from backend.models import Category, Brand, Author, Student, MarkList, Book


# Registering the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Fields to display in the list view
    search_fields = ('name',)      # Add a search bar to search by category name
    list_filter = ('name',)        # Add filters in the sidebar based on category name

admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'image_tag')

    search_fields = ('id','name')

    def image_tag(self, obj):
        if obj.image_path:
            return format_html('<img src="{}" width="150" height="150" />'.format(obj.image_path.url))
        return "No Image"  # In case there's no image

    image_tag.short_description = 'Image'
admin.site.register(Brand,BrandAdmin)

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
             BookInline,
           ]

admin.site.register(Book)

admin.site.register(Author, AuthorAdmin)

class MarkListInLine(admin.StackedInline):
    model = MarkList
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name']

    inlines = [
        MarkListInLine,
    ]
admin.site.register(MarkList)

admin.site.register(Student, StudentAdmin)