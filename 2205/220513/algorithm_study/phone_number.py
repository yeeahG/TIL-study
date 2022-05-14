# 준석
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

# 예지
def solution(phone_number):
    num_four=phone_number[-4:]
    num_hidden=phone_number[:-4]
    answer=len(num_hidden)*"*" + num_four
    return answer

# 은혁
