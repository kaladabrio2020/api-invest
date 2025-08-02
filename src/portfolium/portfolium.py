import dash
from dash import html, Dash   
from dash_mantine_components import MantineProvider


def portfolium(flash_app):
    CONFIGS = dict(
        server = flash_app,
        title  ="api-invest",
        name   ="portfolium", 
        url_base_pathname='/invest/portfolium/'
    )
    app = Dash(**CONFIGS)

    app.layout = MantineProvider([

    ])

    return app.server