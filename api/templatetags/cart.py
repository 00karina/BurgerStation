from django import template
import datetime
register = template.Library()

@register.filter(name='is_in_cart')


def is_in_cart(food, cart):
    keys = cart.keys()
    
    for id in keys:
        
        if int(id) == food.id:
            
           return True
    return False;


@register.filter(name='card_quantity')


def card_quantity(food, cart):
    keys = cart.keys()
    for id in keys:
        print(id,food.id)
        if int(id) == food.id:
           return cart.get(id)
    return 0;

@register.filter(name='total')
def total(food, cart):
    return food.price * card_quantity(food, cart)


@register.filter(name='total_cart_price')

def total_cart_price(foods, cart):
    sum=0 
    for food in foods:
        sum += total(food ,cart)
    return sum

@register.filter(name='dollar')
def dollar(number):
    return "$"+str(number)

@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1