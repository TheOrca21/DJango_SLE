from django.shortcuts import render
from django.contrib import messages
from joblib import load


# Create your views here.

def output(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        weight = request.POST['weight']
        gender = request.POST['gender']
        malar_rash = request.FILES['malar_rash']
        discoid_rash = request.FILES['discoid_rash']
        alopecia = request.FILES['alopecia']
        ulcerations = request.POST.get('ulcerations', False)
        photosensitivity = request.POST.get('photosensitivity', False)
        polyarthritis = request.POST.get('polyarthritis', False)
        fatigue = request.POST.get('fatigue', False)
        fever_chills = request.POST.get('fever_chills', False)
        weight_loss = request.POST.get('weight_loss', False)
        pericarditis = request.POST.get('pericarditis', False)
        endocarditis = request.POST.get('endocarditis', False)
        pleuritis = request.POST.get('pleuritis', False)
        cerebritis = request.POST.get('cerebritis', False)
        headache = request.POST.get('headache', False)
        peripheral_neuropathy = request.POST.get('peripheral_neuropathy', False)
        renal_failure = request.POST.get('renal_failure', False)
        pregnancy_losses = request.POST.get('pregnancy_losses', False)
        anemia = request.POST.get('anemia', False)
        leukopenia = request.POST.get('leukopenia', False)
        thrombocytopenia = request.POST.get('thrombocytopenia', False)
        if gender == 'Male' or gender == 'male':
            gender = 1
        else:
            gender = 0
        model = load('final.joblib')
        input_data = [
            age, weight,gender, malar_rash, discoid_rash, alopecia, ulcerations,
            photosensitivity, polyarthritis, fatigue, fever_chills, weight_loss,
            pericarditis, endocarditis, pleuritis, cerebritis, headache,
            peripheral_neuropathy, renal_failure, pregnancy_losses, anemia,
            leukopenia, thrombocytopenia
        ]

        # Make a prediction
        prediction = model.predict([input_data])

    return render(request, 'output.html', {})

def forms(request):
    return render(request, 'forms.html', {})

def about(request):
    return render(request, 'about.html', {})

def home(request):
    return render(request, 'home.html', {})
