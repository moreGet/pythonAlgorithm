def solution(phone_book):
    phone_book.sort() # 어차피 정렬후 첫번째에 없으면 끝까지 없음

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True

if __name__ == '__main__':
    p = ["119", "97674223", "1195524421"]
    print(solution(p))