from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.name
    


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')  # Image upload path
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        # Truncate the file name if it’s too long
        if self.image and len(self.image.name) > 100:
            file_root, file_ext = os.path.splitext(self.image.name)
            truncated_name = file_root[:100 - len(file_ext)] + file_ext
            self.image.name = truncated_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title