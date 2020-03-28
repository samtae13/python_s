import random as r

q_num = r.randint(1, 100)
print("--- 숫자 맞추기 ---", q_num)

for num in range(1, 7):
    u_ans = int(input("%d번째 예상 숫자:" % num))
    if u_ans == q_num:
        print("정.답")
        break
    elif u_ans > q_num:
        print("작게")
    else:
        print("크게")

if num ==  6:
    print("정답 %d"% q_num)