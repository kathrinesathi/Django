from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('products',views.products,name='products'),
    path('book/<int:book_id>/',views.detail,name='detail'),

]