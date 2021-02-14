from django import forms
from phone_field.forms import PhoneNumber
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,label="", widget=forms.TextInput(attrs={'placeholder': 'kullanıcı adı'}))
    password = forms.CharField(max_length=30,label="",widget=forms.PasswordInput(attrs={'placeholder':'parola'}))
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30,label="", widget=forms.TextInput(attrs={'placeholder': 'kullanıcı adı'}))
    password = forms.CharField(max_length=30,label="",widget=forms.PasswordInput(attrs={'placeholder':'parola'}))
    confirm = forms.CharField(max_length=30,label="",widget=forms.PasswordInput(attrs={'placeholder':'parolayı tekrarla'}))
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if confirm and password and confirm != password:
            raise forms.ValidationError("parolalar eşleşmiyor")

        values = {
            "username":username,
            "password":password
        }
        return values
CHOICES = [(None, 'ÜLKE'),('Türkiye', 'Türkiye'),
 ('Bangladesh', 'Bangladesh'),
 ('UK', 'UK'),
  ('United States', 'United States'),
  ('Canada', 'Canada'), 
  ('Dubai', 'Dubai')]
phone_regex = RegexValidator(
        regex=r'^[Z0-9]*$',
        message='Lütfen geçerli bir telefon numarası giriniz'
    )
class İnfoForm(forms.Form):
    adress_name = forms.CharField(max_length=30,label="", widget=forms.TextInput(attrs={'placeholder': 'adres ismi'}))
    name = forms.CharField(max_length=30,label="", widget=forms.TextInput(attrs={'placeholder': 'isim'}))
    surname = forms.CharField(max_length=30,label="", widget=forms.TextInput(attrs={'placeholder':'soyisim'}))
    adress = forms.CharField(max_length=30,label="", widget=forms.TextInput(attrs={'placeholder': 'adres'}))
    tel_no = forms.CharField( validators=[phone_regex],label="",min_length=11, max_length=11,widget=forms.TextInput(attrs={'placeholder': 'telefon numarası'}))
    email = forms.EmailField(max_length=30,label="", widget=forms.EmailInput(attrs={'placeholder': 'e-mail'}))
    country = forms.ChoiceField(label="",choices=CHOICES,)
    city = forms.CharField(max_length=30,label="", widget=forms.TextInput(attrs={'placeholder': 'şehir'}))
    post_code = forms.CharField(max_length=30,label="", widget=forms.TextInput(attrs={'placeholder':'posta kodu'}))
