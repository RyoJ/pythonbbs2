from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return render(request, 'bbs/index.html')#テンプレート(htmlファイル)を呼び出すショートカット関数
    context = {
        'message': 'Welcome my BBS',
        'players': ['勇者', '戦士', '魔法使い', '忍者']
    }
    return render(request, 'bbs/index.html', context)
    
def index2(request):
    #return render(request, 'bbs/index.html')#テンプレート(htmlファイル)を呼び出すショートカット関数
    context = {
        'message2': 'Welcome my BBS2',
        'player2s': ['勇者2', '戦士2', '魔法使い22', '忍者2']
    }
    return render(request, 'bbs/index.html', context)