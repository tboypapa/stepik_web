from django import forms
from .models import Question, Answer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class SignupForm(forms.Form):
    username = forms.CharField(required=False, max_length=100)
    email = forms.EmailField(required=False)
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Введите имя пользователя')

        try:
            User.objects.get(username=username)
            raise forms.ValidationError('Такое имя пользователя занято')
        except User.DoesNotExist:
            pass

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Введите адрес электронной почты')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Введите пароль')

        self.raw_passord = password
        return make_password(password)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(required=False, max_length=100)
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Введите имя пользователя')

        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Введите пароль')

        return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                raise forms.ValidationError('Неверное имя пользователя или пароль')

        if not user.check_password(password):
            raise forms.ValidationError('Неверное имя пользователя или пароль')


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean_question(self):
        question_id = int(self.cleaned_data['question'])
        self.cleaned_data['question'] = question_id
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise forms.ValidationError(u'Вопрос не найден', code='ques_404')
        return question

    def clean(self):
        pass

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer
