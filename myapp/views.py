# from  django.shortcuts import render
# #Function based views

# def moviesInfo(request):

# 	my_dict={'head_msg':'Movies Information',
# 	'sub_msg1':'Siva Karthikeyan\'s parasakthi releasing soon',
# 	'sub_msg2':'Bahubali-3 is just planning',
# 	'sub_msg3':'Salman Khan ready to marriage',
# 	'img1':'images/movie.jpg',
# 	}
# 	return render(request,'movie.html',context=my_dict)


# def sportsInfo(request):
# 	my_dict={'head_msg':'Sports Information',
# 	'sub_msg1':'Actor ajith kumar in motorsports',
# 	'sub_msg2':'Kohli updating in game anything can happend',
# 	'sub_msg3':'Best Performance by India-Sehwag',
# 	'img1':'images/car1.jpg',
# 	}
# 	return render(request,'movie.html',context=my_dict)

# def politicsInfo(request):
# 	my_dict={'head_msg':'Politics Information',
#     'sub_msg1':'tamilnadu assembly election soon',
# 	'sub_msg2':'Rupee Value now 1$:70Rs',
# 	'sub_msg3':'In India Single Paisa Black money No more',
# 	'img1':'images/poly.jpg',
# 	}
# 	return render(request, 'movie.html', context=my_dict)

# def index(request):
# 	context = {
# 		'head_msg': 'Welcome Page',
# 		'sub_msg1': 'Movies | Sports | Politics',
# 		'sub_msg2': 'Choose category from menu',
# 		'sub_msg3': 'Latest updates available',
# 		'img1':'images/car.jpg',
# 	}
# 	return render(request, 'movie.html', context)


# from  django.shortcuts import render
# def index(request):
#     name = {'firstname': 'MYSTUDENTS',
#             'course':'python',
#             'age':16,
#             'mark':98}
#     return render(request, 'index.html', name)


# from  django.shortcuts import render
# def index(request):
#     view_students = [
#         {'name': 'rani', 'age': 17},
#         {'name': 'raja', 'age': 18},
#         {'name': 'ravi', 'age': 16},
#         {'name': 'renu', 'age': 17},
        
#     ]

#     return render(request, 'index.html', context={'students':view_students })



from  django.shortcuts import render
def home(request):
	return render(request, 'homepage.html')

def product(request):
	mobile = int(request.POST['mobile'])
	keyboard = int(request.POST['keyboard'])
	monitor = int(request.POST['monitor'])
	price = mobile + keyboard + monitor
	context = {'Price': price}

	return render(request, 'result.html', context)