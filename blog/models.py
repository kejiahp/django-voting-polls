from django.db import models
from PIL import Image
from django.utils import timezone
from django.template.defaultfilters import slugify

class Blog(models.Model):
    title = models.CharField(max_length=100,default="No Title")
    image = models.ImageField(default="defaultuser.jpg", upload_to="blogs/%Y/%m/%d")
    author = models.CharField(max_length=50, default="No Author")
    description = models.TextField(default="No Description")
    is_displayed = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 120 or img.width > 120:
            img = img.resize((800,800), Image.ANTIALIAS)
            img.save(self.image.path)