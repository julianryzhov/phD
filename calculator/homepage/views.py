from django.shortcuts import render
import math

# Create your views here.


def index(request):
    template = 'homepage/index.html'
    return render(request, template)


def ET(request):
    template = 'homepage/ET.html'
    return render(request, template)


def OPU_plasma(request):
    template = 'homepage/OPU_plasma.html'
    return render(request, template)


def OPU_ff(request):
    template = 'homepage/OPU_ff.html'
    return render(request, template)


def process_data_ET(request):
    template = 'homepage/result.html'
    if request.method == 'POST':
        leptin = request.POST.get('leptin')
        ghrelin = request.POST.get('ghrelin')
        adiponectin = request.POST.get('adiponectin')
        leptin = float(leptin)
        ghrelin = float(ghrelin)
        adiponectin = float(adiponectin)
        const = -22.9165
        lep_const = -1.2482
        ghr_const = 2.1816
        adipo_const = -3.9672
        result_math = 1/(
            1 + math.e ** -(const + lep_const * leptin + ghr_const * ghrelin + adipo_const * adiponectin))
        result = round(result_math * 100, 2)
        return render(request, template, {'result': result})


def process_data_OPU_plasma(request):
    template = 'homepage/result.html'
    if request.method == 'POST':
        leptin = request.POST.get('leptin')
        adiponectin = request.POST.get('adiponectin')
        leptin = float(leptin)
        adiponectin = float(adiponectin)
        const = -3.6187
        lep_const = -1.6524
        adipo_const = 16.7346
        result_math = 1/(1 + math.e ** -(const + lep_const * leptin + adipo_const * adiponectin))
        result = round(result_math * 100, 2)
        return render(request, template, {'result': result})


def process_data_OPU_ff(request):
    template = 'homepage/result.html'
    if request.method == 'POST':
        leptin = request.POST.get('leptin')
        ghrelin = request.POST.get('ghrelin')
        leptin = float(leptin)
        ghrelin = float(ghrelin)
        const = -6.1612
        lep_const = 0.6656
        ghr_const = -1.2842
        result_math = 1/(1 + math.e ** -(const + lep_const * leptin + ghr_const * ghrelin))
        result = round(result_math * 100, 2)
        return render(request, template, {'result': result})
