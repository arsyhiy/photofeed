from django.db import models
import uuid


class user(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatar/', null=True)

    def __str__(self):
        return str(self.name)

class GalleryImage(models.Model):
    author = models.ForeignKey(user,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)


