from base.models import Message
from django.forms import ModelForm


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
