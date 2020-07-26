from django.db import models


class CommonMailingList(models.Model):
    """Рассылка на общие материалы с сайта"""
    email = models.CharField('Email подаписчика', max_length=50)
    
    class Meta:
        db_table = 'common_mailing_list'

class CaseMailingList(models.Model):
    """Рассылка на материалы конкретного дела"""
    email = models.CharField('Email подаписчика', max_length=50)
    case = models.ForeignKey(to='cases.Case', verbose_name='Дуло', on_delete=models.CASCADE)    
    class Meta:
        db_table = 'case_mailing_list'