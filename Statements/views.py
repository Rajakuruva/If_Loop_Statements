from django.shortcuts import render

# Create your views here.

def If_condition(request):
    d={'a':39,'b':55}
    return render(request,'If_condition.html',d)

def If_Else(request):
    d={'x':140,'y':55}
    return render(request,'If_Else.html',d)

def If_Elif_Else(request):
    d={'a':10,'b':50,'c':140}
    return render(request,'If_Elif_Else.html',d)

def Nested_If(request):
    d={'a':20,'b':30,'c':50}
    return render(request,'Nested_If.html',d)

def Loops(request):
    d={'Name':"Raja",'Village':'Guvva'}
    return render(request,'Loops.html',d)