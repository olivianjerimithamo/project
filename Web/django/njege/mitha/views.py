from django.shortcuts import render

# Create your views here.
def teacher(request):
    Teacher = Teacher.objects.all()
    return render(request, 'fill.html', {"Teacher": teacher})

