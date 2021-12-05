import dash_mantine_components as dmc

header = dmc.Group(
    position="apart",
    children=[
        dmc.Text(
            "Dash Mantine Components",
            variant="gradient",
            style={"fontSize": 35},
            gradient={"from": "indigo", "to": "cyan", "deg": 45},
        ),
        dmc.Anchor(
            dmc.Button("GitHub", variant="outline"),
            size="xl",
            href="https://github.com/snehilvj/dash-mantine-components",
        ),
    ],
)
