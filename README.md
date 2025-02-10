## Description
The application generates a phone number using the python library ["Mimesis"](https://mimesis.name/) (fake data generator for Python). Then validates the received number using the library ["Phonenumbers"](https://github.com/daviddrysdale/python-phonenumbers) (Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.).
If the number is valid, it is shown on the screen. The "Copy" and "QR code" buttons use a phone number without a "+" and a country code.
If the 100 generated numbers are not valid from the point of view of the "Phonenumbers" library, the last number will be displayed, but it will not be valid and highlighted in red. As an example, Estonia (ET code).
The user interface is made using the [WebSim](https://websim.ai/) AI-powered platform

## Installation
Installation of the application depends on the server on which it will be deployed. Each hoster has its own specifics. 
For hosting PythonAnyWhere, you can use these [instructions](https://pressanybutton.ru/post/poleznye-instrumenty/razvorachivanie-django-proekta-na-pythonanywhere/) (in Russian). 
You can see the working application at the url - [validphonegenerator.eu.pythonanywhere.com](https://validphonegenerator.eu.pythonanywhere.com/)

## Technology
Python, Django

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
