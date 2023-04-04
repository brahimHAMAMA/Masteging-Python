# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"
import datetime

thedate = datetime.datetime(2021, 6, 25)
dateNow = datetime.datetime.now()
NumberDays = dateNow - thedate
# Message Will Be

print(f"Days From {thedate.strftime('%Y-%B-%d')} To {dateNow.strftime('%Y-%B-%d')} Is => {NumberDays.days} Days" )

"Days From 2021-06-25 To 2021-08-10 Is => 46"