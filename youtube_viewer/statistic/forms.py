from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Video

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ('url', 'name', 'min_view', 'max_view', 'thread_view', 'count_view', 'avalible')

        widgets = {
            'tags': CheckboxSelectMultiple(),
        }