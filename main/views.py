from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Aidah Cantul',
        'class': 'PBP Apaya'
    }

    return render(request, "main.html", context)