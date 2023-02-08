from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


monthly_tasks = {
    "january": "A hard nut to crack",
    "february": "All ears",
    "march": "A picture is worth a thousand words",
    "april": None,
    "may": "Better late than never",
    "june": "Born with a silver spoon in mouth",
    "july": None,
    "august": "Break the ice",
    "september": "Break a leg",
    "octomber": "Can judge a book by its cover",
    "november": "Chasing rainbows",
    "december": None
}
# Create your views here.


def show_month_list(request):
    months = list(monthly_tasks.keys())
    return render(request, "challenges/index.html", {
        "activity_list": months
    })


def month_number_handler(request, month):
    if abs(month) <= 12:
        chosen_month = list(monthly_tasks.keys())[month - 1]
        generated_correct_url = reverse(
            "month_handle_page", args=[chosen_month])
        return HttpResponseRedirect(generated_correct_url)
    else:
        raise Http404()


def month_handle(request, month):
    month_activity = None
    if month.lower() in monthly_tasks.keys():
        month_activity = monthly_tasks[month.lower()]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "activity": month_activity
        })
    else:
        raise Http404()
