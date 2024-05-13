from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text', 'rate')  # поля, которые вы хотите включить в форму

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)  # получаем продукт из контекста
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(CommentForm, self).save(commit=False)
        instance.product = self.product  # устанавливаем связь с продуктом
        if commit:
            instance.save()
        return instance
