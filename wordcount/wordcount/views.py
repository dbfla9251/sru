from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request,'wordcount/about.html')

def api_count(request):

    #전체문장
    # request.GET.get
    # GET이라는 dictionary에서 키를 입력해주면 값을 가져오는데,
    # 만약 값이 없으면, 두번째 인자로 넘겨준걸 DEFAULT값으로
    full_text = request.GET.get('fulltext', '');
    #총 단어 수 세는 기능 구현
    word_list = full_text.split()
    #각 단어 별로 나온 횟수 세는 기능 구현
    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    print("----")
    print(full_text)


    return JsonResponse({
        'fulltext':full_text,
        'total':len(word_list),
        'dictionary':word_dictionary}, 
    json_dumps_params = {'ensure_ascii': True})

def count(request):
    
    #전체문장
    # request.GET.get
    # GET이라는 dictionary에서 키를 입력해주면 값을 가져오는데,
    # 만약 값이 없으면, 두번째 인자로 넘겨준걸 DEFAULT값으로
    full_text = request.GET.get('fulltext', '');
    #총 단어 수 세는 기능 구현
    word_list = full_text.split()
    #각 단어 별로 나온 횟수 세는 기능 구현
    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    print("----")
    print(full_text)

    return render(request, 'wordcount/count.html',{'fulltext':full_text,'total':len(word_list),'dictionary':word_dictionary.items()})
