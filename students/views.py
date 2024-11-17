from django.shortcuts import render
from django.views.generic import View

from students.models import Student


class IndexView(View):
    def get(self, request, *args, **kwargs):
        # We can do the main logic here for the get methods
        return render(request, "index.html")



class StudentsListView(View):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        context = {"students": students}
        return render(request, "students_list.html", context)



class StudentDetailView(View):
    def get(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs.get('pk'))
        context = {"student": student}
        return render(request, "student_details.html", context)


