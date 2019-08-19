from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=10, null=False, primary_key=True)
    title = models.CharField(max_length=100, null=False)
    price = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    discountAvilable = models.BooleanField()
    discountPrice = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    stock = models.CharField(max_length= 30)
    specifications = models.TextField()
    imgUrl = models.ImageField(
        upload_to="Products/", null=True, verbose_name="")
    def __str__(self):
        return str(self.title)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    review = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.review)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shippingAddress = models.CharField(max_length=500, null=True)
    billingAddress = models.CharField(max_length=500, null=True)
    billingMethod = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()