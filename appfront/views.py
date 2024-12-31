from django.shortcuts import render
from phonenumbers import PhoneNumber
import qrcode
import qrcode.image.svg
# from io import BytesIO
from appfront.functions import generate_number, make_qr_code
from mimesis.locales import Locale


dct_locale = {i.name: i.value for i in Locale}


def index(request):
    data = {
        'dct_locale': dct_locale
    }
    if request.GET.get('countryCode'):
        data['country_code'] = request.GET.get('countryCode')
        # data['quantity'] = request.GET.get('quantity')
        list_of_phonenumbers: PhoneNumber = generate_number(request.GET.get('countryCode'))
        data['phone_number'] = list_of_phonenumbers
        img_qr = make_qr_code(text=list_of_phonenumbers.national_number)
        # stream = BytesIO()
        # img_qr.save(stream)
        # data['svg'] = stream.getvalue().decode()
        data['svg'] = img_qr

    return render(request, 'appfront/index.html', data)

