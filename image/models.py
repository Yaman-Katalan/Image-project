from django.db import models

class Image(models.Model):
    pixabay_id = models.IntegerField(unique=True)
    page_url = models.URLField(max_length=200)
    type = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)
    preview_url = models.URLField(max_length=200)
    webformat_url = models.URLField(max_length=200)
    large_image_url = models.URLField(max_length=200)
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    views = models.IntegerField()
    downloads = models.IntegerField()
    likes = models.IntegerField()
    comments = models.IntegerField()
    user = models.CharField(max_length=100)
    user_image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.tags
