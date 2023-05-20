from django import forms

class MeasurementForm(forms.Form):
    height = forms.FloatField(label='Height')
    weight = forms.FloatField(label='Weight')
    age = forms.IntegerField(label='Age')
    waist = forms.ChoiceField(label='Waist Size')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['waist'].choices = self.get_waist_choices()

    def get_waist_choices(self):
        # Query the waist sizes based on the user's height, weight, and age
        height = self.cleaned_data.get('height')
        weight = self.cleaned_data.get('weight')
        age = self.cleaned_data.get('age')
        # Perform your filtering logic to get the waist size options
        waist_sizes = YourModel.objects.filter(height=height, weight=weight, age=age).values_list('waist', 'waist')
        return waist_sizes