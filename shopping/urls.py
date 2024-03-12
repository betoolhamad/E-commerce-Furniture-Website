from django.contrib import admin
from django.urls import path
from chairs import views as v1 
from tabels import views as v2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.Home,name="home"),
    path('showchairs/',v1.showchairs,name="showchairs"),
    path('details/<int:id>/',v1.details1,name="details1"),
    path('auth_login/',v1.auth_login,name="auth_login"),
    path('auth_register/',v1.auth_register,name="auth_register"),
    path('auth_logout/',v1.auth_logout,name="auth_logout"),
    path('checkout/',v1.checkout,name="checkout"),
    path('add_to_cart/<int:id>/',v1.add_to_cart,name="add_to_cart"),
    # ##############
    path('showtables/',v2.showtables,name="showtables"),
    path('detailsTable/<int:id>/',v2.detailsTable,name="detailsTable"),

    path('checkout2/',v2.checkout2,name="checkout2"),
    path('add_to_cart2/<int:id>/',v2.add_to_cart2,name="add_to_cart2"),

    







    

]
