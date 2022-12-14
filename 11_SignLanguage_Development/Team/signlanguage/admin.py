from django.contrib import admin
# Register your models here.
from .models import Result, AiModel, ModelCnt
import json
from django.core.serializers.json import DjangoJSONEncoder
import numpy as np


# 관리에서 Result 객체에 대해  기본 CRUD 관리를 한다.


class Ai_modelAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'is_selected','pub_date')

    def changelist_view(self, request, extra_context=None):
        model_version = AiModel.objects.all().values_list('version')
        model_cnt = ModelCnt.objects.all()
        test = []
        correct_rate_array = []

        test.append(['version', 'cnt'])
        correct_rate_array.append(['version', 'cnt'])
        for i in range(0, len(model_version)):
            temp = []
            correct_rate = []
            case_cnt = model_cnt.filter(version=str(model_version[i][0])).count()
            case_correct_cnt = model_cnt.filter(version=str(model_version[i][0])).filter(equal=True).count()

            temp.append(model_version[i][0])
            temp.append(case_cnt)
            test.append(temp)

            correct_rate.append(model_version[i][0])
            if case_correct_cnt > 0:
                correct_rate.append(int((case_correct_cnt/case_cnt)*100))
            else:
                correct_rate.append(0)
            correct_rate_array.append(correct_rate)

        as_json = json.dumps(list(test), cls=DjangoJSONEncoder)
        extra_context = extra_context or {'chart_data': correct_rate_array, 'chart_data2': as_json}
        return super().changelist_view(request, extra_context)


admin.site.register(Result)
admin.site.register(AiModel,Ai_modelAdmin)
admin.site.register(ModelCnt)