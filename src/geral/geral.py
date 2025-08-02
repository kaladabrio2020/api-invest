import dash
from dash import html, Dash   
from dash_mantine_components import MantineProvider


def geral(flash_app):
    CONFIGS = dict(
        server = flash_app,
        title  ="api-invest",
        name   ="geral", 
        url_base_pathname='/invest/geral/'
    )
    app = Dash(**CONFIGS)

    app.layout = MantineProvider([

    ])

    return app.server