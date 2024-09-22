from django.contrib import admin
from . models import Author, MyModel
# Register your models here.
admin.site.register(Author)
admin.site.register(MyModel)