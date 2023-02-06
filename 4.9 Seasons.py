month=input("enter the month :")
day=int(input("enter the day: "))
if month in ('january','febuary','march'):
    season='winter'
elif month in ('april','may','june'):
    season='summer'
elif month in ('july','august','september'):
    season='spring'
else:
    season='autumn'
if(month=='march')and(day>19):
    season='summer'
elif(month=='june')and(day>20):
    season='spring'
elif(month=='december')and(day>20):
    season='winter'
print("season is",season)

