from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('validator', '/')
    config.add_static_view(name='static', path='credit_card:static')
    config.scan('.views')
    return config.make_wsgi_app()

