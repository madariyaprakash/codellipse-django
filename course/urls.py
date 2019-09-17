from django.urls import path
from course import views
from django.views.generic import TemplateView

urlpatterns =[
    # courses
    path('courses/', TemplateView.as_view(template_name = "courses/courses_page.html")),
    path('select_course/', TemplateView.as_view(template_name = "courses/select_course.html"))
]