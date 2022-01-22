from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'sendemails/index.html')

def send(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['text']
        from_email = request.POST['from']
        subscribers_list = request.POST['to'].split(',')
        for i in range(len(subscribers_list)):
            subscribers_list[i]=subscribers_list[i].strip()
        send_mail(
        subject,
        message,
        from_email,
        subscribers_list,
        fail_silently=False,
        )
        return HttpResponse('The emails have been successfuly sent.')
