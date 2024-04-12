print('else if ladder program')
print('----------------------')

# applying multiple test conditions to a single value.

# 91-100(s),81-90(A),71-80(B),61-70(C),51-60(D),50(E),<50-FAIL

mark = 76

if mark>=91 and mark<=100:
    print(mark,'grade is S')
elif mark>=81 and mark<=90:
    print(mark,'grade is A')
elif mark>=71 and mark<=80:
    print(mark,'grade is B')
elif mark>=61 and mark<=70:
    print(mark,'grade is C')
elif mark>=51 and mark<=60:
    print(mark,'grade is D')
elif mark==50:
    print(mark,'grade is E')
elif mark<50:
    print(mark,'fail')
else:
    print('enter mark between 1 to 100')
