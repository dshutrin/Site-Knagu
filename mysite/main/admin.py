from django.contrib import admin
from .models import Team, Step, Sub

# Register your models here.
class TableAdmin(admin.ModelAdmin):
	list_display = ('title', 'score1', 'score2', 'score3', 'score4', 'score5', 'score6')
	list_display_links = ('title', 'score1', 'score2', 'score3', 'score4', 'score5', 'score6')
	search_fields = ('title', )
	exclude = ('step_1_score', 'step_2_score', 'step_3_score', 'step_4_score', 'step_5_score', 'step_6_score', 'all_score', 'style', 'normalized_title')

class TableStep(admin.ModelAdmin):
	list_display = ('id', 'coef')
	list_display_links = ('coef', )

class TableSub(admin.ModelAdmin):
	list_display = ('value', )
	#exclude = ('value', )

admin.site.register(Team, TableAdmin)
admin.site.register(Step, TableStep)
admin.site.register(Sub, TableSub)