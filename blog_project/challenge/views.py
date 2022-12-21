from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

challenge_bulanans = {
    "januari": "Belajar python dengan lancar!",
    "februari": "Lancar belajar django!",
    "maret": "Berhasil mengerjakan project sungguhan!",
    "april": "Project 1 success!",
    "mei": "Project 2 success!",
    "juni": "Project 3 success!",
    "juli": "Project 4 success!",
    "agustus": "Project 5 success!",
    "september": "Project 6 success!",
    "oktober": "Project 7 success!",
    "november": "Project 8 success!",
    "desember": None,
}
# Create your views here.

def index(request):
    bulans = list(challenge_bulanans.keys())

    return render(request, "challenge/index.html", {
        "bulans": bulans
    })
    # for bulan in bulans:
    #     capitalize_bulan = bulan.capitalize()
    #     bulan_path = reverse("tantangan-bulanan", args=[bulan])
    #     list_items += f"<li><a href=\"{bulan_path}\">{capitalize_bulan}</a></li>"

    # #"<li><a href="....">Januari</a></li><li><a href="....">Februari</a></li>...........
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

def challenge_bulanan_by_number(request, bulan):
    bulans = list(challenge_bulanans.keys())

    if bulan > len(bulans):
        return HttpResponseNotFound("<h1>Invalid Bulan</h1>")

    redirect_bulan = bulans[bulan - 1]
    redirect_path = reverse("tantangan-bulanan", args=[redirect_bulan]) # /blog/januari
    return HttpResponseRedirect(redirect_path)

def challenge_bulanan(request, bulan):
    try:
        challenge_text = challenge_bulanans[bulan]
        return render(request, "challenge/challenge.html", {
            "text": challenge_text,
            "nama_bulan": bulan
        })
    except:
        raise Http404()