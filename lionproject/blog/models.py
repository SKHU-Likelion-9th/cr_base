from django.db import models
from django.conf import settings #프로젝트에서 사용하는 유저를 import하기 위해 settings를 가져옴
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank= True, null = True ) # 이거 안써주면 사진 안올렸을 때 에러뜨기 때문에 써줘야함
    # upload_to는 업로드할 폴더를 지정하는 것 임 settings.py에 MEDIA_URL로 지정해둔 media 폴더 안에 blog 폴더를 만들어서 관리하겠다는 설정임

    def __str__(self):
        return self.title  # 글의 제목으로 보이게 하기 위함

    def summary(self):
        return self.body[:100]  # 슬라이싱을 통해 100번째 인덱싱까지 잘라줌