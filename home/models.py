from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=100)

class competition(models.Model):
    PENDING = 0
    DRAWN = 1
    STATUS_CHOICES = (
        (PENDING, 'PENDING'),
        (DRAWN, 'DRAWN'),
    )
    image = models.ImageField(upload_to ='competitions/')
    image1 = models.ImageField(upload_to ='competitions/')
    image2 = models.ImageField(upload_to ='competitions/')
    name = models.CharField(max_length=30)
    slug=models.SlugField(max_length=200,unique=True)
    description = models.CharField(max_length=30)
    detail = models.CharField(max_length=30000)
    no_of_tickets = models.PositiveIntegerField()
    sold_tickets  = models.PositiveIntegerField(default=0)
    price=models.PositiveIntegerField()
    end_time=models.DateTimeField()
    question1=models.CharField(max_length=30000)
    question2=models.CharField(max_length=30000)
    question3=models.CharField(max_length=30000)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name
        super(competition, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

   

class tickets(models.Model):
    competition_id = models.ForeignKey(competition, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = 'tickets'
        verbose_name = 'Tickets for different comprtition'

class winner(models.Model):
    ticket=models.ForeignKey(tickets, on_delete=models.CASCADE)

