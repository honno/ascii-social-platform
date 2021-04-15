from django.forms import *
from django.contrib.auth.forms import UserCreationForm

from .models import *

__all__ = ["JoinForm", "ArtForm", "CommentForm"]


# ------------------------------------------------------------------------------
# UserCreationForm


class JoinForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


# ------------------------------------------------------------------------------
# ArtForm


class ArtTextarea(Widget):
    template_name = "core/widgets/art_textarea.html"

    def __init__(self, attrs=None):
        default_attrs = {"cols": "80", "rows": "24"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class ArtCharField(CharField):
    widget = ArtTextarea


class ArtForm(ModelForm):
    text = ArtCharField()
    js_enabled = BooleanField(required=False, widget=HiddenInput)
    description = CharField(required=False, widget=Textarea)

    class Meta:
        model = Art
        fields = ["title", "text", "description", "thumb_x_offset", "thumb_y_offset"]

    class Media:
        js = ["core/art_form.js"]

    def clean(self):
        data = super().clean()

        if data.get("js_enabled", False):
            # potential problem:
            # 1. dot purposely added as the first char
            # 2. script to prepend dot didn't work
            # 3. ???
            # 4. GOODBYE DOT
            if data["text"][0] == ".":
                data["text"] = data["text"][1:]

        return data


# ------------------------------------------------------------------------------
# CommentForm


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
