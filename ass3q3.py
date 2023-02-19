def count_upper_lower(a):
    upper_case=0
    lower_case=0
    for i in a:
        if i.isupper():
            upper_case+=1
        elif i.islower():
            lower_case+=1
    return(upper_case,lower_case)

a='There was a Lion in the Den'
(upper_case,lower_case)=count_upper_lower(a)
print('upper_case_count',upper_case)
print('lower_case_count',lower_case)