import click
import connexion
from connexion.mock import MockResolver
from flask_injector import FlaskInjector

from .injections import ApiModule, AppProviderModule, CachedApiModule
from .json_encoder import CustomJsonEncoder

app = connexion.App(__name__, specification_dir='swagger/')


@app.route('/')
def hello_world():
    return 'Hello at Python Łódź'


def setup(app: connexion.App):
    foo_bar = [
        'foo', 'bar',
    ]

    app.add_api('api_v1.yaml', swagger_ui=True, arguments={'data': foo_bar})
    app.add_api('api_examples_v1.yaml', resolver=MockResolver(mock_all=True))

    FlaskInjector(app=app.app, modules=[
        ApiModule,
        AppProviderModule,
        # CachedApiModule,  # Uncomment this to see how injector replaces BaseTalkingProvider implementation
    ])

    app.app.json_encoder = CustomJsonEncoder


@click.command()
@click.option('--port', '-p', default=5000)
def main(port):
    app.run(port=port)


setup(app)


if __name__ == '__main__':
    main()
