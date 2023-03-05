from django.db import models
from django.contrib.auth.models import User

from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #here we have used a OneToOneField rather than a Foreign Key for the following reasons: (1) If a foreign key is joining two models (say A and B), then A gives uniques B output, but same B's value may give many A output. Eg, Roll no. 10(A) is from class 8th(B), but there are many roll no.s in class 8th.
    #(2) This problems is solved in OneToOneField. Here, every A field gives unique B field's value and vice-versa.  
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (min(img.height,300),min(img.width,300))
            img.thumbnail(output_size) #thumbnail image is smaller sized version of the actual image
            img.save(self.image.path)

        