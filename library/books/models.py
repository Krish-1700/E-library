from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.IntegerField()
    language=models.CharField(max_length=20)
    pages=models.IntegerField()
    image=models.ImageField(upload_to="images")
    pdf=models.FileField(upload_to="pdf")
