from django.db import models





# class Patient(models.Model):
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     ]
#     Choice = [('Yes', 'yes'), ('No', 'no')]
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     height = models.FloatField()
#     weight = models.FloatField()
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
#     malar_rash = models.ImageField()
#     discoid_rash = models.ImageField()
#     alopecia = models.ImageField()
#     ulcerations = models.CharField(max_length=3, choices=Choice)
#     photosensitivity = models.CharField(max_length=3, choices=Choice)
#     polyarthritis = models.CharField(max_length=3, choices=Choice)
#     fatigue = models.CharField(max_length=3, choices=Choice)
#     fever_chills = models.CharField(max_length=3, choices=Choice, verbose_name='Fever and Chills (at night especially)')
#     weight_loss = models.CharField(max_length=3, choices=Choice, verbose_name='Weight loss/loss of appetite')
#     pericarditis = models.CharField(max_length=3, choices=Choice)
#     endocarditis = models.CharField(max_length=3, choices=Choice)
#     pleuritis = models.CharField(max_length=3, choices=Choice)
#     cerebritis = models.CharField(max_length=3, choices=Choice)
#     headache = models.CharField(max_length=3, choices=Choice)
#     peripheral_neuropathy = models.CharField(max_length=3, choices=Choice)
#     renal_failure = models.CharField(max_length=3, choices=Choice)
#     pregnancy_losses = models.CharField(max_length=3, choices=Choice, verbose_name='Pregnancy Losses')
#     anemia = models.CharField(max_length=3, choices=Choice)
#     leukopenia = models.CharField(max_length=3, choices=Choice)
#     thrombocytopenia = models.CharField(max_length=3, choices=Choice)
#
#     def __str__(self):
#         return self.name
