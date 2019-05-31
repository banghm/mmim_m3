from django.shortcuts import render, Http404, redirect, HttpResponse
from django.urls import reverse
from .models import *
from .forms import *
# from django.conf import settings
# Create your views here.
from django.template import RequestContext


def index(request):
    #print(request.session['isLogin'])
    if request.session.get('isLogin', 'false') == 'false':
        return redirect('/elections/login/')
        
    print(request.session['isLogin'])
    return render(request, 'elections/main.html')

def logout(request):
    request.session.flush()
    return redirect('/elections/login/')

def login(request):
    if request.method == 'POST':
        id = request.POST.get('username')
        pw = request.POST.get('password')

        try:
            user = MMIM.objects.get(user_id=id)
            u_pw = user.user_pw
            if u_pw == pw:
                request.session['isLogin'] = 'true'
                request.session['id'] = user.id # 식별자
                request.session['name'] = user.name
                return redirect('/elections/index/')
            else:
                raise Http404("비밀번호가 맞지 않습니다.")

        except Exception as e:
            raise Http404('해당 아아디는 등록되지 않았습니다.')
        
    if request.session.get('isLogin', 'false') == 'true':
        return HttpResponse('이미 로그인 중입니다.')

    return render(request, 'elections/login.html', {})

def register(request):
    if request.method == 'POST':
        print(request.POST.keys(), 'hello')
        name = request.POST.get('name')
        user_id = request.POST.get('id')
        user_pw = request.POST.get('pw')
        adr1 = request.POST.get('zip_h_1') + request.POST.get('zip_h_2')
        pn = request.POST.get('cel2_1')
        jm = request.POST.get('jumin')
        choice = request.POST.get('job')

        MMIM.objects.create(
            name=name,
            user_id=user_id,
            user_pw=user_pw,
            adr1=adr1,
            pn=pn,
            jm=jm,
            choice=choice
        )
        return redirect('/elections/login/')

    if request.session.get('isLogin', 'false') == 'true':
        return HttpResponse('이미 회원가입을 하셨습니다.')

    return render(request, 'elections/join.html', {})

def Contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
    
        return redirect(reverse('elections:show-contract', kwargs={ 'p_id' :form.cleaned_data['employer'].id, 'id' : form.cleaned_data['employee'].id }))

    if request.session.get('isLogin', 'false') == 'false':
        return redirect('/elections/login/')

    form = ContractForm()
    return render(request, 'elections/gyeyagseo.html', {'form' : form})

def showContract(request, p_id, id):
    a = MMIM.objects.get(pk=p_id)
    b = MMIM.objects.get(pk=id)
    c = contract.objects.get(employer=a, employee=b)
    print(a, b, c)
    return render(request, 'elections/jaksungsuccess.html', {'c' : c})

def showMyContract(request):
    user = MMIM.objects.get(id=request.session['id'])
    if user.choice == '40':
        datas = contract.objects.filter(employer=user)
    elif user.choice == '39':
        datas = contract.objects.filter(employee=user)
    return render(request, 'elections/inquiry.html', {'datas' : datas})

def page_not_found_view(request):
    return render(request, 'page_not_found.html', RequestContext(request))
