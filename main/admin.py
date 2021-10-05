from django.contrib import admin
from .models import News, Category, Journalist


# Register your models here.


admin.site.register(News)
admin.site.register(Category)
admin.site.register(Journalist)