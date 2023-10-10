from django.urls import path
from . import views

# url 네임스페이스
app_name = 'pybo'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name = 'answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]

# localhost:8000/pybo/ 이후에 들어올 값에 따른 매핑 
# localhost:8000/pybo/ 까지만 입력하는 경우 views.py의 index 함수 실행
# name = 'index' : http://localhost:8000/pybo/ 의 url은 'index'라는 별칭부여
'''
def index(request):
question_list = Question.objects.order_by('-create_date')
context = {'question_list' : question_list}
return render(request, 'pybo/question_list.html', context)
'''
#  index 함수 : 요청이 들어오는 경우 질문목록을 정렬한 값 및 question_list.html을 반환


