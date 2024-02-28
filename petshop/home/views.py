from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import sellDog
from .models import sellCat
from .models import dogFood, dogAcc, dogToy, catToy, catAcc, catFood, trackCat, trackDog
from .forms import sellDogForm
from .forms import sellCatForm
from .forms import doctorForm
from .forms import feedbackForm
from .models import feedbackone
from .models import doctor
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    return render(request, "contactus.html")

def feedback(request):
    return render(request, "feedback.html")

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials!!!")
            return redirect('login')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            messages.info(request, 'Username taken, signup again!!!')
            return redirect('signup')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'e-mail taken, signup again!!!')
            return redirect('signup')
        else:
            user = User.objects.create_user(username = username, first_name = fname, last_name = lname, password = password, email = email)
            user.save()
        return redirect('login')
    else:    
        return render(request, 'signup.html')  

def logout(request):
    auth.logout(request)
    return redirect("/")

def profile(request):
    return render(request, "profile.html")

def seller(request):
    if request.method == "POST":
        form = sellDogForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.POST['username']
            breed = request.POST['breed']
            age = request.POST['age']
            img = request.FILES['img']
            phone = request.POST['phone']
            price = request.POST['price']
            address = request.POST['address']

            obj = sellDog.objects.create(username = username, breed=breed,age = age, phone = phone, img = img, price = price, address = address) 
            obj2 = trackDog.objects.create(username = username, breed=breed,age = age, phone = phone, img = img, price = price, address = address) 
            obj.save()
            obj2.save()
        return redirect("/")
    else:
        print("oh noo")
        form = sellDogForm(request.POST)
    return render(request, 'seller.html',  {"form": form})

def saleDog(request):
    dogInfos = sellDog.objects.all()
    return render(request, "dogs.html", {"dogInfos": dogInfos})

def opt(request):
    return render(request, "opt.html")

def sellCatOk(request):
    if request.method == "POST":
        form = sellCatForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.POST['username']
            breed = request.POST['breed']
            age = request.POST['age']
            img = request.FILES['img']
            phone = request.POST['phone']
            price = request.POST['price']
            address = request.POST['address']
            
            obj = sellCat.objects.create(username = username, breed=breed,age = age, phone = phone, img = img, price = price, address = address)
            obj2 = trackCat.objects.create(username = username, breed=breed,age = age, phone = phone, img = img, price = price, address = address) 
            obj.save()
            obj2.save()
        return redirect("/")
    else:
        print("oh noo")
        form = sellCatForm(request.POST)
    return render(request, 'sellCat.html',  {"form": form})

def saleCat(request):
    catInfos = sellCat.objects.all()
    return render(request, "cats.html", {"catInfos": catInfos})

def accessories(request):
    return render(request, "accessories.html")

def dogAccessories(request):
    dogFoods = dogFood.objects.all()
    dogToys = dogToy.objects.all()
    dogAccs = dogAcc.objects.all()
    return render(request, "dogAccessories.html", {"dogFoods": dogFoods, "dogToys": dogToys, "dogAccs": dogAccs})

def catAccessories(request):
    catFoods = catFood.objects.all()
    catAccs = catAcc.objects.all()
    catToys = catToy.objects.all()
    return render(request, "catAccessories.html", {"catFoods": catFoods, "catToys":catToys, "catAccs": catAccs})

def doctorApp(request):
    print(request.method)
    if request.method == "POST":
        form = doctorForm(request.POST)
        print("till here")
        if form.is_valid():
            username = request.POST['username']
            reason = request.POST['reason']
            phone = request.POST['phone']
            email = request.POST['email']
            pet = request.POST['pet']
            address = request.POST['address']

            obj = doctor.objects.create(username = username, reason = reason, email = email, phone = phone, address = address, pet = pet)
            obj.save()
        return redirect("/appointmentBooked")
    else:
        print("oh noo")
        form = doctorForm(request.POST)
    return render(request, "doctor.html",  {"form": form})

def feedbackMet(request):
    print("ops")
    if request.method == "POST":
        form = feedbackForm(request.POST)
        print("till here")
        if form.is_valid():
            print("success")
            name = request.POST['name']
            subject = request.POST['subject']
            phone = request.POST['phone']
            email = request.POST['email']
            message = request.POST['message']

            obj = feedbackone.objects.create(name = name, subject = subject, email = email, phone = phone, message = message)
            obj.save()
        return redirect("/appointmentBooked")
    else:
        print("oh noo")
        form = feedbackForm(request.POST)
    return render(request, "feedback.html")

def appointmentBooked(request):
    return render(request, "appointmentBooked.html")

def thankyou(request):
    impp = request.COOKIES.get('impp')
    sold1 = sellCat.objects.filter(breed=impp).delete()
    sold2 = sellDog.objects.filter(breed=impp).delete()
    sold1 = trackCat.objects.filter(breed=impp).update(age=0)
    sold2 = trackDog.objects.filter(breed=impp).update(age=0)
    return render(request, "thankyou.html")

@csrf_exempt
def payment(request):
    return render(request, "payment.html")

def offered(request):
    dogIs = sellDog.objects.filter(username=request.user)
    catInfos = sellCat.objects.filter(username=request.user)
    return render(request, "offered.html", {"dogIs": dogIs, "catInfos": catInfos})

def delete(request):
    delll = request.COOKIES.get('mainn')
    dogDel = sellDog.objects.filter(breed=delll).delete()
    trackDogDel = trackDog.objects.filter(breed=delll).delete()

    delll1 = request.COOKIES.get('mainn')
    catDel = sellCat.objects.filter(breed=delll1).delete()
    trackCatDel = trackCat.objects.filter(breed=delll1).delete()
    return render(request, "delete.html")

def sold(request):
    trackInfos = trackDog.objects.filter(age=0,username=request.user)
    trackInfos2 = trackCat.objects.filter(age=0,username=request.user)
    return render(request, "sold.html", {"trackInfos": trackInfos, "trackInfos2": trackInfos2})