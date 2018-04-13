"""
  Data collector module
"""
import pandas_datareader.data as web
from datetime import datetime
import time

class Collector(object):
  """ 
    Supports data collection through multiple objects or as a static method call
  """
  
  def __init__(self, symbol=None, start=None, end=None):
    
    if not symbol:
      print("Bot: you didn't specify a symbol! Defaulting to GOOGL.")
      symbol = "GOOGL"
    
    if not start:
      print("Bot: you didn't specify a start date! Defaulting to the past day.")
      start = datetime.utcfromtimestamp(time.time()-3600*24)
    
    if not end:
      print("Bot: you didn't specify an end date! Defaulting to now.")
      end = datetime.utcfromtimestamp(time.time())      
    
    self.data = web.DataReader(symbol, 'morningstar', start, end)
    
  @staticmethod
  def get_data(symbol=None, start=None, end=None):
    
    if not symbol:
      print("Bot: you didn't specify a symbol! Defaulting to GOOGL.")
      symbol = "GOOGL"
    
    if not start:
      print("Bot: you didn't specify a start date! Defaulting to the past day.")
      start = datetime.utcfromtimestamp(time.time()-3600*24)
    
    if not end:
      print("Bot: you didn't specify an end date! Defaulting to now.")
      end = datetime.utcfromtimestamp(time.time())      
    
    return web.DataReader(symbol, 'morningstar', start, end)    
    

nokia = Collector("nok").data
print("-"*6, "Stats for Nokia", "-"*6)
print("Mean:", nokia["Close"]["nok"].mean())
print("Max:", nokia["Close"]["nok"].max())
print("Min:", nokia["Close"]["nok"].min())
print("Median:", nokia["Close"]["nok"].median())
