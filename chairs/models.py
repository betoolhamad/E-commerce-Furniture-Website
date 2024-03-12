from django.db import models

class Items(models.Model): #هذا جدول اسمه العناصر
    name=models.CharField(max_length=50) #كل سجل في هذا الجدول مرتبط بأكثر من سجل بالجدول الثاني فالعلاقة many to many 
    def __str__(self):
        return self.name #عشان نُظهر اسم الجوال لما نحطه داخل الجدول في صفحة الادمن

class ItemDetails(models.Model): #هذا جدول اسمه تفاصيل العناصر
    color=models.CharField(max_length=50) #هنا نمثل الحقول اللي بنحتاجها داخل الجدول
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150,null="True")
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    itemid=models.ForeignKey(Items,on_delete=models.CASCADE) #هنا قلنا ان الاي دي بالجدول الاول يعتبر فورن كي بالجدول الثاني .. 
    #واللي بين قوسين نقول ان اي عملية حذف سجل في جدول الاب راح تنحذف كل السجلات المرتبطة بالسجل اللي انا حذفته في جدول الاب
    def __str__(self):
        return self.color

class Cart(models.Model):
    Id_product=models.IntegerField()
    Id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    Created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Id_product