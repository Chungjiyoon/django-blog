from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200) #줄 길이 제한
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True) #media/blog/파일이름

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100] #100글자만!
