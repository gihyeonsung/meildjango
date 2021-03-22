from django import template
from django.utils import timezone

register = template.Library()


@register.filter(expects_localtime=True)
def humanizeTimedelta(timedelta: timezone.timedelta):
    """
    humanize timedelta in korean to string
    """
    secs = timedelta.total_seconds()
    if secs < 60:
        return f'{secs}초'

    mins = int(secs // 60)
    if mins < 60:
        return f'{mins}분'

    hours = int(mins // 60)
    if hours < 24:
        return f'{hours}시간'

    days = int(hours // 24)
    return f'{days}일'
