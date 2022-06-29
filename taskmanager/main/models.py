from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Task(models.Model):
    role = (('red', 'Red'),
            ('yellow', 'Yellow'),
            ('blue','Blue'),
            ('green','Green')
            )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owners notes", blank=True, null=True)
    title = models.CharField('Name', max_length=16)
    task = models.TextField('Task',max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    crossed_out = models.BooleanField ('crossed', default=False)
    color = models.CharField(max_length=10, choices=role, default='red')

    role = (('red','Red'),('yellow','Yellow'))
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/my-board/'

    class Meta:
        verbose_name_plural = 'My board'

class Server_Board(models.Model):
    role = (('red', 'Red'),
            ('yellow', 'Yellow'),
            ('blue','Blue'),
            ('green','Green')
            )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owners notes", blank=True, null=True)
    title = models.CharField('Name', max_length=16)
    task = models.TextField('Task',max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    crossed_out = models.BooleanField ('crossed', default=False)
    reaction_count_in_post = models.ManyToManyField(User,related_name='reaction_count_in_post')
    color = models.CharField(max_length=10, choices=role, default='red')

    role = (('red','Red'),('yellow','Yellow'))

    def total_likes(self):
        return self.reaction_count_in_post.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/server-board/'

    class Meta:
        verbose_name_plural = 'Server board'

# class CustomUser(AbstractUser):
#     avatar_url = models.CharField('avatar_url',max_length= 100, default="https://i.imgur.com/BoZwIXW.png")
# #     bio = models.TextField('bio',max_length=200)
# #     reaction_count = models.CharField('avatar_url',max_length= 100)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar_url = models.CharField('avatar_url',null=True, max_length=100, default="https://i.imgur.com/BoZwIXW.png")
    bio = models.TextField('bio',max_length=300,null=True, default="")
    reaction_count = models.CharField('reaction_count',null=True,max_length= 100, default=0)
    activation_email = models.BooleanField('activat', default=False, null=True)


    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

        instance.userprofile.save()


