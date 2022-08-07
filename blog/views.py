from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import*
from .forms import* 
from django.core.mail import send_mail, BadHeaderError

menu = [{'title':"Главная", 'url_name':'home'},
        {'title':'Продукты','url_name':'products'},
        {'title':'Решения','url_name':'cases'},
        {'title':'Контакты','url_name':'add_post'}]


def home(request):
    return render(request, "home.html", {'menu': menu,'title':'Главная страница'})

def products(request):
    return render(request, "products.html", {'menu': menu,'title':'Продукты'})

def cases(request):
    return render(request, "cases.html", {'menu': menu,'title':'Решения'})
    
def success(request):
    return render(request, "success.html", {'menu': menu,'title':'Обратная связь'})


def add_post(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                #'phone_number':form.cleaned_data['phone_number'],
                'content': form.cleaned_data['content'],
            }
            content = "\n".join(body.values())
            try:
                send_mail(subject, content, 
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            
            return redirect("success")

    form = ContactForm()
    return render(request, "add_post.html", {'menu': menu,'form': form,'title':'Обратная связь'})






