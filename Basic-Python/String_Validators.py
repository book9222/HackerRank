# if __name__ == '__main__':
#     s = input()
#     ans_f = False
#     for i in s:
#         if i.isalnum():
#             print("True")
#             ans_f = False
#             break
#         ans_f = True
#     if ans_f : 
#         print("False")
    
#     ans_f = False
#     for i in s:
#         if i.isalpha():
#             print("True")
#             ans_f = False
#             break
#         ans_f = True
#     if ans_f : 
#         print("False")
            
#     ans_f = False
#     for i in s:
#         if i.isdigit():
#             print("True")
#             ans_f = False
#             break
#         ans_f = True
#     if ans_f : 
#         print("False")
        
#     ans_f = False
#     for i in s:
#         if i.islower():
#             print("True")
#             ans_f = False
#             break
#         ans_f = True
#     if ans_f : 
#         print("False")
        
#     ans_f = False
#     for i in s:
#         if i.isupper():
#             print("True")
#             ans_f = False
#             break
#         ans_f = True
#     if ans_f : 
#         print("False")
            


if __name__ == '__main__':
    s = input()
    
    res = any(i.isalnum() for i in s)
    print(res)
    res = any(i.isalpha() for i in s)
    print(res) 
    res = any(i.isdigit() for i in s)
    print(res)
    res = any(i.islower() for i in s)
    print(res)
    res = any(i.isupper() for i in s)
    print(res)