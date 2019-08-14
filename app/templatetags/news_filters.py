from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    time_now = datetime.now()
    time_now = time_now.timestamp()
    if time_now - value < (60 * 60):
        value = 'Только что'
    elif ((time_now - value) < (60 * 1440)) and ((time_now - value) > (60 * 60)):
        value = '{} часов назад'.format(int((time_now - value) // (60 * 60)))
    elif (time_now - value) > 60 * 1440:
        value = datetime.fromtimestamp(value)
        value = '%s-%s-%s' % (value.year, value.month, value.day)
    return value


@register.filter
def format_score(value):
    if value < -5:
        value = 'Все плохо'
    elif (value > -5) and (value <= 5):
        value = 'Нейтрально'
    elif value > 5:
        value = 'Хорошо'
    return value


@register.filter
def format_num_comments(value):
    if value == 0:
        value = 'Оставьте комментарий'
    elif (value > 0) and (value <= 50):
        value = value
    elif value > 50:
        value = '50+'
    return value


@register.filter
def format_selftext(value, count=5):
    selftext = value.split()
    value = ' '.join(selftext[:count]) + '...' + ' '.join(selftext[-count:])
    return value
