# coding=utf-8
from django.views.generic import DetailView
from .models import Receipt


class ReceiptView(DetailView):
	model = Receipt
