from django.views import View
from django.shortcuts import render


class BazarIndex(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bazar_index.html')
    

