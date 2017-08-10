from .controller import Controller
from pyramid.view import (
    view_config,
    view_defaults
)


@view_defaults(route_name='validator')
class Views(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'Credit Card Validation'
        self.result = ''
        self.controll = Controller()

    @property
    def validation_result(self):
        return self.result

    @view_config(renderer='validator.pt')
    def validator(self):
        if 'validate' in self.request.params:
            self.result = ''

            for item in self.request.POST.items():
                if str(item[0]) == 'txtList':
                    lines = str(item[1]).splitlines()
                    N = lines[0]

                    try:
                        for line in lines[1:int(N) + 1]:
                            self.result += self.controll.isValid(line) + "\n"
                    except Exception as e:
                        self.result = str(e)

        return {'page_title': 'Validator View'}
