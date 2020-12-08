# Jhonatan Nagasako
# Udacity Data Analysis
# Project 1 - Analyzing Global Temps
# Purpose:
#      Using code and CSV files provide to determine
#      moving averages and line graph comparisons

############################

import urllib
dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
urllib.request.urlretrieve(dls, "test.xls")  # For Python 3