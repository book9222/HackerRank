if __name__ == '__main__':
    s = input()
    ans_f = False
    for i in s:
        if i.isalnum():
            print("True")
            ans_f = False
            break
        ans_f = True
    if ans_f : 
        print("False")
    
    ans_f = False
    for i in s:
        if i.isalpha():
            print("True")
            ans_f = False
            break
        ans_f = True
    if ans_f : 
        print("False")
            
    ans_f = False
    for i in s:
        if i.isdigit():
            print("True")
            ans_f = False
            break
        ans_f = True
    if ans_f : 
        print("False")
        
    ans_f = False
    for i in s:
        if i.islower():
            print("True")
            ans_f = False
            break
        ans_f = True
    if ans_f : 
        print("False")
        
    ans_f = False
    for i in s:
        if i.isupper():
            print("True")
            ans_f = False
            break
        ans_f = True
    if ans_f : 
        print("False")
            
