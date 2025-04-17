# импортируем библиотеки для ответов, обработки форм и нашу модель БД
from django.shortcuts import render
from .forms import UserForm
from .models import Person

# вывод формы, обработка результата, запись в БД и отработка шаблонов HTTP
def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            registration_number = userform.cleaned_data["registration_number"]

            putdata = Person(textbox1_text=registration_number, textbox2_text=name)
            putdata.save()
            return render(request, "backpage.html", {"name": name, "registration_number": registration_number})
    return render(request, "index.html", {"form": userform})

