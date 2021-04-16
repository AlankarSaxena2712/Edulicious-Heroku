from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact, CLass_1, CLass_2, CLass_3, CLass_4, CLass_5, CLass_6, CLass_7, CLass_8, CLass_9, CLass_10
from users.models import PhoneSave

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        contact = Contact(name=name, email=email, phone=phone, query=query)

        send_mail(
                f"{name} has contacted you.",
                f'{name} has contacted you. Their query is "{query}".\n\n Phone No : {phone}\nEmail : {email}',
                'edulicious2020@gmail.com',
                ['edulicious2020@gmail.com', 'saxenaalankar42@gmail.com'],
                fail_silently=False,
            )

        contact.save()
        thank = True 
        return render(request, 'contact.html', {'thank':thank})
    return render(request, 'contact.html')

@login_required
def notes(request):
    u_name = request.user.username
    check_verify = PhoneSave.objects.values().filter(name=u_name)
    final_check = False
    for i in check_verify:
        final_check = i['verified']
    if final_check == False:
        thank = True
        return render(request, 'home.html', {'thank':thank})
    else:
        for c in check_verify:
            if c['stud_class'] == 1:
                show_1 = True
                clas_1 = CLass_1.objects.all()
                return render(request, 'notes.html', {'show_1': show_1, 'clas_1':clas_1})
            elif c['stud_class'] == 2:
                show_2 = True
                clas_2 = CLass_2.objects.all()
                return render(request, 'notes.html', {'show_2':show_2, 'clas_2':clas_2})
            elif c['stud_class'] == 3:
                show_3 = True
                clas_3 = CLass_3.objects.all()
                return render(request, 'notes.html', {'show_3':show_3, 'clas_3':clas_3})
            elif c['stud_class'] == 4:
                show_4 = True
                clas_4 = CLass_4.objects.all()
                return render(request, 'notes.html', {'show_4':show_4, 'clas_4':clas_4})
            elif c['stud_class'] == 5:
                show_5 = True
                clas_5 = CLass_5.objects.all()
                return render(request, 'notes.html', {'show_5':show_5, 'clas_5':clas_5})
            elif c['stud_class'] == 6:
                show_6 = True
                clas_6 = CLass_6.objects.all()
                return render(request, 'notes.html', {'show_6':show_6, 'clas_6':clas_6})
            elif c['stud_class'] == 7:
                show_7 = True
                clas_7 = CLass_7.objects.all()
                return render(request, 'notes.html', {'show_7':show_7, 'clas_7':clas_7})
            elif c['stud_class'] == 8:
                show_8 = True
                clas_8 = CLass_8.objects.all()
                return render(request, 'notes.html', {'show_8':show_8, 'clas_8':clas_8})
            elif c['stud_class'] == 9:
                show_9 = True
                clas_9 = CLass_9.objects.all()
                return render(request, 'notes.html', {'show_9':show_9, 'clas_9':clas_9})
            elif c['stud_class'] == 10:
                show_10 = True
                clas_10 = CLass_10.objects.all()
                return render(request, 'notes.html', {'show_10':show_10, 'clas_10':clas_10})

def add_notes(request):
    if request.method == 'POST':
        name = request.POST.get('fileName')
        for_class = request.POST.get('classSelect')
        subject = request.POST.get('subject')
        file_link = request.POST.get('link')
        if for_class == '1':
            cls_1 = CLass_1.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '2':
            cls_1 = CLass_2.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '3':
            cls_1 = CLass_3.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '4':
            cls_1 = CLass_4.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '5':
            cls_1 = CLass_5.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '6':
            cls_1 = CLass_6.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '7':
            cls_1 = CLass_7.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '8':
            cls_1 = CLass_8.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '9':
            cls_1 = CLass_9.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        elif for_class == '10':
            cls_1 = CLass_10.objects.create(file_name=name, subject=subject, file_link=file_link)
            cls_1.save()
            messages.success(request, f'Succesfully added {name}')
        return redirect('add-notes')
    return render(request, 'addNotes.html')