def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:  
            if not stack:  
                return False
            stack.pop()
            
    return len(stack) == 0