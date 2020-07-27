from mailchimp3 import MailChimp
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import CommonMailingList, CaseMailingList
from .services import add_email_to_common_mailchimp_list, add_email_to_case_mailchimp_list
def add_to_common_list_view(request):
    """Веб-сервис, добавляющий email в общий лист рассылки""""
    
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'sccess': False, 'message': 'Передайте email'})
    add_email_to_common_mailchimp_list(email=email)
    return JsonResponse({'success'}: True)

def add_to_case_list_view(request):
    """"""
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'sccess': False, 'message': 'Передайте email'})
    case_id = request.GET.get('case_id')
    if not case_id:
        return JsonResponse({'sccess': False, 'message': 'Передайте case_id'})
    add_email_to_case_mailchimp_list(email=email, case_id=case_id)
    return JsonResponse({'success'}:True)
