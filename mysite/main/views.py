from django.shortcuts import render
from .models import Team, Step, Sub
from .forms import AddPostForm
from django.forms import formset_factory

# Create your views here.
def admin_panel(request, admin_id):
	teams = Team.objects.order_by('id')
	steps = Step.objects.order_by('id')

	FormTeamplate = formset_factory(AddPostForm, extra=len([x for x in teams]))
	form = FormTeamplate()


	if request.method == 'POST':

		form = FormTeamplate(request.POST)
		admin_num = int(str(request).replace('<WSGIRequest: POST \'/admin', '', 1)[0])
		scores = [x['score'] for x in FormTeamplate(request.POST).cleaned_data]

		if admin_num == 1:
			for i in range(len(teams)):
				if scores[i].isdigit():
					team = Team.objects.get(title=teams[i].title)
					team.step_1_score = scores[i]
					team.save()

		elif admin_num == 2:
			for i in range(len(teams)):
				if scores[i].isdigit():
					team = Team.objects.get(title=teams[i].title)
					team.step_2_score = scores[i]
					team.save()

		elif admin_num == 3:
			for i in range(len(teams)):
				if scores[i].isdigit():
					team = Team.objects.get(title=teams[i].title)
					team.step_3_score = scores[i]
					team.save()

		elif admin_num == 4:
			for i in range(len(teams)):
				if scores[i].isdigit():
					team = Team.objects.get(title=teams[i].title)
					team.step_4_score = scores[i]
					team.save()

		elif admin_num == 5:
			for i in range(len(teams)):
				if scores[i].isdigit():
					team = Team.objects.get(title=teams[i].title)
					team.step_5_score = scores[i]
					team.save()

		elif admin_num == 6:
			for i in range(len(teams)):
				if scores[i].isdigit():
					team = Team.objects.get(title=teams[i].title)
					team.step_6_score = scores[i]
					team.save()

			value = Sub.objects.get(id=1)
			value.value = True
			value.save()


		teams = Team.objects.order_by('id')
		for team in teams:
			summ = 0
			summ += team.step_1_score * (Step.objects.get(id=1).coef / 100)
			summ += team.step_2_score * (Step.objects.get(id=2).coef / 100)
			summ += team.step_3_score * (Step.objects.get(id=3).coef / 100)
			summ += team.step_4_score * (Step.objects.get(id=4).coef / 100)
			summ += team.step_5_score * (Step.objects.get(id=5).coef / 100)
			summ += team.step_6_score * (Step.objects.get(id=6).coef / 100)

			team.all_score = summ
			team.save()


	if request.method == 'POST':
		admin_num = int(str(request).replace('<WSGIRequest: POST \'/admin', '', 1)[0])
	if request.method == 'GET':
		admin_num = int(str(request).replace('<WSGIRequest: GET \'/admin', '', 1)[0])


	teams = Team.objects.order_by('id')
	out_scores = []
	if admin_num == 1:
		out_scores = [f'(текущее: {x.step_1_score})' for x in teams]
	if admin_num == 2:
		out_scores = [f'(текущее: {x.step_2_score})' for x in teams]
	if admin_num == 3:
		out_scores = [f'(текущее: {x.step_3_score})' for x in teams]
	if admin_num == 4:
		out_scores = [f'(текущее: {x.step_4_score})' for x in teams]
	if admin_num == 5:
		out_scores = [f'(текущее: {x.step_5_score})' for x in teams]
	if admin_num == 6:
		out_scores = [f'(текущее: {x.step_6_score})' for x in teams]


	names = []
	for i in range(len(teams)):
		names.append(f'{teams[i].title} {out_scores[i]}')


	if (6 >= int(admin_id) > 0):
		data = {'body' : f'{admin_id}', 'form' : form, 'names' : names}
		return render(request, 'main/admin_panel.html', data)
	else:
		return render(request, 'main/error_admin_page.html')


def home(request):
	posts = Team.objects.order_by('id')

	step_imgs = [
		'/static/images/plane.png',
		'/static/images/plane.png',
		'/static/images/plane.png',
		'/static/images/plane.png',
		'/static/images/plane.png',
		'/static/images/plane.png'
	]

	for post in posts:

		post.score1 = int(post.score1) * step_imgs[0]
		post.score2 = int(post.score2) * step_imgs[1]
		post.score3 = int(post.score3) * step_imgs[2]
		post.score4 = int(post.score4) * step_imgs[3]
		post.score5 = int(post.score5) * step_imgs[4]
		post.score6 = int(post.score6) * step_imgs[5]

	data = {
		'posts' : posts
	}

	if len([post for post in posts]) > 0:
		return render(request, 'main/home.html', data)
	else:
		return render(request, 'main/null_home.html')


def send_results(request):

	def normalize(text):
		return text.replace(' ', '_')

	#если нажата кнопка результатов на главной
	score = Sub.objects.get(id=1).value

	teams = [team for team in reversed(Team.objects.order_by('all_score'))]

	style = '@keyframes NAME { 0% {padding-left: 0%;} 100% {padding-left: PERCENT%;} }'
	styles = ''

	for i in range(1, len( [x for x in teams] )+1):
		team = Team.objects.get(id=i)
		team.normalized_title = normalize(team.title)
		team.style = style.replace('NAME', normalize(team.title), 1).replace('PERCENT', str((72.96/60)*team.all_score))
		team.save()

		if all([ team.step_1_score, team.step_2_score, team.step_3_score, team.step_4_score, team.step_5_score, team.step_6_score ]):
			styles = f'{styles}\n\n{team.style}'

	if score:
		teams = [team for team in teams]
		scores = [team.all_score for team in teams]
		return render(request, 'main/result_page.html', { 'teams' : teams, 'main_style' : styles, 'names' : [normalize(x.title) for x in teams]})

		return render(request, 'main/result_page.html', { 'names' : ['Результаты еще не подведены!'] })
	
	else:
		return render(request, 'main/null_results.html')
