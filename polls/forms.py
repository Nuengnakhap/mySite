from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from polls.models import Poll


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('%(value)s ไม่ใช่เลขคู่', params={'value': value})


class PollForm(forms.Form):
    title = forms.CharField(label="ชื่อโพล", max_length=100, required=True)
    email = forms.CharField(validators=[validators.validate_email])
    no_questions = forms.IntegerField(label="จำนวนคำถาม", min_value=0, max_value=10,
                                      required=True, validators=[validate_even])
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def clean_title(self):
        data = self.cleaned_data['title']

        if "ไอทีหมีแพนด้า" not in data:
            raise forms.ValidationError("คุณลืมชื่อคณะ")

        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and not end:
            # raise forms.ValidationError("โปรดเลือกวันสิ้นสุด")
            self.add_error('end_date', "โปรดเลือกวันสิ้นสุด")
        elif not start and end:
            # raise forms.ValidationError("โปรดเลือกวันเริ่มต้น")
            self.add_error('start_date', "โปรดเลือกวันเริ่มต้น")


class PollModelForm(forms.ModelForm):
    email = forms.CharField(validators=[validators.validate_email])
    no_questions = forms.IntegerField(label="จำนวนคำถาม", min_value=0, max_value=10,
                                      required=True, validators=[validate_even])

    class Meta:
        model = Poll
        exclude = ['del_flag']

    def clean_title(self):
        data = self.cleaned_data['title']

        if "ไอทีหมีแพนด้า" not in data:
            raise forms.ValidationError("คุณลืมชื่อคณะ")

        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and not end:
            # raise forms.ValidationError("โปรดเลือกวันสิ้นสุด")
            self.add_error('end_date', "โปรดเลือกวันสิ้นสุด")
        elif not start and end:
            # raise forms.ValidationError("โปรดเลือกวันเริ่มต้น")
            self.add_error('start_date', "โปรดเลือกวันเริ่มต้น")

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField()
#     sender = forms.EmailField()
#     recipients =
