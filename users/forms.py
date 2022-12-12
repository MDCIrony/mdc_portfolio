from django import forms

class NewProjectForm(forms.Form):
    FAVORITE_TECHNOLOGIES = [
        ('html', 'HTML'),
        ('python', 'Python'),
        ('javascript', 'Javascript'),
        ('css3', 'CSS3'),
        ('java', 'Java'),
        ('flask', 'Flask'),
        ('django', 'Django'),
    ]

    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))

    type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))

    date = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3'
    }))

    technologies = forms.MultipleChoiceField(
        required = False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_TECHNOLOGIES,
    )
