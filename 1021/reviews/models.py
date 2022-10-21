from django.db import models
from django.conf import settings

RATE_CHOICES = (
    (1, "★"),
    (2, "★★"),
    (3, "★★★"),
    (4, "★★★★"),
    (5, "★★★★★"),
)

title_table = (
    (1, "블랙 아담"),
    (2, "리멤버"),
    (3, "자백"),
    (4, "인생은 아름다워"),
    (5, "에브리씽 에브리웨어 올 앳 원스"),
    (6, "공조2: 인터내셔날"),
    (7, "귀못"),
    (8, "극장판 짱구는 못말려: 수수께끼! 꽃피는 천하떡잎학교"),
)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_title = models.IntegerField(choices=title_table)
    grade = models.IntegerField(choices=RATE_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)

class ReComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.CharField('대댓글', max_length=150)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body