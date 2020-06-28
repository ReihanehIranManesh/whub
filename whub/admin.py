from django.contrib import admin

from .models import Category, Country, Do, Dont, Comment, Review

# Register your models here.

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Do)
admin.site.register(Dont)
admin.site.register(Comment)
admin.site.register(Review)
