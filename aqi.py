import pandas as pd
dates = pd.date_range('20150102', '20201231', freq='MS').strftime('%Y%m')   # 构造出日期序列  便于之后构造url


for i in range(len(dates)):
        df = pd.read_html(f'http://www.tianqihoubao.com/aqi/yangzhou-{dates[i]}.html', encoding='gbk', header=0)[0]
        if i == 0:
                df.to_csv('历年聊城空气质量数据.csv', mode='a+', index=False,header=1)    # 写入第一个数据表，含有表头
                i += 1
        else:
                df.to_csv('历年聊城空气质量数据.csv', mode='a+', index=False, header=False)  #追加写入后续的数据（无表头）到上一步的csv数据表中
