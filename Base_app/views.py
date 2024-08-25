from django.shortcuts import render
from django.http import HttpResponse
from Base_app.models import Book_table1,Aboutus,Feedback,ItemList,Items
# Create your views here.
def home(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    review= Feedback.objects.all()
    return render(request, 'home.html',{'items':items,'list':list,'review':review})

def about(request):
    data= Aboutus.objects.all()
    return render(request, 'about.html', {'data':data})

def order(request):
    return render(request, 'order.html')

def feedback(request):
    if request.method=="POST":
        user_name = request.POST.get('user_name')
        description = request.POST.get('Description')
        rating = request.POST.get('Rating')
        image = request.FILES.get('Image')
        print("User Name:", user_name)
        print("Description:", description)
        print("Rating:", rating)
        print("Image:", image)
        if user_name and description and rating and image:
            # Create and save the Feedback object
            data = Feedback(User_name=user_name, Description=description, Ratings=rating, Image=image)
            data.save()
                  
    return render(request, 'feedback.html')

def book_table(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        person=request.POST.get('person')
        date=request.POST.get('date')
        if name!=" " and email!=" " and number!=" " and person!=" " and date !=" ":
            data=Book_table1(Name=name,Email=email,Number=number,Person=person,Date=date)
            data.save()
    return render(request, 'book_table.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    return render(request, 'menu.html',{'items':items,'list':list})