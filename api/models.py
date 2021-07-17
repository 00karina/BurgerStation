from django.db import models
from django.conf import settings
import datetime
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name
        
    @staticmethod
    def get_all_categories():
        return Category.objects.all()


class Food(models.Model):
    category=models.ForeignKey(Category,related_name='food',on_delete=models.CASCADE,default=1)
    img=models.ImageField(upload_to="img")
    name=models.CharField( max_length=100)
    desc=models.TextField()
    price=models.PositiveIntegerField(default=0)
    available=models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def get_all_food():
        return Food.objects.all()
    
    @staticmethod
    def get_all_food_by_category(category_id):
        if category_id:
            return Food.objects.filter(category=category_id)
        else:
     
           return Food.objects.all()
    
    @staticmethod
    def get_food_by_id(ids):
        return Food.objects.filter(id__in=ids)

class Order(models.Model):
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer_id(user_id):
        return Order.objects.filter(customer=user_id)