# 변수만 적어놔도 쓸 수 있음
PI = 3.141592

class Math:
  # self 내 거에 있는 값이라는 뜻. 꼭 들어가야함
  def solve(self, r):
    return PI * (r**2)
  def sum(self, a, b):
    return a + b


# 실행은 이 밑에서부터
if __name__ == "__main__":
  print(PI)
  a = Math()
  print(a.solve(2))
  print(a.sum(PI, 4.4))