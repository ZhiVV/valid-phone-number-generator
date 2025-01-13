from collections import namedtuple


LocaleData = namedtuple('LocaleData', ['country_name', 'mask', 'country_code'])


EXTRA_LOCALE = {
    "THA": LocaleData('Thailand', '+66 # ### ####', '+66'),
    "VNM": LocaleData('Vietnam', '+84 ### ### ###', '+84'),
    "IDN": LocaleData('Indonesia', '+62 ### #### ####', '+62'),
}


