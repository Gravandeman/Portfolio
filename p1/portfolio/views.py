import logging

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from .models import News, Posts, Review
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm, ReviewForm
from .forms import NewsForm, PostForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def parent(request):
    return render(request, 'parent.html')

def question(request):
    return render(request, 'question.html')

def review(request):
    return render(request, 'review.html')
def registration(request):
    return render(request, 'registration/registration.html')


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Измените на страницу, куда перейти после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('')  # Перенаправьте пользователя на главную страницу после входа
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})




@csrf_protect
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm()

    return render(request, 'add_news.html', {'form': form})
@csrf_protect
def add_parent(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parent')
    else:
        form = PostForm()

    return render(request, 'add_parent.html', {'form': form})


def news(request):
    news_list = News.objects.all().order_by('-created_at')  # Получение всех новостей из базы данных
    return render(request, 'news.html', {'news_list': news_list})

def home(request):
    news_list = News.objects.all().order_by('-created_at')  # Получение всех новостей из базы данных
    return render(request, 'home.html', {'news_list': news_list})


def parent(request):
    posts_list = Posts.objects.all()
    return render(request, 'parent.html', {'posts_list': posts_list})



def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news_detail.html', {'news': news})

def parent_detail(request, news_id):
    post = get_object_or_404(Posts, pk=news_id)
    return render(request, 'parent_detail.html', {'post': post})


from django.shortcuts import render, redirect
from .models import Question  # Импортируйте модель Question или другую модель, в которой будете хранить вопросы


@login_required  # Декоратор login_required требует авторизацию пользователя
def ask_question(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']
        user = request.user  # Получаем текущего пользователя

        if question_text:
            # Создаем новый вопрос, связывая его с текущим пользователем
            Question.objects.create(question_text=question_text, asked_by=user)
            return redirect('question')  # Перенаправляем пользователя обратно на страницу с вопросами
        else:
            # Если текст вопроса пустой
            pass

    return render(request, 'question.html')

def question_view(request):
    questions = Question.objects.all()  # Извлекаем все вопросы из базы данных
    context = {'questions': questions}  # Создаем контекст с вопросами
    return render(request, 'question.html', context)  # Отправляем контекст в шаблон

def question(request):
    questions = Question.objects.all()  # Получаем все вопросы из базы данных
    return render(request, 'question.html', {'questions': questions})

def answer_question(request, question_id):
    if request.method == 'POST':
        # Получить данные ответа из POST-запроса
        answer_text = request.POST.get('answer_text')

        try:
            # Найти вопрос по идентификатору
            question = Question.objects.get(pk=question_id)

            # Проверить, что текущий пользователь авторизован 
            if request.user.is_authenticated:
                # Сохранить ответ
                question.answer = answer_text
                question.save()
            else:
                # Пользователь не авторизован, перенаправьте на страницу входа
                return redirect('login')  # Замените 'login' на имя вашей страницы входа

        except Question.DoesNotExist:
            # Обработка случая, если вопрос не найден
            return redirect('question')  # Перенаправьте пользователя обратно на страницу с вопросами

    return redirect('question')


@login_required
def submit_review(request):
    if request.method == 'POST':
        user_review = request.POST.get('user_review', '')  # Получить текст отзыва из формы
        selected_rating = int(request.POST.get('user_rating', 1))  # Получить рейтинг из формы

        # Создайте и сохраните отзыв
        review = Review(author=request.user, text=user_review, rating=selected_rating)
        review.save()
        return redirect('review')
    return render(request, 'review.html')

def review(request):
    reviews = Review.objects.all()  # Извлекаем все отзывы из базы данных
    return render(request, 'review.html', {'reviews': reviews})


