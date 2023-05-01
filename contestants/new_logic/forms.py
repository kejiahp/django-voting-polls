from django import forms

height_measurement = [
    ("Ft", "Ft"),
    ("Mm", "Mm")
]
experience_types = [
    ("beginner", "beginner"),
    ("intermediate", "intermediate"),
    ("professional", "professional")
]
gender_types = [
    ("male", "male"),
    ("female", "female")
]
agency_choices = [
    ("True", "True"),
    ("False", "False")
]


class NewPageantRegistrationForm(forms.Form):

    firstname = forms.CharField(max_length=300, required=True)
    lastname = forms.CharField(max_length=300, required=True)
    instagram_handle = forms.CharField(max_length=300, required=True)
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=gender_types, required=True)
    date_of_birth = forms.DateField(required=True)
    height_type = forms.ChoiceField(choices=height_measurement, required=True)
    height = forms.IntegerField(min_value=0, required=True)
    image1 = forms.ImageField(required=True)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    state_of_residence = forms.CharField(widget=forms.Textarea, required=True)
    phonenumber = forms.CharField(required=True)

    is_in_agency = forms.ChoiceField(choices=agency_choices, required=True)

    agency_name = forms.CharField(max_length=300, required=False)
    agency_modeling_image = forms.ImageField(required=False)
    modeling_experience = forms.ChoiceField(
        choices=experience_types, required=False)
