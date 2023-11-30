from jobs.models import Job
from django import forms




class JobForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'description-field'}))
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            
        }