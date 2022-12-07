from django.shortcuts import render
from .models import PatientDetails
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
from django.http import HttpResponse
import json 
from django.template.loader import render_to_string

ITEM_PER_PAGE = 5
# Create your views here.
def patient_list(request):
    patients = PatientDetails.objects.all().order_by('id')
    page = request.GET.get('page',1)
    search_key = request.GET.get('search_key')
    if search_key:
        patients = patients.filter(first_name__icontains=search_key)
    paginator = Paginator(patients, ITEM_PER_PAGE)
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        patients = paginator.page(paginator.num_pages)

    context = {
        'patients': patients
    }
    if request.is_ajax():
        response_data = {}
        response_data['page_content'] = render_to_string('patient_detail_table.html', context)
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render(request, "patient_list.html",context)