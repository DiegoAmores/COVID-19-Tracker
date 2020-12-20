from covid_tracker_app import CovidTrackerApp
import pandas as pd 
import builtins
from unittest import mock

covid_report = CovidTrackerApp()

def test_columns(capsys):
    with mock.patch("builtins.input",
                    side_effect = ["2020-12-16"]):
        assert covid_report.latest_highest_deaths_rates() == [4.391238291617682, 4.317442197883367, 3.7857762929447043, 3.489647042419556, 2.812280290602297, 2.516104447549402, 2.513333041380505, 2.4018232455512765, 2.31304169831343, 2.1771731451682865]  
    with mock.patch("builtins.input",
                    side_effect = ["2020-12-17"]):
        assert covid_report.latest_highest_deaths_rates() == [4.350234981273499, 4.292110398397106, 3.7374655210883208, 3.467789284331239, 2.8068137824235384, 2.511438986157379, 2.4931888400800513, 2.4224012028814927, 2.2990463215258856, 2.1777135440762834]  
    with mock.patch("builtins.input",
                    side_effect = ["2020-12-15"]):
        assert covid_report.latest_highest_deaths_rates() == [4.430611680805852, 4.345436950802612, 3.837872283337805, 3.5159717487231608, 2.841469671257745, 2.53235687317281, 2.510635736462858, 2.405294663252466, 2.319694489907256, 2.1719358849199395]
