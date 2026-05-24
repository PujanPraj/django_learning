from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employees')

urlpatterns = [
    # students endpointsse
    # function based view
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    # employees endpoints   
    # class based view
    # path('employees/', views.EmployeeView.as_view()),
    # path('employees/<int:pk>', views.EmployeeDetailView.as_view())

    path('', include(router.urls)),

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentView.as_view()),

    path('blogs/<int:pk>/', views.BlogsDetailView.as_view()),
    path('comments/<int:pk>', views.CommentDetailView.as_view()),
]
