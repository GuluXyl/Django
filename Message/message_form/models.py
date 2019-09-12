from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length = 32,verbose_name="姓名",primary_key=True)
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100,verbose_name="联系地址")
    message = models.TextField()

    class Meta:
        pass