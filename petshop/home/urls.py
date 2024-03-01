from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SuccessView, ContactView

urlpatterns = [
    path("", views.index, name="home"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("contactus", views.contactus, name="contactus"),
    path("feedback", views.feedbackMet, name="feedback"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("profile", views.profile, name="profile"),
    path("seller", views.seller, name="seller"),
    path("dogs", views.saleDog, name="saleDog"),
    path("cats", views.saleCat, name="saleCat"),
    path("opt", views.opt, name="opt"),
    path("sellcat", views.sellCatOk, name="sellCat"),
    path("accessories", views.accessories, name="accessories"),
    path("dogAccessories", views.dogAccessories, name="dogAccessories"),
    path("catAccessories", views.catAccessories, name="catAccessories"),
    path("doctor", views.doctorApp, name="doctor"),
    path("payment", views.payment, name="payment"),
    path("appointmentBooked", views.appointmentBooked, name="appointmentBooked"),
    path("thankyou", views.thankyou, name="thankyou"),
    path("offered", views.offered, name= "offered"),
    path("delete", views.delete, name="delete"),
    path("sold", views.sold, name="sold"),
    path("", include("sendemail.urls")), 
    path("doctor", ContactView.as_view(), name="contact"),
    path("appointmentBooked", SuccessView.as_view(), name="success"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)