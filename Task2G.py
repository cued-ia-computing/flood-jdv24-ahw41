# This task serves to list the towns where I assess the risk of flooding to be greatest.
# No particular number of towns is given
# Risks will be "severe", "high", "moderate", "low"
# Classifications for each risk are in if statements at end of this program
# Effectively, if the level is going down risk is low, and otherwise various high levels
# of relative height and of rate of change of level (which were determined experimentally and
# honestly could probably be improved a lot, but it's difficult to make such estimates) were
# used as the cutoff for various risk levels.

import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import return_poly
import matplotlib


def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations = stations_highest_rel_level(stations, 30)
    riskAssessmentData = []
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        poly = return_poly(dates, levels, 4)
        deltaHeight = poly(matplotlib.dates.date2num(dates[0]) - matplotlib.dates.date2num(dates[0]))
        deltaHeight -= poly(matplotlib.dates.date2num(dates[1]) - matplotlib.dates.date2num(dates[0]))
        deltaTime = (dates[0] - dates[1]).seconds / 84600
        dHdT = deltaHeight / deltaTime
        riskAssessmentData.append([station.relative_water_level(), dHdT])
    riskLevel = []
    for station in range(len(stations)):
        if riskAssessmentData[station][1] < 0:
            riskLevel.append("1")
        elif riskAssessmentData[station][0] > 2.5 or riskAssessmentData[station][1] > 1:
            riskLevel.append("4")
        elif riskAssessmentData[station][0] > 2 or riskAssessmentData[station][1] > 0.8:
            riskLevel.append("3")
        elif riskAssessmentData[station][0] > 1.5 or riskAssessmentData[station][1] > 0.4:
            riskLevel.append("2")
        else:
            riskLevel.append("1")
    pairs = []
    for i in range(len(riskLevel)):
        pairs.append([riskLevel[i], stations[i]])
    pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
    for i in range(len(pairs)):
        if pairs[i][0] == "4":
            print(str(pairs[i][1].town) + ": Severe Risk")
        elif pairs[i][0] == "3":
            print(str(pairs[i][1].town) + ": High Risk")
        elif pairs[i][0] == "2":
            print(str(pairs[i][1].town) + ": Moderate Risk")
        else:
            print(str(pairs[i][1].town) + ": Low Risk")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
