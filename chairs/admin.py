from django.contrib import admin
from .models import Items,ItemDetails

#ادمن هي خدمة من دجانقو وهي عبارة لوحة تحكم نستطيع من خلالها التحكم بالبيانات واضافتها وهو يستطيع ادارة كل تطبيقاتك 

admin.site.register(Items)
admin.site.register(ItemDetails)
#، هذي عملية تسجيل المودل في ملف الادمن، استوردناهم ثم سجلناهم
# Register your models here.
