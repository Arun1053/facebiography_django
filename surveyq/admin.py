from django.contrib import admin
from surveyq.models import SurveyResponse, EmotionCaptured
# Register your models here.

admin.site.register(SurveyResponse)
admin.site.register(EmotionCaptured)