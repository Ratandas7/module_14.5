from django import forms
import datetime

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, initial="Angela")
    comment = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type' : 'date'}))

    BIRTH_YEAR_CHOICES = ['1995', '1996', '1997', '1998', '1999', '2000']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    balance = forms.DecimalField()

    email_address = forms.EmailField(required=False, label="Please enter your email address")

    # first_nam = forms.CharField(initial="Your name")

    i_agree = forms.BooleanField(initial=True)

    day = forms.DateField(initial=datetime.date.today)

    FAVORITE_COLORS_CHOICES = [('blue', 'Blue'), ('green', 'Green'), ('black', 'Black')]

    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_color_1 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_colors_1 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

    # title = forms.CharField()
    # description = forms.CharField()

    # first_name = forms.CharField(max_length=200)
    # last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())

    # typed_favorite_color = forms.TypedChoiceField(choices=FAVORITE_COLORS_CHOICES)

    # typed_favorite_colors = forms.TypedMultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)

    duration = forms.DurationField()

    file = forms.FileField()

    file_path = forms.FilePathField(path='project_1/')

    weight = forms.FloatField()

    image = forms.ImageField()

    Generic_IP_Address = forms.GenericIPAddressField()

    Null_Bool = forms.NullBooleanField()

    # regex = forms.RegexField(regex = "G.*s")

    # slug = forms.SlugField()

    # time = forms.TimeField()

    url = forms.URLField()

    uuid = forms.UUIDField(disabled = True)

    # father = forms.CharField(error_messages={'required' : "please enter your name"})


    