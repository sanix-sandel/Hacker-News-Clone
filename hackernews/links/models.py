from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Link(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField()

    submitted_by=models.ForeignKey(User, related_name='links_sub', on_delete=models.CASCADE)
    upvotes=models.ManyToManyField(User, related_name='votes', blank=True)

    submitted_on=models.DateTimeField(auto_now_add=True, editable=False)

    def get_absolute_url(self):
        return reverse('link_view', args=[self.id])


class Comment(models.Model):
    body=models.TextField()
    commented_on=models.ForeignKey(Link, related_name='comments', on_delete=models.CASCADE)
    in_reply_to=models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    commented_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True, editable=False)
