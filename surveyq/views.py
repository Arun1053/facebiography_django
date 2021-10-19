from django.shortcuts import render
from django.http import JsonResponse
import pdb
import json
import base64
from deepface import DeepFace
from PIL import Image
import io
import cv2
import numpy as np
from surveyq.models import SurveyResponse, EmotionCaptured



# Create your views here.
def index(request):
    return render(request, 'camcap_tp.html')


questions = ['Would you recommend neosoft to a friend?', 'Is the salary credited on time?',
                 'Is the working environment friendly?', 'Do neosoft have extra engaging events?',
                 'Do neosoft recognise its employees?', 'Any comments or suggestions']
def done(request):
    resp = []
    if request.method == 'POST':

        print('got a post request')
        form = request.POST.get('getdata')
        form = json.loads(form)
        images = json.loads(form['images'])

        resp.append(form['recommed1'])
        resp.append(form['recommed2'])
        resp.append(form['recommed3'])
        resp.append(form['recommed4'])
        resp.append(form['recommed5'])
        resp.append(form['comment'])



        z = []
        z.append(form['email'])

        for img in images:
            x = base64.b64decode(img.split(',')[1])
            image = Image.open(io.BytesIO(x))
            image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
            try:
                obj = DeepFace.analyze(img_path=image)
                z.append(obj['dominant_emotion'])
            except:
                pass
        print(form ['email'], form['recommed1'], form['recommed2'], form['recommed3'], form['recommed4'], form['recommed5'], form['comment'])
        print(z)

        inst = SurveyResponse(all_in_one=form)
        emo = EmotionCaptured(dominant_emotion=z)
        emo.save()
        inst.save()
        request.session['resp'] = resp
        request.session['images'] = images
        return JsonResponse({'status':True})

    resp = request.session['resp']
    images = request.session['images']
    respo = {}
    for i, quest in enumerate(questions):
        respo[quest]=resp[i]

    return render(request, 'form1.html', {'response':respo, 'images':images})