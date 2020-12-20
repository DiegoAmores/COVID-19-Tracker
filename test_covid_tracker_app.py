from covid_tracker_app import CovidTrackerApp
import pandas as pd 
import builtins
from unittest import mock

covid_report = CovidTrackerApp()

def test_happy_cases_death_rate(capsys):
    with mock.patch("builtins.input",
                    side_effect = ["2020-12-16"]):
        assert covid_report.latest_highest_deaths_rates() == [4.391238291617682, 4.317442197883367,
         3.7857762929447043, 3.489647042419556, 2.812280290602297, 2.516104447549402, 2.513333041380505,
          2.4018232455512765, 2.31304169831343, 2.1771731451682865]  
    with mock.patch("builtins.input",
                    side_effect = ["2020-12-17"]):
        assert covid_report.latest_highest_deaths_rates() == [4.350234981273499, 4.292110398397106,
         3.7374655210883208, 3.467789284331239, 2.8068137824235384, 2.511438986157379,
          2.4931888400800513, 2.4224012028814927, 2.2990463215258856, 2.1777135440762834]  
    with mock.patch("builtins.input",
                    side_effect = ["2020-12-15"]):
        assert covid_report.latest_highest_deaths_rates() == [4.430611680805852, 4.345436950802612,
         3.837872283337805, 3.5159717487231608, 2.841469671257745, 2.53235687317281, 2.510635736462858,
          2.405294663252466, 2.319694489907256, 2.1719358849199395]

def test_edge_cases_death_rate(capsys):
    with mock.patch("builtins.input",
                    side_effect = ["2020-06-30"]):
        assert covid_report.latest_highest_deaths_rates() == [9.29182611686804, 8.746647847565278, 8.664657303726926, 
                                                              7.981072079810721, 7.396998585624805, 7.338916536952185, 
                                                              6.666666666666667, 6.666666666666667, 6.416464891041162, 5.65038957949206]
    with mock.patch("builtins.input",
                    side_effect = ["2020-07-01"]):
        assert covid_report.latest_highest_deaths_rates() == [9.284548655844715, 8.701019935745451, 
                                                              8.67638765810038, 7.972264713995536, 7.4040479004608635, 
                                                              7.297744491857529, 6.666666666666667, 6.521739130434782, 
                                                              6.428817649086521, 5.67258054945707]
    

def test_recent_most_case_area(capsys):
    with mock.patch("builtins.input", side_effect=["2020-12-15"]):
        assert covid_report.recent_most_case_area() == [105999, 39190, 24689, 20222, 19876,
         19771, 16821, 15968, 14158, 12561, 11436, 11393, 11087, 9956, 9218, 8802, 7784, 7145,
          7103, 7045, 6543, 6528, 6213, 6131, 5873, 5454, 5345, 5007, 4950, 4640, 4634, 4604,
           4553, 3957, 3488, 2938, 2844, 2777, 2533, 2053, 1719, 1626, 1498, 1385, 1332, 1141,
            994, 668, 529, 491, 240, 226, 50, 34, 0]
    
    with mock.patch("builtins.input", side_effect =["2020-11-25"]):
        assert covid_report.recent_most_case_area() == [593936, 333157, 213435, 206807, 201660,
         201404, 194374,138769, 134862, 134779, 126787, 110637, 106909, 101504, 99868, 94653,
          90000, 89670, 80640, 71017, 69793, 67338, 63862, 59958, 59421, 55738, 54108, 53683,
           51869, 50950, 47674, 44266, 42268, 40922, 37943, 33685, 30433, 30217, 25435, 24973,
            17055, 16925, 16026, 15773, 15488, 13585, 13253, 9832, 6874, 5314, 2322, 2220, 478,
             357, 9]
    
    with mock.patch("builtins.input", side_effect =["2020-10-22"]):
        assert covid_report.recent_most_case_area() == [864661, 660835, 516109, 405748, 400392,
         341830, 324553, 316729, 292396, 286590, 261025, 246146, 211447, 208703, 205321, 203600,
          195064, 193490, 162032, 149968, 144355, 142578, 135721, 133271, 125989, 121643, 115264,
           105774, 104031, 97417, 95289, 94729, 92476, 91745, 86668, 74823, 70280, 58112, 57180,
            54012, 49809, 47696, 47428, 39329, 30474, 29849, 25240, 24270, 11837, 9293, 5303,
             4162, 3127, 535, 25]

def test_reg_data():
    state_death = covid_report.reg_data()

    assert len(state_death[0]) == 50
    assert len(state_death[1]) == 50

    assert len(state_death[0]) != 49
    assert len(state_death[1]) != 49
    assert len(state_death[0]) != 51
    assert len(state_death[1]) != 51
    assert len(state_death[0]) != 100
    assert len(state_death[1]) != 100

    assert state_death[0][0] == 'Alabama'
    assert state_death[0][17] == 'Louisiana'
    assert state_death[0][25] == 'Montana'
    assert state_death[0][49] == 'Wyoming'

    assert state_death[1][0] == '4487'
    assert state_death[1][17] == '5591'
    assert state_death[1][25] == '707'
    assert state_death[1][49] == '194'
