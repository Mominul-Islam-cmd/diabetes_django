from django.http import HttpResponse # type: ignore
import pickle
import numpy as np # type: ignore
import pandas as pd # type: ignore
from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore
import joblib # type: ignore





def diabetics_home(request):
    return render(request,'home.html')


