from django.shortcuts import render
from userauths.forms import UserRegisterForm

def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render (request, "userauths/sign-up.html", context)