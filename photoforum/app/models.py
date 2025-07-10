from django.db import models
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent


class forum_user(models.Model):
  nickname = models.CharField(max_length=50) 
  id = models.AutoField(primary_key=True) 
  avatar_image= models.ImageField(upload_to=os.path.join(BASE_DIR, 'avatar'), null=True)

class image(models.Model):
  id = models.AutoField(primary_key=True) 
  author = models.ForeignKey('forum_user', on_delete=models.RESTRICT, null=True)
  feed_image = models.ImageField(upload_to=os.path.join(BASE_DIR, 'image'), null=True, blank=True)
