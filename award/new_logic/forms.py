from django import forms

gender_types = [
    ("male", "male"),
    ("female", "female")
]

categories = [("VIDEO DIRECTOR OF THE YEAR", "VIDEO DIRECTOR OF THE YEAR"), ("PAGEANT ICON OF THE YEAR", "PAGEANT ICON OF THE YEAR"), ("ARTISTE OF THE YEAR", "ARTISTE OF THE YEAR"), ("MEDIA PERSONALITY OF THE YEAR", "MEDIA PERSONALITY OF THE YEAR"), ("ENTREPRENEUR OF THE YEAR", "ENTREPRENEUR OF THE YEAR"), ("CINEMATIC STAR OF THE YEAR", "CINEMATIC STAR OF THE YEAR"), ("SONG / ARTISTE OF THE YEAR", "SONG / ARTISTE OF THE YEAR"), ("BRAND OF THE YEAR", "BRAND OF THE YEAR"), ("DANCER OF THE YEAR", "DANCER OF THE YEAR"), ("MODEL OF THE YEAR OF THE YEAR", "MODEL OF THE YEAR OF THE YEAR"), ("COMEDIAN / SKITMAKER OF THE YEAR", "COMEDIAN / SKITMAKER OF THE YEAR"), ("FASHION DESIGNER OF THE YEAR", "FASHION DESIGNER OF THE YEAR"),
              ("REAL ESTATE COMPANY OF THE YEAR", "REAL ESTATE COMPANY OF THE YEAR"), ("SKINCARE BRAND OF THE YEAR", "SKINCARE BRAND OF THE YEAR"), ("CREATIVE DIRECTOR OF THE YEAR", "CREATIVE DIRECTOR OF THE YEAR"), ("MC OF THE YEAR", "MC OF THE YEAR"), ("ATHLETE OF THE YEAR", "ATHLETE OF THE YEAR"), ("SOCIAL MEDIA INFLUENCER OF THE YEAR", "SOCIAL MEDIA INFLUENCER OF THE YEAR"), ("CONTENT CREATOR OF THE YEAR", "CONTENT CREATOR OF THE YEAR"), ("TV STAR OF THE YEAR", "TV STAR OF THE YEAR"), ("MAKEUP ARTISTE OF THE YEAR", "MAKEUP ARTISTE OF THE YEAR"), ("CEO OF THE YEAR", "CEO OF THE YEAR"), ("CREATIVE OF THE YEAR", "CREATIVE OF THE YEAR"), ("WRITER / BLOGGER OF THE YEAR", "WRITER / BLOGGER OF THE YEAR"), ("DJ OF THE YEAR", "DJ OF THE YEAR")]


class NewAwardsRegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=300, required=True)
    lastname = forms.CharField(max_length=300, required=True)
    email = forms.EmailField(required=True)

    category = forms.ChoiceField(
        choices=categories, required=True)

    date_birth = forms.DateField(required=True)
    instagram_handle = forms.CharField(max_length=300, required=True)
    gender = forms.ChoiceField(choices=gender_types)
    brand_name = forms.CharField(max_length=300, required=True)
    industry_years = forms.IntegerField(required=True)
    image = forms.ImageField(required=False)
