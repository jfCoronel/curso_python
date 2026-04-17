# /// script
# dependencies = [
#     "marimo",
#     "pandas==3.0.2",
#     "plotly==6.7.0",
# ]
# requires-python = ">=3.14"
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Primer caso con Marimo
    """)
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(start=0,stop=10,step=1)
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"""
    El valor del slider es: __{slider.value}__
    """)
    return


@app.cell
def _():
    import pandas as pd

    meteo= pd.read_csv("sevilla_met.csv")
    return meteo, pd


@app.cell
def _(meteo, mo):
    columnas_meteo = list(meteo.columns[3:])
    selector_columna = mo.ui.dropdown(
        options=columnas_meteo,
        label="Columnas de meteo (desde la 3)",
    )
    selector_columna
    return (selector_columna,)


@app.cell
def _(meteo, pd, selector_columna):
    import plotly.express as px

    time = pd.date_range(start="01-01-2001",periods=8760,freq="1h")
    meteo["time"] = time

    fig = px.line(
        meteo,
        x="time",
        y=selector_columna.value,
        title=f"Gráfica anual de: {selector_columna.value}",
    )
    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
