import textwrap

def wrap(string, max_width):
    ans = ""
    # ans = ans + ((s + "\n") for s in textwrap.wrap(string, max_width))
    for s in textwrap.wrap(string, max_width):
        ans += s + "\n"

    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)