from django.db import models

# Create your models here.


class Article(models.Model):
    # max_length is must param to limit the length
    """
    the variables is the Database of  filed
    """
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
