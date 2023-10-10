from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    # ModelForm : 모델과 연결된 폼 -> 연결된 모델의 데이터 저장 가능
    # -> 이너클래스인 Meta클래스 필요
    class Meta:
        # 사용 할 모델과 모델의 속성을 명시.
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }  