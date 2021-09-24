import pdb

from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from register.models import Reg_User
from surveyq.models import SurveyResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def form(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        marital_status = request.POST.get('marital_status')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        ins = Reg_User(first_name=first_name, last_name=last_name, email=email, age=age,
                   marital_status=marital_status, gender=gender, contact=contact, address=address,
                   city=city, state=state, zipcode=zipcode)
        ins.save()
        print('registerd')

    
        email_body = """<pre> 
        Congratulations and Thank you.
        Go to the page: <a href="https://ac4b-1-186-170-61.ngrok.io/survey">click here</a>
        Thanks,
        XYZ Team.
        </pre>"""
    
    
        message = MIMEText(email_body,'html')
        message['Subject'] = 'Link for the Survey'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("neosoft.training.02@gmail.com", "p@ssNeo002")
        server.sendmail("neosoft.training.02@gmail.com", email, message.as_string())

        if not first_name or not last_name or not email or not age or not marital_status or not gender or not address or not city or not state or not zipcode or not contact:
            error_statement = "All fields are required"
            context = {'error_statement':error_statement,
                       'register_form':User.objects.all()}
            return render(request, 'fail.html', context)




    return render(request, 'form.html')

def sur_status(request):
    email_db = Reg_User.objects.values_list('email')
    emails1 = []
    emails2 = []
    for i in range(len(email_db)):
        emails1.append(email_db[i][0])


    y = SurveyResponse.objects.values_list('all_in_one')

    for i in range(len(y)):
        t = y[i][0]
        emails2.append(t['email'])
    # print(emails2, emails1)
    context = {'emails1': emails1, 'emails2':emails2}
    return  render(request, 'email_list.html', context)