def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    
    return [7-max(cnt+zero,1) ,7-max(cnt,1)]
    
if __name__ == '__main__':
    lottos = [45, 4, 35, 20, 3, 9]
    win_nums = [20, 9, 3, 45, 4, 35]
    print(solution(lottos, win_nums))