import sys

def get_feedback(secret, guess):
    # secret 和 guess 都是四位字符串
    a = 0
    b = 0
    # 计算A：位置和数字均正确
    for i in range(4):
        if secret[i] == guess[i]:
            a += 1
    # 计算B：数字正确、位置不对
    # 先统计各数字出现次数，再用min(次数)求得重合总个数，减去A即为B
    count_secret = [0]*10
    count_guess = [0]*10
    for ch in secret:
        count_secret[int(ch)] += 1
    for ch in guess:
        count_guess[int(ch)] += 1
    for d in range(10):
        b += min(count_secret[d], count_guess[d])
    b -= a
    return f"{a}A{b}B"

def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    N = int(input_lines[0].strip())
    guesses = []
    for i in range(1, N+1):
        line = input_lines[i].strip()
        if not line:
            continue
        parts = line.split()
        guess_str = parts[0]
        feedback = parts[1]
        guesses.append((guess_str, feedback))
    
    candidate = None
    count = 0
    # 枚举从0000到9999所有四位数字
    for num in range(10000):
        secret = f"{num:04d}"
        valid = True
        for guess_str, feedback in guesses:
            if get_feedback(secret, guess_str) != feedback:
                valid = False
                break
        if valid:
            candidate = secret
            count += 1
            # 如果候选解超过1个就可以退出
            if count > 1:
                break
    if count == 1:
        print(candidate)
    else:
        print("NA")

if __name__ == "__main__":
    main()