from django.test import TestCase
from .models.Mensagem import Mensagem
from .models.Observer import Observer
# Create your tests here.

#Teste Observer
mensagem = Mensagem()
observer = Observer()
mensagem.attach(observer)
mensagem.status = '123'