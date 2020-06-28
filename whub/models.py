from django.db import models
from django.core.files import File
from django.contrib.auth.models import User


from multiselectfield import MultiSelectField

MY_CHOICES = ((1, 'Place of interest'),
(2, 'Transportation'),
(3, 'Food'),
(4, 'Events'),
(5, 'Culture'),
(6, 'Residency'))


class Category(models.Model):
    name = MultiSelectField(choices=MY_CHOICES,
    max_choices=3)
    def __str__(self):
        return f"{self.id} - {self.name}"

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.id} - {self.name}"

class Review(models.Model):
    user = models.ForeignKey(User, null= True, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete = models.CASCADE, default = 0)
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField(max_length=200,  blank=True)
    image = models.ImageField(upload_to = 'images', default = 'C:/FP/FP/media/images/default.png')
    cdatetime = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.ForeignKey(Country, null= True, on_delete=models.CASCADE)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.text} - {self.cdatetime}"

class Do(models.Model):
    text = models.CharField(max_length=150)
    review = models.ForeignKey(Review, null= True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id} - {self.text}"

class Dont(models.Model):
    text = models.CharField(max_length=150)
    review = models.ForeignKey(Review, null= True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id} - {self.text}"

class Comment(models.Model):
    text = models.CharField(max_length=150)
    cdatetime = models.CharField(max_length=100, null=True, blank=True)
    review = models.ForeignKey(Review, null= True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null= True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id} - {self.text} - {self.cdatetime}"

# with open('C:\FP\whub\countries.txt', 'r') as f:
#     for line in f:
#         nameofcount = line.split(',')[0]
#         myobject = Country(name=nameofcount[1:len(nameofcount) - 1])
#         myobject.save()
#     f.close()
