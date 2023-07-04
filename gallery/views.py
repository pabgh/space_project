from django.shortcuts import render



def index(request):

    dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webtelescope.org / NASA / James Webb Space Telescope"},
    2: {"nome": "Nebulosa de Orion",
        "legenda": "nasa.org / NASA / Hubble Space Telescope"},
    }

    return render(request, 'gallery/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'gallery/imagem.html')
