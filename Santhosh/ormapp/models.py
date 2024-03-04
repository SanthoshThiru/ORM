from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
	bookname=models.CharField(max_length=30);
	bookid=models.IntegerField(primary_key=True);
	author=models.CharField(max_length=30);
	edition=models.IntegerField();
	shelfno=models.CharField(max_length=10);
class Book_DBAdmin(admin.ModelAdmin):
	list_display=("bookname","bookid","author","edition","shelfno");

