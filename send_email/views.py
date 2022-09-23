from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import SendEmail
from .utils import send_email


class SendView(View):
    template_name = "send_email/send.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        s = SendEmail()
        # message = request.FILES["message"]
        # s.text = message

        # s.sender1 = sender
        message = input("Input: ")
        print(send_email(message=message))
        return HttpResponse("Done, check your email")
