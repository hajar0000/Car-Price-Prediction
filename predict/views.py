from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .utils import model
import pandas as pd
import numpy as np
from .forms import PredictionForm

def predict_price(request):
    predicted_price = None
    form = PredictionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        input_data = pd.DataFrame([form.cleaned_data])
        numeric_columns = ['Present_Price', 'Fuel_Type', 'Seller_Type', 'Transmission', 
                          'Owner', 'Age', 'Kms_Driven']
        input_data[numeric_columns] = input_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

        if not input_data.isnull().any().any():
            input_data['log_Age'] = np.log10(input_data['Age'])
            input_data['log_Kms_Driven'] = np.log10(input_data['Kms_Driven'])
            input_data['Precent Price & Log Age'] = input_data['Present_Price'] * input_data['log_Age']
            input_data['Precent Price & Fuel'] = input_data['Present_Price'] * input_data['Fuel_Type']
            input_data = input_data.drop(['Age', 'Kms_Driven'], axis=1)

            input_data = input_data[['Present_Price', 'Fuel_Type', 'Seller_Type', 'Transmission', 
                                    'Owner', 'log_Age', 'log_Kms_Driven', 
                                    'Precent Price & Log Age', 'Precent Price & Fuel']]
            predicted_price = model.predict(input_data)[0][0]

    # If AJAX request, return the result as a partial HTML response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        result_html = render_to_string('predict/result.html', {'predicted_price': predicted_price, 'form': form})
        return JsonResponse({'result_html': result_html})

    # For normal requests, render the full page
    return render(request, 'predict/predict.html', {'form': form, 'predicted_price': predicted_price})
