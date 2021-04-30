from django.db import models
from django.conf import settings #프로젝트에서 사용하는 유저를 import하기 위해 settings를 가져옴

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title  # 글의 제목으로 보이게 하기 위함

    def summary(self):
        return self.body[:100]  # 슬라이싱을 통해 100번째 인덱싱까지 잘라줌