from django.contrib import admin
from .models import sellDog
from .models import sellCat
from .models import dogFood, dogAcc, dogToy, catAcc, catFood, catToy, doctor, feedbackone, trackCat, trackDog

# Register your models here.

@admin.register(dogFood)
@admin.register(sellDog)
@admin.register(sellCat)
@admin.register(dogAcc)
@admin.register(dogToy)
@admin.register(catToy)
@admin.register(catAcc)
@admin.register(catFood)
@admin.register(doctor)
@admin.register(feedbackone)
@admin.register(trackDog)
@admin.register(trackCat)

class foodDogAdmin(admin.ModelAdmin):
    list_display1 = ['id', 'productName', 'img', 'price']

class sellDogAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'breed','age', 'img', 'price', 'phone','address']

class sellCatAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'breed','age', 'img', 'price', 'phone','address']

class dogAccAdmin(admin.ModelAdmin):
    list_display1 = ['id', 'productName', 'img', 'price']

class dogToyAdmin(admin.ModelAdmin):
    list_display1 = ['id', 'productName', 'img', 'price']

class catToyAdmin(admin.ModelAdmin):
    list_display1 = ['id', 'productName', 'img', 'price']

class catFoodAdmin(admin.ModelAdmin):
    list_display1 = ['id', 'productName', 'img', 'price']

class catAccAdmin(admin.ModelAdmin):
    list_display1 = ['id', 'productName', 'img', 'price']

class doctorAdmin(admin.ModelAdmin):
    list_display2 = ['id', 'username', 'pet', 'email', 'address', 'phone', 'reason']

class feedbackAdmin(admin.ModelAdmin):
    list_display3 = ['id', 'name', 'phone', 'email', 'subject', 'message']

class trackDogAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'breed','age', 'img', 'price', 'phone','address']

class trackCatAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'breed','age', 'img', 'price', 'phone','address']