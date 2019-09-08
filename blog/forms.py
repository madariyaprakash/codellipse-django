from django import forms
from .models import Post, Comment, AskQuestion
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostCreateForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'status',
            'banner',
        ]


# class PostBannerForm(forms.ModelForm):
#     class Meta:
#         model = PostBanner
#         fields = ['image']


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'status',
        ]

class PostCommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder': 'Text goes here..',
        'rows':'2',
        'cols':'50',
    }))
    class Meta:
        model = Comment
        fields = [
            'content',
        ]


class AskQuestionCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = AskQuestion
        fields = [
            'title',
            'description',
            'status',
        ]
        # We can also write in this way to change the label of the form
        # labels = {
        #     "aq_title":"Title",
        #     "aq_description" : "Description",
        #     "aq_status":"Status"
        # }

class AskQuestionEditForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = AskQuestion
        fields = [
            'title',
            'description',
            'status',
        ]
        