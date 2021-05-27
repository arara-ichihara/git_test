from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # detailViewの場合pkの数字でレコードの特定がされる。だからこれがデフォルト。intは正規表現でintじゃないと受け付けない。https://qiita.com/dai-takahashi/items/7d0187485cad4418c073
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # 整数がマッチした場合、viewsのintegerの引数にvalue(pk)を代入
    path('<int:question_id>/vote/', views.vote, name='vote'),
]