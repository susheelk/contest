'''
ottawa 0
winnipeg -1
edmonton -2
victoria -3
halifax +1
st johns +1.5
'''

def addHour(time, hr):
    time = [time[0]+hr, time[1]]
    if (time[0] >= 24):
        time[0] -=24
    time[1] = "%02d" % time[1]
    return map(str, time)


ottawa = raw_input()

ottawa = map(int, [ottawa[0:2], ottawa[2:]])

print str(int(str("".join(addHour(ottawa, -0))))) + " in Ottawa"
print str(int(str("".join(addHour(ottawa, -3))))) + " in Victoria"
print str(int(str("".join(addHour(ottawa, -2))))) + " in Edmonton"
print str(int(str("".join(addHour(ottawa, -1))))) + " in Winnipeg"
print str(int(str("".join(addHour(ottawa, -0))))) + " in Toronto"
print str(int(str("".join(addHour(ottawa, 1))))) + " in Halifax"

st = map(int, addHour(ottawa, 1))
st[1] += 30

if st[1] >= 60:
    st[1] = 60-st[1]
    st[0]+=1


st = map(str, st)
st[1] = "%02d" % int(st[1])

print str( int( str( "".join(st) ) ) ) + " in St. John's"
