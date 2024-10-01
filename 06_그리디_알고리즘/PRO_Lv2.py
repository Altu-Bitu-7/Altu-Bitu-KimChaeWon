def solution(number, k):
    result = []  
    for num in number:
        while k > 0 and result and result[-1] < num:
            result.pop()  
            k -= 1      
        result.append(num)

    if k > 0:
        result = result[:-k]

    return ''.join(result)