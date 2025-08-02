import dash
from dash import html, Dash   
from dash_mantine_components import MantineProvider


def home(flash_app):
    CONFIGS = dict(
        server = flash_app,
        title  ="api-invest",
        name   ="home", 
        url_base_pathname='/invest/home/'
    )
    app = Dash(**CONFIGS)

    app.layout = MantineProvider([

    ])

    return app.server