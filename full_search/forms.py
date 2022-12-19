from django import forms

languages =(
    ("-1", "Qualquer Idioma"),
    ("pt", "Portuguese"),
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("en-gb", "English UK"),
    ("ja", "Japanese"),
)


class FullSearchForm(forms.Form):
    Query = forms.CharField(required=True,label= 'Parâmetros de busca:', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert your query here'}))    
    Lang = forms.ChoiceField(choices=languages,label='Idioma:',required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    Date1 = forms.CharField(required=True,label='Data Inicial:',widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'datepicker'}))
    Date2 = forms.CharField(required=True, label='Data Final:',widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'datepicker2'}))
    
    
    #name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    #comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))  
        
        
        
