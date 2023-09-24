from django.shortcuts import render
from . import DST
from . import Malar_Rash_Detector
from . import Discoid_Rash
from . import Alopecia
import numpy as np
from PIL import Image
def output(request):
    result = "None"
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        weight = request.POST['weight']
        height = request.POST['height']
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

        # Load the image
        image = Image.open(malar_rash)
        image = image.resize((224, 224))  # Resize to match the input size during training
        image_array = np.array(image) / 255.0  # Normalize pixel values
        # Ensure the image has the same shape as expected by the model (e.g., (1, 224, 224, 3))
        input_image = np.expand_dims(image_array, axis=0)

        # Make predictions
        predictions = Malar_Rash_Detector.model.predict(input_image)
        # Assuming class_labels is a list of class names (e.g., ['class_0', 'class_1'])
        predicted_class_index = np.argmax(predictions)
        predicted_class = Malar_Rash_Detector.class_labels[predicted_class_index]
        if predicted_class == 'Malar rash':
            malar_rash = 1
        else:
            malar_rash = 0

        image2 = Image.open(discoid_rash)
        image2 = image2.resize((224, 224))  # Resize to match the input size during training
        image_array2 = np.array(image2) / 255.0  # Normalize pixel values
        # Ensure the image has the same shape as expected by the model (e.g., (1, 224, 224, 3))
        input_image2 = np.expand_dims(image_array2, axis=0)

        # Make predictions
        predictions2 = Discoid_Rash.model.predict(input_image2)
        # Assuming class_labels is a list of class names (e.g., ['class_0', 'class_1'])
        predicted_class_index2 = np.argmax(predictions2)
        predicted_class2 = Discoid_Rash.class_labels[predicted_class_index2]
        if predicted_class2 == 'Discoid':
            discoid_rash = 1
        else:
            discoid_rash = 0

        image3 = Image.open(alopecia)
        image3 = image3.resize((224, 224))  # Resize to match the input size during training
        image_array3 = np.array(image3) / 255.0  # Normalize pixel values
        # Ensure the image has the same shape as expected by the model (e.g., (1, 224, 224, 3))
        input_image3 = np.expand_dims(image_array3, axis=0)

        # Make predictions
        predictions3 = Alopecia.model.predict(input_image3)
        # Assuming class_labels is a list of class names (e.g., ['class_0', 'class_1'])
        predicted_class_index3 = np.argmax(predictions3)
        predicted_class3 = Alopecia.class_labels[predicted_class_index3]
        if predicted_class3 == 'Alopecia':
            alopecia = 1
        else:
            alopecia = 0
        input_data = [
            age, height, weight, gender, malar_rash, discoid_rash, alopecia, ulcerations,
            photosensitivity, polyarthritis, fatigue, fever_chills, weight_loss,
            pericarditis, endocarditis, pleuritis, cerebritis, headache,
            peripheral_neuropathy, renal_failure, pregnancy_losses, anemia,
            leukopenia, thrombocytopenia
        ]
        for e in input_data:
            e = int(e)
        z = []
        model = DST.clf
        z.append(input_data)
        result = model.predict(z)
        if result == [1]:
            result = "Positive"
        else:
            result = "Negative"
    return render(request, 'output.html', {'result': result, 'name': name})

def forms(request):
    return render(request, 'forms.html', {})

def about(request):
    return render(request, 'about.html', {})

def home(request):
    return render(request, 'home.html', {})
