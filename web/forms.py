from django import forms
from .models import Aluguel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column
from crispy_forms.layout import Button
from crispy_forms.layout import Reset

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AluguelForm(forms.ModelForm):

    class Meta:
        model = Aluguel
        fields = ('data_aluguel', 'data_devolucao')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nome = forms.CharField()
    sobrenome = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'nome', 'sobrenome', 'email', 'password1', 'password2']


class ContatoForm(forms.Form):
    emissor = forms.EmailField(required=True, label='Remetente')
    assunto = forms.CharField(required=True)
    msg = forms.CharField(widget=forms.Textarea, label='Mensagem')


    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('emissor', css_class='form-group col-md-6'),
                Column('assunto', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'msg'
        )
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))
