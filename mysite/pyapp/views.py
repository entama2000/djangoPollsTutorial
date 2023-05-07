from django.shortcuts import render

# Create your views here.
def index_template(request):
    pyapp_data = {
        'str' : 'Django',
        'num' : range(15),
    }
    return render(request, 'index.html', pyapp_data)