# Today Is "2021, 8, 10"
import datetime
theDate = datetime.datetime.now()
print(theDate.strftime("%Y-%m-%d"))
print(theDate.strftime("%b %d, %Y"))
print(theDate.strftime("%d - %b - %Y"))
print(theDate.strftime("%d / %b / %y"))
print(theDate.strftime("%d / %B / %Y"))
print(theDate.strftime("%a, %d %B %Y"))

"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"