# Name: libTest.py
# Date: 5/11/26
# Author: Alex Vu

import plotly.express as px
import cmath, math


def math():
    # [mils pk-pk, degrees]
    O = cmath.rect(5.6, math.radians(135))
    OT = cmath.rect(3.3, math.radians(238))
    TW = cmath.rect(74, math.radians(315))

    T = OT - O
    IC = TW / T
    HS = O * IC
    CW = -HS
    
    amplitude = abs(CW)
    angle = math.degrees(cmath.phase(CW)) % 360

    return [amplitude, angle]

def influence():
    correction = math()
    fig = px.scatter_polar(correction, r="amplitude", theta="angle")
    fig.show()


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