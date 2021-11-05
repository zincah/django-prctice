from django.shortcuts import render
from googletrans import Translator 


# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        bt = request.POST.get("btext")
        b = request.POST.get("before")
        a = request.POST.get("after")
        translator = Translator()
        trans = translator.translate(bt, src=b, dest=a)
        context.update({
            "bt" : bt,
            "b" : b,
            "a" : a,
            "at" : trans.text
        })
    return render(request, "trans/index.html", context)