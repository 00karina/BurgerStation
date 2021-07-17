from django.contrib import admin

# Register your models here.
class foodAdmin(admin.ModelAdmin):
    list_filter=['available']
class categoryAdmin(admin.ModelAdmin):
    list_filter=['name']

from api.models import Category,Food,Order
admin.site.register(Food,foodAdmin)
admin.site.register(Category,categoryAdmin)
admin.site.register(Order)