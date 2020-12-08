import urllib
dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
urllib.request.urlretrieve(dls, "test.xls")  # For Python 3