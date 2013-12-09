
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
import httplib2
import urlparse


def index(request):
   return render(request, 'index.html')

def search(request):
   errors = []
   if 'url' in request.GET and request.GET['url']:
      url = request.GET['url']
     
      try:
         if not url.startswith('http'):
            url = "http://"+url            
         h = httplib2.Http()
         resp = h.request(url, "HEAD")      
      
         if (int(resp[0]['status']) < 400):
            html= 'exito.html'
         else:
            html= 'fail.html'
         return render(request, html, {'pagina': url})

      except:
         errors.append('Invalid URL.')
         return render(request, 'index.html', {'errors': errors})         
   else:
      message = 'You must enter a URL.'
      errors.append(message)
      return render(request, 'index.html', {'errors': errors})
   
   
def exito(request):
   return render(request, 'exito.html')

def fail(request):
   return render(request, 'fail.html')