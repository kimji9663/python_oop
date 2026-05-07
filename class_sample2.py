class Person:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        
        # *args: 추가적인 위치 인자들
        self.hobbies = args # 값   형태로 받는다
        
        # **kwargs: 키워드 인자들
        self.info = kwargs # 변수 = 값   형태로 받는다
    def introduce(self):
        print(f"이름: {self.name}")
        
        if self.hobbies:
            print("취미:", ", ".join(self.hobbies))
        
        if self.info:
            print("추가 정보:")
            for key, value in self.info.items():
                print(f"  {key}: {value}")


# 사용 예시
p1 = Person("철수", "축구", "게임", age=20, city="서울")
p1.introduce()

print("------")

p2 = Person("영희", age=25)
p2.introduce()