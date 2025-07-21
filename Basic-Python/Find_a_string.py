def count_substring(string, sub_string):
    ans = 0
    for i in range(len(string)-len(sub_string)+1):
        sec_str = string[i:i+len(sub_string)]
        if sec_str == sub_string: 
            ans += 1 
    return ans

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)