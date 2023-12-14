from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Customer

User = get_user_model()


class IndexView(View):
    def get(self, request):
        context = {}
        try:
            user = User.objects.get(id=request.user.id)
            context["user"] = user
        except User.DoesNotExist:
            user = None
        try:
            customer = Customer.objects.get(id_user_id=user)
            context["customer"] = customer
        except Customer.DoesNotExist:
            pass
        return render(request, "index.html", context)
