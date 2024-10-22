from django.contrib import admin

from .models import Category, File, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent' , 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable' , 'parent']
    search_fields = ['title']


class FileInlineAdmin(admin.StackedInline):
    model = File
    extra = 0
    fields = ['title', 'file', 'is_enable']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInlineAdmin, ]  # Added inline model for file




# @admin.register()
# class FileAdmin():
#     pass