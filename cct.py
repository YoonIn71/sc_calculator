def cal_score(sc):
    if 90<=sc<=100:
        return 'A'
    elif 80<sc<=90:
        return 'B'
    elif 70<sc<=80:
        return 'C'
    elif 60<sc<=70:
        return 'D'
    else:
        return 'F'
def main():
    sc=int(input('점수를 입력해주세요'))
    print(cal_score(sc))
if __name__ == "__main__":
    main()
