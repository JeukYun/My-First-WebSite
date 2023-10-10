from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm


def index(request):
    question_list = Question.objects.order_by('-create_date')
    # '-create_date' 앞에 '-' 있는경우 역방향, 없으면 순방향 정렬
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid(): # 폼이 유효한 경우
            question = form.save(commit=False) # question 객체에 임시 저장
            question.create_date = timezone.now() # 작성일시 저장
            question.save() # 데이터 실제로 저장
            return redirect('pybo:index')
    else:
        form = QuestionForm() # 제목, 내용입력을 하지 않은 경우
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)