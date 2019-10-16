import tushare as ts
import time

while 1 == 0:
    dataNow = ts.get_realtime_quotes("002600")

    name = dataNow.loc[0][0]
    price = float(dataNow.loc[0][3])
    high = dataNow.loc[0][4]
    low = dataNow.loc[0][5]
    volum = dataNow.loc[0][8]
    amount = dataNow.loc[0][9]
    openTody = dataNow.loc[0][1]
    pre_close = dataNow.loc[0][2]
    timee = dataNow.loc[0][30]

    # print(dataNow.loc[0])
    buy = 3.3
    sell = 3.4
    if price >= buy:
        print("买")
    elif price >= sell:
        print("卖")
    else:
        print("等")
    time.sleep(5)
