from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription', null=False)

    # ex) 이미지가 아닌 사이즈, 언제 찍었는지 등 외부정보
    class Meta:
        unique_together = ['user', 'project']
