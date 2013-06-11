from django import forms
from django.conf import settings


class NSAForm(forms.Form):
    user = forms.CharField(required=True)
    passwd = forms.CharField(required=True,
                           widget=forms.fields.PasswordInput)

    def clean(self):
        cleaned_data = super(NSAForm, self).clean()
        user = cleaned_data.get('user', None)
        passwd = cleaned_data.get('passwd', None)

        if user != "nsa":
            self._errors["user"] = self.error_class(["Wrong username."])

        if passwd != "nsa":
            self._errors["passwd"] = self.error_class(["Wrong password."])

        return cleaned_data
