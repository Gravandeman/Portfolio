from django.contrib import admin
from .models import News, Posts, Question, Review

admin.site.register(News)
admin.site.register(Posts)
admin.site.register(Question)
admin.site.register(Review)