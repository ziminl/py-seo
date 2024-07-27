


from pytrends.request import TrendReq

# Google Trends API
pytrends = TrendReq(hl='en-US', tz=360)
pytrends = TrendReq(hl='ko-KR', tz=360)



keywords = ["SEO", "Python", "Automation"]



pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')
data = pytrends.interest_over_time()

print(data.head())


