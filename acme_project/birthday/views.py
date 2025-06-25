from django.shortcuts import render

from .forms import BirthdayForm
from .utils import calculate_birthday_countdown

def birthday(request):
    form = BirthdayForm(request.GET or None)
    if form.is_valid():
        pass
    context = {'form': form}
    if form.is_valid():
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context)