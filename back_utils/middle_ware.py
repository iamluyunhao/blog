from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponse, HttpResponseRedirect
from backweb.models import User
import re


class LoginStatusMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        if re.match(r'/web/.*', request.path):
            return None
        if re.match(r'/media/.*', request.path):
            return None
        if request.path in [reverse('backweb:login')]:
            return None
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            request.user = user
            return None
        else:
            return HttpResponseRedirect(reverse('backweb:login'))

    def process_response(self, request, response):
        return response