mail=str(input("Enter your email : "))
S=mail.partition('@')
S1=str(S[0])
S2=str(S[2])
S3=S2.partition('.')
S4=str(S3[0])
S5=str(S3[2])
while True:
    if S1[0] in ('0','1','2','3','4','5','6','7','8','9'):
        print("Enter another valid Email :")  
        break  
    elif len(S1)>=3 and len(S4)>=3 and S3[1]=="." and S5=="com":
        print("Ok")
        break 
    else: 
        print("Enter another Valid Email :")
        break

    