from django.shortcuts import redirect, render
import pdfplumber
import os


# Create your views here.

def plum_daldal(filename):
    st = ""
    with pdfplumber.open(filename) as pdf:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            st += page.extract_text()
        return st


def index(request):
    context = {}
    if request.method == 'POST':
        if request.FILES:
            pdf = request.FILES.get("pfile")
            context.update({
                "text" : plum_daldal(pdf)
            })
        else :
            return redirect("reader:index")   
    return render(request, "reader/index.html", context)