import tushare
dataNow = tushare.get_realtime_quotes("002600")
print(dataNow)