st = raw_input()

if sum([1 for x in st if x.islower()]) > sum([1 for x in st if x.isupper()]):
    print st.lower()
elif sum([1 for x in st if x.islower()]) < sum([1 for x in st if x.isupper()]):
    print st.upper()
else:
    print st
