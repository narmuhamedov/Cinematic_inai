from django.db import models

class TvShow(models.Model):
    GENRE = (
        ('HORROR', "HORROR"),
        ("ANIME", "ANIME"),
        ("COMEDY", "COMEDY"),
        ("FANTASY", "FANTASY"),
        ("ROMANTIC", "ROMANTIC"),
        ("DRAMMA", "DRAMMA")
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    quantity = models.IntegerField()
    trailer = models.URLField()
    genre =  models.CharField(choices=GENRE, max_length=100)

    def __str__(self):
        return self.title


class CommentTvShow(models.Model):
    comment = models.ForeignKey(TvShow, on_delete=models.CASCADE, related_name='comment_object')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment.title