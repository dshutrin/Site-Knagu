from django import forms
from .models import *

class AddPostForm(forms.Form):
	score = forms.ChoiceField(label='Счёт', choices=(
								('не изменять', ('не изменять')),
								(0, (0)),
    							(1, (1)),
    							(2, (2)),
    							(3, (3)),
    							(4, (4)),
    							(5, (5)),
    							(6, (6)),
    							(7, (7)),
    							(8, (8)),
    							(9, (9)),
    							(10, (10))
							)
	)
