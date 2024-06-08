from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field

class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        status = data.get('status')
        phone_number = data.get('phone_number')
        gender = data.get('gender')
        if status:
            user_field(user, 'status', status)
        if phone_number:
            user_field(user, 'phone_number', phone_number)
        if gender:
            user_field(user, 'gender', gender)
        return super().save_user(request, user, form, commit=commit)
