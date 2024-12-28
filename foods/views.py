from multiprocessing import context
from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from foods.models import Menu

def index(request):
  context = dict()
  today = datetime.today().date();
  menus = Menu.objects.all()
  context = {"date":today }
  context["menus"] = menus
  return render(request,'foods/index.html',context=context);



def food_detail(request,food):
  context = dict()
  if food == "chicken":
    context["name"] = "코딩에 빠진 닭"
    context["descriptions"] ="주머니가 가벼운 당신의 마음까지 생각한 가격 !"
    context["price"] = 10000;
    context['img_path'] = "foods/images/chicken.jpg"
  elif food == "sushi":
    context["name"] = "코코스시"
    context["descriptions"] ="주머니가 가벼운 당신의 마음까지 생각한 가격 !"
    context["price"] = 10000;
    context['img_path'] = "foods/images/sushi.jpg"
  elif food == "burger":
    context["name"] = "코데리아"
    context["descriptions"] ="주머니가 가벼운 당신의 마음까지 생각한 가격 !"
    context["price"] = 10000;
    context['img_path'] = "foods/images/burger.jpg"
  elif food == "bibimbap":
    context["name"] = "코가네"
    context["descriptions"] ="주머니가 가벼운 당신의 마음까지 생각한 가격 !"
    context["price"] = 10000;
    context['img_path'] = "foods/images/bibimbap.jpg"
  else :
    raise Http404("이런 음식은 없습니다 !")
  return render(request,'foods/detail.html',context=context)