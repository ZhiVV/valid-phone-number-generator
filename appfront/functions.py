import qrcode
import mimesis
from mimesis import Person
import phonenumbers
from phonenumbers import PhoneNumber
from io import BytesIO
from appfront.config import EXTRA_LOCALE


def make_qr_code(text, border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M):
    qr = qrcode.QRCode(
        version=None,
        error_correction=error_correction,
        image_factory=qrcode.image.svg.SvgPathImage,
        border=border,
        box_size=box_size,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img_qr = qr.make_image()
    stream = BytesIO()
    img_qr.save(stream)
    return stream.getvalue().decode()


def generate_number(locale: str = 'en') -> PhoneNumber:
    extra_locale = False
    try:
        person = Person(locale)
    except mimesis.exceptions.LocaleError:
        print('Used not mimesis locale')
        extra_locale = True
    valid = False
    count = 0
    result = 'empty'

    while not valid:
        count += 1
        print(f'attempt no.{count}')
        if extra_locale:
            mask = EXTRA_LOCALE[locale].mask
            temp_number = Person().phone_number(mask=mask)
        else:
            temp_number = person.phone_number()
        print(f' raw generate number: {temp_number}')
        temp_number = temp_number.replace(" ", "")
        temp_number = temp_number.replace("-", "")
        temp_number = temp_number.replace("(", "")
        temp_number = temp_number.replace(")", "")
        if temp_number[0] != '+':
            print(' no + in number, try again')
            continue
        print(f' number after formating: {temp_number}')
        number_parse = phonenumbers.parse(temp_number, None)
        valid = phonenumbers.is_valid_number(number_parse)
        if valid:
            result = number_parse  # temp_number
        elif count > 100:
            # number_parse.national_number = 0
            number_parse.extension = 'not valid'
            result = number_parse
            valid = True
            print(f' number not valid for E.164, but the number of attempts exceeded')
        else:
            print(f' number not valid for E.164, try again')

    return result
