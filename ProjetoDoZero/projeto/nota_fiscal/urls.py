from django.urls import path
from .views import criar_nota_fiscal

urlpatterns = [    
    path('criar/', criar_nota_fiscal, name='nota_fiscal_criar'),
]