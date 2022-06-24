def sum(a, b):
  if type(a) != type(b):
    print("더하기를 할 수 없습니다")
    return
  else:
    return a+b


# 언더바 두개로 시작하는것들은 시스템 모듈
if __name__ == "__main__":
  print(sum(10,20))