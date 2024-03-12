from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.template import loader
from .models import ItemsTabels,ItemDetailsTabels
# from chairs.models import Cart
from .models import Cart2 
from django.contrib.auth.decorators import login_required


#Chairs App
#showchairs function to retrive all data from both table and we linked this with loop in showchair.html page
def showtables(request):
    template=loader.get_template('showtables.html')
    tabels = ItemDetailsTabels.objects.select_related('itemid') #Retrive from DB from both tables (inner join)  
    return HttpResponse(template.render({'tabels':tabels, 'request' : request})) #send the phone object "which is the item table data" to showvhairs page


def detailsTable(request,id):
    template=loader.get_template('detailsTable.html')
    table = ItemDetailsTabels.objects.select_related('itemid').filter(id=id)
    context={
        'table': table,
        'request' : request
    }
    return HttpResponse(template.render(context))

@login_required(login_url='/auth_login/')
def checkout2(request):
    template=loader.get_template('checkouttables.html')
    current_user = request.user.id
    cart=Cart2.objects.all().filter(Id_user=current_user).first()
    product=ItemsTabels.objects.get(id=cart.Id_product)

    
    context1={
            'cart':cart,
            'productname':product,
            'request':request
            
    }
    return HttpResponse(template.render(context=context1)) 

def add_to_cart2(requset,id):
     currentuser=requset.user
     discount=2
     state=False
     table=ItemDetailsTabels.objects.select_related('itemid').filter(id=id)
    
     for item in table:
           net=item.total-discount
     cart = Cart2(
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
     count=Cart2.objects.filter(Id_user=currentuser).count()
     cart.save()
     requset.session['countcart']=count
     return redirect("/showtables")
