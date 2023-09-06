from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Naufal Mahdy Hanif',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
