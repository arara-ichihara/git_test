from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect
from django.utils import timezone
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html' # デフォルトのものから名前修正してる
    context_object_name = 'latest_question_list' # デフォルトのものから名前修正してる
    model = Question #ねんのため定義しておく
    
    def get_queryset(self):
        # https://qiita.com/dai-takahashi/items/7d0187485cad4418c073
        # この関数で元々用意されているget_querysetを上書き(オーバーライド)して取得するデータを加工できる。どこにreturnするとか考えなくていい。
        """Return the last five published questions."""
       #  return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now() # 書き方決まってる'https://codelab.website/django-queryset-filter/'
        ).order_by('-pub_date')[:5]
    # def get_queryset(self):
    #   return Question.objects.all()
    # これがmodel = Questionの代わりになる。https://hombre-nuevo.com/python/python0057/
    # 条件つけてるからこの方法じゃないといけない

class DetailView(generic.DetailView): #generic.DetailViewの子クラス、#detailviewは詳細ページ用の既存view
    model = Question # model = Question.objects.all()と同じ。Questionテーブルを選択
    template_name = 'polls/detail.html'  # デフォルトのものから名前修正してる
    # modelの小文字(question)がQuestionから自動生成されてdeltail.htmlに渡される!!!!!


class ResultsView(generic.DetailView): #detailviewは詳細ページ用の既存view
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # questionにQuestionのオブジェクトの中の主キーがquestion_idの列をぶち込むつまり選択した設問になる
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # selected_choiceに選択した質問の中のどのchoiceをしたかをpkにいれて取得する
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        # models.pyで定義したchoiceのvoteFieldにアクセスしてupdateする(DBいじる感じ)
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        return redirect('polls:results', question.id,)