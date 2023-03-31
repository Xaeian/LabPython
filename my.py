from datetime import datetime, timedelta
import re, calendar

class time(datetime):
  
  def interval(interval:str="", dt:None|datetime=None):
    dt = time.now() if dt is None else dt
    value = re.findall("\-?[0-9]*\.?[0-9]+", interval)
    if not value: return dt
    value = float(value[0])
    factor = re.sub("[^a-z]", "", interval.lower())
    if factor == "y" or factor == "mo":
      if factor == "y": value *= 12
      month = dt.month - 1 + int(value)
      year = dt.year + month // 12
      month = month % 12 + 1
      day = min(dt.day, calendar.monthrange(year, month)[1])
      return dt.replace(year, month, day)
    match factor:
      case "w": dt += timedelta(weeks=value)
      case "d": dt += timedelta(days=value)
      case "h": dt += timedelta(hours=value)
      case "m": dt += timedelta(minutes=value)
      case "s": dt += timedelta(seconds=value)
      case "ms": dt += timedelta(milliseconds=value)
      case "us": dt += timedelta(microseconds=value)
    return dt
  
  def intervals(intervals:str=""):
    dt = time.now()
    for interval in intervals.split():
      dt = time.interval(interval, dt)
    return dt
  
  def isInterval(text:str):
    if re.search("^(\-|\+)?[0-9]*\.?[0-9]+(y|mo|w|d|h|m|s|ms|µs|us)$", text.strip()): return True
    else: return False
    
  def isIntervals(text:str):
    if re.search("^((\-|\+)?[0-9]*\.?[0-9]+(y|mo|w|d|h|m|s|ms|µs|us) ?)*$", text.strip()): return True
    else: return False
  
  def create(some:str|int|float="now"):
    some = str(some).strip()
    if some.lower() == "now": return time.now()
    if some.replace('.', '', 1).isdigit(): return time.fromtimestamp(float(some))
    if time.isInterval(some): return time.interval(some)
    if time.isIntervals(some): return time.intervals(some)
    if re.search("^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})$", some): return time.strptime(some, '%Y-%m-%d %H:%M:%S')
    if re.search("^(\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})$", some): return time.strptime(some, '%m/%d/%y %H:%M:%S')
    else: return None
  
  def string(self):
    return self.strftime("%Y-%m-%d %H:%M:%S")