from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('parent/', views.parent, name='parent'),
    path('question/', views.question, name='question'),
    path('review/', views.review, name='review'),
    path('registration/', views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_news/', views.add_news, name='add_news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('parent/<int:news_id>/', views.parent_detail, name='parent_detail'),
    path('add_parent/', views.add_parent, name='add_parent'),
    path('ask_question/', views.ask_question, name='ask_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('submit_review/', views.submit_review, name='submit_review'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
