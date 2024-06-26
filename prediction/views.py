# prediction/views.py
from django.http import HttpResponse # type: ignore
import pickle
import numpy as np # type: ignore
import pandas as pd # type: ignore
from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore
import joblib # type: ignore


# Load the trained model and preprocessing objects
model = joblib.load('prediction/models/knn_model.pkl')
scaler = joblib.load('prediction/models/scaler.pkl')

def predict_diabetes(request):
    if request.method == 'POST':
        age = float(request.POST.get('age'))
        hypertension = int(request.POST.get('hypertension'))
        heart_disease = int(request.POST.get('heart_disease'))
        bmi = float(request.POST.get('bmi'))
        hba1c_level = float(request.POST.get('hba1c_level'))
        blood_glucose_level = float(request.POST.get('blood_glucose_level'))
        Female = float(request.POST.get('Female'))
        Male= float(request.POST.get('Male'))
        Other= float(request.POST.get('Other'))
        
      
        
        input_data = np.array([[age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level,Female,Male,Other]])
        input_data = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        
        return render(request, 'result.html', {'result': result})
    
    return render(request, 'design.html')
