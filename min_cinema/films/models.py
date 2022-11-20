from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    producer = models.CharField(max_length=50)
    scenario = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')
    trailer = models.URLField(null=True)

    def __str__(self):
        return self.title

class CommentMovie(models.Model):
    comment = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comment')
    text_comment = models.TextField()

