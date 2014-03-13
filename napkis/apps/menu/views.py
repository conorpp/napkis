from django.http import HttpResponse
from django.utils import timezone, simplejson
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from napkis.apps.menu.models import MenuItem
from napkis.apps.menu.forms import MenuItemForm
from napkis.utils import pubLog, REDIS

@csrf_exempt
def test(request):
    data = {'d1':'Hello world',
            'd2': 'Hello jacob',
            'fields':{'f1':1,
                      'f2':2,
                      'f3':4,
                      'f4':5},
            'urls':{
                'addMenuItem':"""
                
                specify a new menu item\'menu(optional)\',\n
                \'name\', \'desciption(optional)\,\n
                \'price(optional)\', \n
                \'date(optional)\', \n
                meal (choices: \'dinner\', \'breakfast\', \'lunch\')(optional) \n
                
                """}}
    
    
    return HttpResponse(simplejson.dumps(data))

@csrf_exempt
def addMenuItem(request):
    try:
        raw = request.POST
        pubLog('body: '+str(request.body))
        menu = raw.get('menu', '')
        name = raw.get('name', '')
        description = raw.get('description', '')
        try:price = float(raw.get('price', 0))
        except: price  = 0
        date = raw.get('date', '')
        meal = raw.get('meal', '')
        if menu:
            m = MenuItem.objects.create(menu_id=menu, name=name, description=description, price=price,date=date, meal=meal)
        else:
            m = MenuItem.objects.create(name=name, description=description, price=price,date=date, meal=meal)
        pubLog('menu item created successfully.', request.POST)
        REDIS.publish(0, simplejson.dumps({
            'TYPE':'menuitem',
            'html': render_to_string('menuitem.html',{'menus':[m]}),
            'pk':m.pk
            }))
        return HttpResponse('Success', status=200)
    except Exception as e:
        print 'add menu item err',e
        pubLog('add menu item failure'+str(e))
        return
    
@csrf_exempt
def getMenuItems(request):
    pubLog('menu items queried', request.POST)
    query = request.POST.get('name','')
    order = request.POST.get('order','-created')
    num = request.POST.get('max',20)
    
    if query:
        items = MenuItem.objects.filter(name__icontains = query)
    else:
        items = MenuItem.objects.all()
        
    if order: items.order_by(order)
    
    return HttpResponse(serializers.serialize('json', items[:num]))
    


def testing(request):
    return render(request,'testing.html',{'form':MenuItemForm()})
    

def menu(request):
    pubLog('menu requested')
    return render(request, 'menu.html', {'menus':MenuItem.objects.all()})

def index(request):
    pubLog('Index requested')
    return render(request, 'index.html', {})




