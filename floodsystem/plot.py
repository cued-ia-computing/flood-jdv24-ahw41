import matplotlib.pyplot as plt
from .analysis import polyfit
import numpy as np
import matplotlib


def plot_water_level_with_fit(station, dates, levels, p):
    poly = polyfit(dates, levels, p)
    plt.hlines(station.typical_range, dates[0], dates[-1])
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    dates = matplotlib.dates.date2num(dates)
    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1 - dates[0]))
    plt.show()


def return_poly(dates, levels, p):
    poly = polyfit(dates, levels, p)
    dates = matplotlib.dates.date2num(dates)
    return poly


def plot_water_levels(station, dates, levels):
    plt.hlines(station.typical_range, dates[0], dates[-1])
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
