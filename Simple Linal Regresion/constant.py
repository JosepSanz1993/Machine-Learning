url = 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1451606400&period2=1620518400&interval=1d&events=history&includeAdjustedClose=true'
lambda_s = lambda x:float(x)
lambda_f = lambda x:x>20 and x<80
name = 'Adj Close'
num_row = 10
volume = 70
