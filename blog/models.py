from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.db.models.signals import pre_save
from django.dispatch import receiver
# importing the slugify module 
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# from PIL import Image


# Let's create a model manager to modify the initial queryset so that we could 
# retrieve the only published data
# class PublishedPost(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status="Published")

# class DraftedPost(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status="Draft")


# Create your models here.
class Post(models.Model):
    # post_list = models.Manager() # This is default manager 
    # published = PublishedPost()  # The default PublishedPost manager.
    # drafted = DraftedPost() # This is manager to show the drafted post

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title   =   models.CharField(max_length=100)
    slug    =   models.SlugField(max_length=200)
    author  =   models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE)
    body    =   RichTextUploadingField()
    likes   =   models.ManyToManyField(User, related_name='likes', blank =True)
    created =   models.DateField(auto_now_add=True) #This is modifiable
    updated =   models.DateField(auto_now_add=True)
    status  =   models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    banner   = models.ImageField(upload_to = "post_images/", default="default_post_img.jpg")



    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    # to count the total no of counts
    def total_likes(self):
        return self.likes.count()



# class PostBanner(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to = "post_images/", blank=True, null=True)

#     def __str__(self):
#         return self.post.title + "images"



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # we can also write "Comment" insted of "self"
    reply = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'. format(self.post.title, str(self.user.username))





# class PublishedAQ(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status="Published")


# class DraftedAQ(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status="Draft")


class AskQuestion(models.Model):
    # ask_list = models.Manager()     # This is the main model manager
    # published_aq = PublishedAQ()    # This is ask public question published manager
    # drafted_aq = DraftedAQ()    # This is ask public question drafted manager

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length = 400)
    slug = models.CharField(max_length = 500)
    author = models.ForeignKey(User, related_name="ask_ques", on_delete=models.CASCADE)
    description = RichTextUploadingField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default = 'draft')

    def __str__(self):
        return self.title

@receiver(pre_save, sender = AskQuestion)
@receiver(pre_save, sender = Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug