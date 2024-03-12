from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.template import loader
from .models import Items,ItemDetails,Cart
from .forms  import CreateUserForm,LoginUserForm
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def Home(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

#Chairs App
#showchairs function to retrive all data from both table and we linked this with loop in showchair.html page
def showchairs(request):
    template=loader.get_template('showchairs.html')
    chairs = ItemDetails.objects.select_related('itemid') #Retrive from DB from both tables (inner join)  
    return HttpResponse(template.render({'chairs':chairs, 'request' : request})) #send the phone object "which is the item table data" to showvhairs page

#details1 function to retrive all data from both table when we want to choses one things or product details that user chosee or send the parameter to the url then backend and we linked this with loop in details1.html page
def details1(request,id):
    template=loader.get_template('details1.html')
    chairs = ItemDetails.objects.select_related('itemid').filter(id=id)
    print(chairs.query)
    context={
        'chairs': chairs,
        'request' : request
    }
    return HttpResponse(template.render(context))

#Auth chairs function
@csrf_exempt
def auth_login(request):
     form=LoginUserForm()
     if request.method=="POST":
          form=LoginUserForm(data=request.POST)
          if form.is_valid():
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']

              user=authenticate(username=username,password=password)
              if user:
                   if user.is_active:
                        login(request,user)
                        return render(request,'index.html')
     context={'form':form}
     return render(request,'auth_login.html',context)

@csrf_exempt
def auth_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")

#register chairs function
@csrf_exempt
def auth_register(request):
    template=loader.get_template('auth_register.html')
    form=CreateUserForm()
    if request.method=="POST":
           form=CreateUserForm(request.POST)
           if form.is_valid():
                form.save()
                return redirect('auth_login')
    context={'registerform':form}
    return HttpResponse(template.render(context=context))

@login_required(login_url='/auth_login/')
def checkout(request):
    template=loader.get_template('checkout.html')
    current_user = request.user.id
    cart=Cart.objects.all().filter(Id_user=current_user).first()
    product=Items.objects.get(id=cart.Id_product)
    
    context={
            'cart':cart,
            'productname':product,
            'request':request
            
    }
    return HttpResponse(template.render(context=context)) 


def add_to_cart(requset,id):
     currentuser=requset.user
     discount=2
     state=False
     chairs=ItemDetails.objects.select_related('itemid').filter(id=id)
    
     for item in chairs:
           net=item.total-discount
     cart = Cart(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
)
     

     currentuser=requset.user.id
     count=Cart.objects.filter(Id_user=currentuser).count()
     print(count)
     cart.save()
     requset.session['countcart']=count
     return redirect("/showchairs")