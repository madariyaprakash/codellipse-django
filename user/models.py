from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # CASCADE means when we delete the use, respective profile pic will get deleted,
    # However, when we delete the picture, user account is not going to be deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to='profile_pics')

    
    def __str__(self):
        return f'{self.user.username} Profile'

    # this will run after model saved, this method is already in parent cls, however, we're
    # creating our own to add some functionality here
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        # opennig image for current user
        img = Image.open(self.image.path)
        if img.height>300 or img.width>300: 
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

