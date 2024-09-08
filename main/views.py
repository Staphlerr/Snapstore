from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Ayam Geybok Bang Bang',
        'price': '82.000',
        'description': 'Ayam pake mozzarella pedes gila huh hah',
        'rating': '9,7/10',
        'date': '8 Agustus 2024',
    }

    return render(request, "product.html", context)
