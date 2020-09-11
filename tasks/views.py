from django.shortcuts import render, redirect

# Create your views here.
from .models import Task
from .forms import RawTaskForm, RawReminderForm
import datetime

def create_view(request):
    crr_date = datetime.date.today()
    form = RawTaskForm()
    date = crr_date.strftime('%d %b %y')
    if request.method == 'POST':
        form = RawTaskForm(request.POST, request.FILES)
        if form.is_valid():
            Task.objects.create(**form.cleaned_data, status=False, date=crr_date)
            crr_date2 = crr_date + datetime.timedelta(days=1)
            Task.objects.create(**form.cleaned_data, status=False, date=crr_date2)
            crr_date2 = crr_date + datetime.timedelta(days=7)
            Task.objects.create(**form.cleaned_data, status=False, date=crr_date2)
            crr_date2 = crr_date + datetime.timedelta(days=30)
            Task.objects.create(**form.cleaned_data, status=False, date=crr_date2)
            return redirect("list")
        else:
            form = RawTaskForm()
    return render(request, "create.html", {"form":form, "crr_date":crr_date, "date":date})

def todo_view(request):
    crr_date = datetime.date.today()
    form = RawTaskForm()
    date = crr_date.strftime('%d %b %y')
    if request.method == 'POST':
        form = RawTaskForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            Task.objects.create(**form.cleaned_data, status=False, date=crr_date)
            return redirect("list")
        else:
            form = RawTaskForm()
    return render(request, "todo.html", {"form":form, "crr_date":crr_date, "date":date})

def reminder_view(request):
    crr_date = datetime.date.today()
    form = RawReminderForm()
    date = crr_date.strftime('%d %b %y')
    if request.method == 'POST':
        form = RawReminderForm(request.POST, request.FILES)
        if form.is_valid():
            Task.objects.create(**form.cleaned_data, status=False)
            return redirect("list")
        else:
            form = RawReminderForm()
    return render(request, "reminder.html", {"form":form, "crr_date":crr_date, "date":date})

def list_view(request):
    crr_date = datetime.date.today()
    date = crr_date.strftime('%d %b %y')
    print(crr_date)
    qset = Task.objects.filter(date=crr_date, status=False)
    qset2 = Task.objects.filter(date=crr_date, status=True)
    if request.method == 'POST':
        obj = Task.objects.get(id=int(request.POST.get("qwerty")))
        print(obj)
        print(obj.status)
        if obj.status:
            obj.status = False
        else:
            obj.status = True
        obj.save()
        return redirect("list")
    return render(request, "list.html", {"crr_date":crr_date, "qset":qset, "qset2":qset2, "date":date})
            
            