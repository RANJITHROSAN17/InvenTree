"""
Provide templates for the various model status codes.
"""

from django import template
from django.utils.safestring import mark_safe
from InvenTree.status_codes import PurchaseOrderStatus, SalesOrderStatus
from InvenTree.status_codes import StockStatus, BuildStatus

register = template.Library()


@register.simple_tag
def purchase_order_status(key, *args, **kwargs):
    return mark_safe(PurchaseOrderStatus.render(key))


@register.simple_tag
def sales_order_status(key, *args, **kwargs):
    return mark_safe(SalesOrderStatus.render(key))


@register.simple_tag
def stock_status(key, *args, **kwargs):
    return mark_safe(StockStatus.render(key))


@register.simple_tag
def build_status(key, *args, **kwargs):
    return mark_safe(BuildStatus.render(key))


@register.simple_tag
def sales_order_codes(*args, **kwargs):
    print("doing")
    return "hello world"