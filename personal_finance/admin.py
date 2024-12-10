from django.contrib import admin
from .models import PersonalBankAccount, AccountHolderAddress

# Register your models here.
admin.site.register(PersonalBankAccount)
admin.site.register(AccountHolderAddress)
