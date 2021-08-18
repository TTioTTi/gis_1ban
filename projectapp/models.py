from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # 게시글 생성 시 게시판 이름 나오도록 하는 기능
    def __str__(self):
        return f'{self.name}'
