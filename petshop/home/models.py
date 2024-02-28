from django.db import models

breed_choice = (
  ('German shephard', 'German shephard'),
('labrador', 'labrador'),
('pug', 'pug'),
('Golden Retriever','Golden Retriever'),
('Siberian Husky','Siberian Husky'),
('Rottweiler', 'Rottweiler'),
('Bulldog','Bulldog'),
('Put Bull','Pit Bull'),
('Pomeranian','Pomeranian'),
('Basset Hound','Basset Hound')
)

breed_choice_cat = (('Siamese cat', 'Siamese cat'),
('Persian cat', 'Persian cat'),
('Somali cat', 'Somali cat'),
('Burmese cat', 'Burmese cat'),
('American bobtail', 'American bobtail'))


pet_choice = (('dog', 'dog'),
              ('cat', 'cat'))
# Create your models here.
class sellDog(models.Model):
    username = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, choices=breed_choice)
    age = models.PositiveIntegerField()
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    address = models.TextField(max_length=100)

class sellCat(models.Model):
    username = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, choices=breed_choice_cat)
    age = models.PositiveIntegerField()
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    address = models.TextField(max_length=100)

class dogFood(models.Model):
    productName = models.CharField(max_length=300)
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()

class dogAcc(models.Model):
    productName = models.CharField(max_length=300)
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()

class dogToy(models.Model):
    productName = models.CharField(max_length=300)
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()

class catFood(models.Model):
    productName = models.CharField(max_length=300)
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()

class catAcc(models.Model):
    productName = models.CharField(max_length=300)
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()

class catToy(models.Model):
    productName = models.CharField(max_length=300)
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()

class doctor(models.Model):
    username = models.CharField(max_length=200, blank=True)
    reason = models.TextField(max_length=500, blank=True)
    phone = models.PositiveIntegerField( blank=True)
    email = models.CharField(max_length=300, blank=True)
    address = models.TextField(max_length=300, blank=True)
    pet = models.CharField(max_length=300,choices=pet_choice)

class feedbackone(models.Model):
    name = models.CharField(max_length=300)
    phone = models.PositiveIntegerField()
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=500)

class trackDog(models.Model):
    username = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, choices=breed_choice)
    age = models.PositiveIntegerField()
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    address = models.TextField(max_length=100)

class trackCat(models.Model):
    username = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, choices=breed_choice_cat)
    age = models.PositiveIntegerField()
    img = models.ImageField(blank=True)
    price = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    address = models.TextField(max_length=100)