from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150, default='')
    last_name = models.CharField(max_length=150, default='')
    position = models.CharField(max_length=150, default='')
    manager = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
class Menu(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=2000,default='')
    def __unicode__(self):
        return self.name
    
class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, null=True, blank=True)
    
    name = models.CharField(max_length=200, default='', null=True)
    description = models.CharField(max_length=2000,default='', null=True)
    
    price = models.FloatField(default=0, null=True)
    day = models.DateTimeField(auto_now_add=True, null=True)
    choices = (('dinner', 'dinner'), ('lunch', 'lunch'), ('breakfast', 'breakfast'))
    meal = models.CharField(choices=choices, max_length=100, default='', null=True)
    
    date = models.DateTimeField(auto_now_add=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100, default='')
    size = models.IntegerField(default=1)
    ready = models.BooleanField(default=False)
    notes = models.CharField(default= '', max_length=5000 )
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    group = models.ForeignKey(Group)
    menuItem = models.ForeignKey(MenuItem)
    created = models.DateTimeField(auto_now_add=True)

    
class Tag(models.Model):
    menu = models.ForeignKey(Menu, blank=True, null=True)
    menuItem = models.ForeignKey(MenuItem, blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True)
    order = models.ForeignKey(Order, blank=True, null=True)
    
    tag = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)




