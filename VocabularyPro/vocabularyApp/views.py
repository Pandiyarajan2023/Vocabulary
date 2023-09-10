from django.shortcuts import render
from vocabularyApp.models import vocabulary
from vocabularyApp.form import vocabularyForm

# Create your views here.

def home(request):
    return render(request,'htmlpage/home.html')

def addvocabulary(request):
    form = vocabularyForm()
    if(request.method=='POST'):
        form=vocabularyForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'htmlpage/addcart.html',{'addpro' : form})

def viewvocabulary(request):
    cart_list = vocabulary.objects.all()
    return render(request,'htmlpage/viewcart.html',{'viewpro' : cart_list})

