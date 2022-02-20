from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from accounts.models import User


SUGGESTION_STATES = [
    
    ('invalid', 'INVÁLIDO'),
    ('reject', 'RECUSADO'),
    ('loading', 'EM ANDAMENTO'),
    ('accept', 'ACEITO'),
    
]



class CategorySuggestion(Model):
    name = CharField(max_length=50, verbose_name='Nome')
    state = CharField(max_length=256, choices=SUGGESTION_STATES, verbose_name='Estado:')
    user = ForeignKey(User, on_delete=RESTRICT, verbose_name='Usuário')


class SubCategorySuggestion(Model):
    name = CharField(max_length=50, verbose_name='Nome')
    state = CharField(max_length=256, choices=SUGGESTION_STATES, verbose_name='Estado:')
    user = ForeignKey(User, on_delete=RESTRICT, verbose_name='Usuário')