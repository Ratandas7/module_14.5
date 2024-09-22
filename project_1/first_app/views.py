from django.shortcuts import render, redirect
from first_app . forms import ContactForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'first_app/home.html', {'form' : form})