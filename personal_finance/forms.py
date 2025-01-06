from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .constant import GENDER_TYPE
from django import forms
from .models import PersonalBankAccount, AccountHolderAddress


class UserForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.CharField(max_length=10, choices=GENDER_TYPE)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1' 'password2', 'first_name',
                  'last_name', 'email', 'birth_date', 'account_type',
                  'gender', 'address', 'city', 'postal_code', 'country']

    def data_save(self, commit=True):
        bank_user = super().save(commit=False)

        if commit == True:
            bank_user.save()
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            address = self.cleaned_data.get('address')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')

            AccountHolderAddress.objects.create(
                user=bank_user,
                gender=gender,
                postal_code=postal_code,
                address=address,
                city=city,
                country=country,
            )
            PersonalBankAccount.objects.create(
                user=bank_user,
                account_type=account_type,
                gender=gender,
                birth_date=birth_date,
                account_no=10000+bank_user.id
            )

        return bank_user
