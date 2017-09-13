#Good times (fix)

ottawa = raw_input()
#Why did I use lists here? Good question, its to mess with y'all
print ottawa+' in Ottawa'
print str(int(''.join(list(ottawa)[:2]))-3)+ottawa[2:]+' in Victoria'
print str(int(''.join(list(ottawa)[:2]))-2)+ottawa[2:]+' in Edmonton'
print str(int(''.join(list(ottawa)[:2]))-1)+ottawa[2:]+' in Winnipeg'
print ottawa+' in Toronto'
print str(int(''.join(list(ottawa)[:2]))+1)+ottawa[2:]+' in Halifax'

if len(ottawa) <= 3:
    ottawa = ("0"*(4-len(ottawa)))+ottawa

hour = int(ottawa[:2])+1
minute = int(ottawa[2:])+30

if(minute >= 60):
    minute -= 60
    hour +=1



if len(str(minute)) == 1:
    minute = str('0'+str(minute))


print str(hour)+str(minute)+" in St. John's"
