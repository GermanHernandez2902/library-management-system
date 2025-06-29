from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import forms, models
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.contrib.auth import logout
from librarymanagement.settings import EMAIL_HOST_USER
from datetime import date

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'library/index.html')

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'library/studentclick.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'library/adminclick.html')

def custom_logout(request):
    logout(request)
    return redirect('/')

def adminsignup_view(request):
    form = forms.AdminSigupForm()
    if request.method == 'POST':
        form = forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            group, _ = Group.objects.get_or_create(name='ADMIN')
            group.user_set.add(user)
            return redirect('adminlogin')
    return render(request, 'library/adminsignup.html', {'form': form})

def studentsignup_view(request):
    form1 = forms.StudentUserForm()
    form2 = forms.StudentExtraForm()
    if request.method == 'POST':
        form1 = forms.StudentUserForm(request.POST)
        form2 = forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            extra = form2.save(commit=False)
            extra.user = user
            extra.save()
            group, _ = Group.objects.get_or_create(name='STUDENT')
            group.user_set.add(user)
            return redirect('studentlogin')
    return render(request, 'library/studentsignup.html', {'form1': form1, 'form2': form2})

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request, 'library/adminafterlogin.html')
    else:
        return render(request, 'library/studentafterlogin.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def addbook_view(request):
    form = forms.BookForm()
    if request.method == 'POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'library/bookadded.html')
    return render(request, 'library/addbook.html', {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewbook_view(request):
    books = models.Book.objects.all()
    return render(request, 'library/viewbook.html', {'books': books})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def issuebook_view(request):
    form = forms.IssuedBookForm()
    if request.method == 'POST':
        form = forms.IssuedBookForm(request.POST)
        if form.is_valid():
            models.IssuedBook.objects.create(
                enrollment=request.POST.get('enrollment2'),
                isbn=request.POST.get('isbn2')
            )
            return render(request, 'library/bookissued.html')
    return render(request, 'library/issuebook.html', {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewissuedbook_view(request):
    issuedbooks = models.IssuedBook.objects.all()
    li = []
    for ib in issuedbooks:
        issdate = f"{ib.issuedate.day}-{ib.issuedate.month}-{ib.issuedate.year}"
        expdate = f"{ib.expirydate.day}-{ib.expirydate.month}-{ib.expirydate.year}"
        days = (date.today() - ib.issuedate).days
        fine = max(0, (days - 15) * 10)
        books = models.Book.objects.filter(isbn=ib.isbn)
        students = models.StudentExtra.objects.filter(enrollment=ib.enrollment)
        for i, book in enumerate(books):
            if i < len(students):
                student = students[i]
                li.append((student.get_name, student.enrollment, book.name, book.author, issdate, expdate, fine))
    return render(request, 'library/viewissuedbook.html', {'li': li})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewstudent_view(request):
    students = models.StudentExtra.objects.all()
    return render(request, 'library/viewstudent.html', {'students': students})

@login_required(login_url='studentlogin')
def viewissuedbookbystudent(request):
    try:
        student = models.StudentExtra.objects.get(user_id=request.user.id)
    except models.StudentExtra.DoesNotExist:
        return render(request, 'library/viewissuedbookbystudent.html', {
            'error': 'No student profile found for this user.'
        })

    issuedbooks = models.IssuedBook.objects.filter(enrollment=student.enrollment)
    li1 = []
    li2 = []
    for ib in issuedbooks:
        books = models.Book.objects.filter(isbn=ib.isbn)
        for book in books:
            li1.append((request.user, student.enrollment, student.branch, book.name, book.author))
        issdate = f"{ib.issuedate.day}-{ib.issuedate.month}-{ib.issuedate.year}"
        expdate = f"{ib.expirydate.day}-{ib.expirydate.month}-{ib.expirydate.year}"
        days = (date.today() - ib.issuedate).days
        fine = max(0, (days - 15) * 10)
        li2.append((issdate, expdate, fine))
    return render(request, 'library/viewissuedbookbystudent.html', {'li1': li1, 'li2': li2})

def aboutus_view(request):
    return render(request, 'library/aboutus.html')

def contactus_view(request):
    form = forms.ContactusForm()
    if request.method == 'POST':
        form = forms.ContactusForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            name = form.cleaned_data['Name']
            message = form.cleaned_data['Message']
            send_mail(f'{name} || {email}', message, EMAIL_HOST_USER, ['wapka1503@gmail.com'], fail_silently=False)
            return render(request, 'library/contactussuccess.html')
    return render(request, 'library/contactus.html', {'form': form})
