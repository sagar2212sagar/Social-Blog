from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save

from  django.contrib.auth.models import User
def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")
class Posts(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),


    )
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=200)
    author=models.ForeignKey(User,related_name='blog_post')
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    image=models.ImageField(upload_to=upload_location,blank=True)
    body=models.TextField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    favorite=models.ManyToManyField(User, related_name='favourite',blank=True)

    def __str__(self):
        return self.title
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("blog:post_detail",args=[self.id,self.slug])
@receiver(pre_save,sender=Posts)
def pre_save_slug(sender,**kwargs):
    slug=slugify(kwargs['instance'].title)
    kwargs['instance'].slug=slug

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)


    def __str__(self):
        return "Profile of user {}".format(self.user.username)
class Contact(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact=models.CharField(max_length=20)
    message=models.TextField(max_length=500)
