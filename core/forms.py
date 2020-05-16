from django import forms
from django.forms import formset_factory
from django.template.defaultfilters import mark_safe


class ParserForm(forms.Form):
    url = forms.CharField(required=True, max_length=200,
                          # label=mark_safe('<strong>Скопируйте ссылку с youtube</strong>'),
                          widget=forms.TextInput(
                              attrs={'class': 'form-control long-input', 'placeholder': 'https://www.youtube.com/watch...',
                                     'pattern': 'https://.+you.+'}),
                          label_suffix=':')
    # content = forms.CharField(required=True, label=mark_safe('<strong>Введите запросы</strong>'),
    #                           widget=forms.Textarea(
    #                               attrs={'class': 'form-control',
    #                                      'placeholder': 'Каждый запрос с новой строки', 'rows': '6', 'cols': '6'}))
    # google = forms.BooleanField(required=False, initial=True, label=mark_safe('<strong>Google</strong>'))
    # yandex = forms.BooleanField(required=False, label=mark_safe('<strong>Yandex</strong>'))

    # def __init__(self, *args, **kwargs):
    #     super(ParserForm, self).__init__(*args, **kwargs)
    #     self.fields['content'].label = 'Запросы'
    #     self.fields['url'].label = 'url'
    #     self.fields['google'].widget.attrs.update({'style': 'display: inline;'})
    #     self.fields['yandex'].widget.attrs.update({'style': 'display: inline;'})

class ContactForm(forms.Form):
    user = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = 'Имя'
        self.fields['content'].label = 'Сообщение'
        self.fields['content'].help_text = 'Напишите своё сообщение'

        # self.fields['date'].label = 'Дата доставки'
        # self.fields['date'].help_text = 'Доставка производиться на следующий день после оформления заказа. Менеджер с Вами свяжится'
        # self.fields['date'].widget.attrs['class'] = 'help-text-class help-text-other'

    # content.widget.attrs.update({'style': 'width: 70vh; display: inline; margin-right: 1px;', 'class': 'date-widget'})
