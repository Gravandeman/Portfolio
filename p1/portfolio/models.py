from django.db import models
from django.contrib.auth.models import User



class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='parent_images/', null=True)


    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_text





class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем, создавшим отзыв
    text = models.TextField()  # Текст отзыва
    rating = models.PositiveIntegerField(default=1)  # Рейтинг (например, от 1 до 5)

    @property
    def rating_range(self):
        return range(self.rating)

    @property
    def empty_stars(self):
        return range(5 - self.rating)

    def __str__(self):
        return f"Отзыв от {self.author.first_name} {self.author.last_name}"


