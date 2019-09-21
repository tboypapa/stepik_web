from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(**self.cleaned_data)
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
        answer.save()
        return answer
