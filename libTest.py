# Name: libTest.py
# Date: 5/11/26
# Author: Alex Vu

import plotly.express as px

def windPlot():
    df = px.data.wind()
    fig = px.scatter_polar(df, color="strength", r="frequency", 
                           theta="direction")
    fig.show()

def stockPlot():
    df = px.data.stocks()
    stocks = ["GOOG", "AAPL", "AMZN", "FB", "NFLX", "MSFT"]
    fig = px.line(df, x="date", y=stocks, hover_name="value")
    fig.show()


def main():
    # windPlot()
    # stockPlot()
    influence()


if __name__ == "__main__":
    main()