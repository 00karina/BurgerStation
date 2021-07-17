from django.shortcuts import render,redirect 
from django.views import View
from .models import Food,Category,Order
from django.contrib.auth.models  import auth,User
from django.contrib.auth.hashers import  check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
class Index(View):
    def post(self,request):
        food=request.POST.get('food')
        
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(food)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(food)
                    else:
                        cart[food]=quantity-1
                else:
                    cart[food]=quantity+1
                
            else:
                cart[food]=1
        else:
            cart={}
            cart[food]=1
        request.session['cart']=cart
       
        return redirect('index')
        
    def get(self,request):
        

        foods=None
       
        categories=Category.get_all_categories()
        categoryID=request.GET.get('category')
        
       
        if categoryID:
            foods=Food.get_all_food_by_category(categoryID)
        else:
            foods=Food.get_all_food();
        data={}
        data['foods']=foods
        data['categories']=categories
        
        return render(request,"index.html",data)

    

def signup(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
        return redirect('/')
        
    else:
        return render(request,'signup.html')



def cart(request):
    if request.user.is_authenticated:
        if request.session.get('cart')==None:
            return redirect('/')
        else:

            ids=list(request.session.get('cart').keys())
            foods=Food.get_food_by_id(ids)
            
    else:
        return redirect('login')    
        
    return render(request,'cart.html',{'foods':foods})

def logins(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username,password=password)
        request.session['user'] = user.id
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def checkout(request):
    if request.method=='POST':
    
        user=request.session.get('user')
        print("user",user)
        cart=request.session.get('cart')
        foods=Food.get_food_by_id(list(cart.keys()))
        

        for food in foods:
            order=Order(customer=User(id=user),
            food=food,
            price=food.price,
        
            
            quantity=cart.get(str(food.id))
            )
            order.save()
        
        return redirect('cart')

class order(View):
    def get(self,request):
        user=request.session.get('user')
        orders=Order.get_order_by_customer_id(user)
        

        return render(request,'order.html',{"orders":orders})
