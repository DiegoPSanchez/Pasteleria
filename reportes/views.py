from django.http import JsonResponse
from django.views.generic import ListView, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from proceso.models import Pedido
from reportes.forms import ReportForm

class ReportSale(TemplateView):
    model = Pedido
    template_name = 'reportes.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Pedido.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha__range = [start_date, end_date])
                for s in search:
                    data.append(s.toJSON)
            else:
                data['error'] = 'Ha ocurrido un errorx'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title']='Reporte de Ventas'
       context['form']=ReportForm()
       return context