import unittest

# from django.contrib.auth.models import User

from events.forms.comment_form import CommentForm

# user = User.objects.get(pk=42)


# Form test
class TestCommentForm(unittest.TestCase):
    def test_valid_form(self):
        data = {'text': 'Some text'}
        self.form = CommentForm(data=data)
        self.assertTrue(self.form.is_valid())

    def invalid_valid_form_short_text(self):
        data = {'text': 'S'}
        self.form = CommentForm(data=data)
        self.assertFalse(self.form.is_valid())

    def invalid_valid_form_long_text(self):
        data = {'text': 'Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. Some long text above 300 characters. '}
        self.form = CommentForm(data=data)
        self.assertFalse(self.form.is_valid())

