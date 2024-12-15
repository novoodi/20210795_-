import random
import string
import pandas as pd

# 학생 수
num_students = 30

# 학생 정보 리스트 생성
students = []

for _ in range(num_students):
    # 이름: 알파벳 대문자 두 글자
    name = ''.join(random.choices(string.ascii_uppercase, k=2))
    # 나이: 18 ~ 22 사이의 정수
    age = random.randint(18, 22)
    # 성적: 0 ~ 100 사이의 정수
    grade = random.randint(0, 100)

    # 학생 정보 딕셔너리 생성 및 리스트에 추가
    student = {"이름": name, "나이": age, "성적": grade}
    students.append(student)

# 생성된 학생 리스트를 Excel 파일로 저장
df = pd.DataFrame(students)
df.to_excel("students_score.xlsx", index=False)
print("랜덤 학생 리스트가 'students_score.xlsx'에 저장되었습니다.")


# 선택 정렬 알고리즘
# 여기서 key는 정렬 기준을 의미한다.
def selection_sort(students, key):
    # 삽입할 요소(여기서는 학생정보임)를 n에 저장 
    n = len(students)
    # i부터 정렬되지 않은 부분의 시작 인덱스를 0부터 n-1까지 순서대로 대입한다.
    for i in range(0, n - 1):
        least = i
        for j in range(i + 1, n):
            # key에 해당하는 값이 더 작으면 least를 j로 업데이트
            if students[j][key] < students[least][key]:
                least = j
        # 이 과정이 모두 끝나면 least에 있는 값이 가장 작은 값이다.
        # 해당 값을 i번째에 있는 값과 교환한다.
        students[i], students[least] = students[least], students[i]
        # 이 과정을 n-1번 진행하면 정렬이 완료됨

# 삽입 정렬 알고리즘
# 여기서 key는 정렬 기준을 의미한다.
def insertion_sort(students, key):
    # 삽입할 요소(여기서는 학생정보임)를 n에 저장 
    n = len(students)
    for i in range(1, n):
        # 삽입할 요소를 미리 key 값에 저장해줌
        # 이를 인댁스 번호로 보면 1임
        key_index = students[i]
        # i-1의 값부터 비교를 위해 j에 i-1 할당
        j = i - 1
        # j가 0보다 크거나 같고, j번째 값이 key_index보다 크다면
        while j >= 0 and students[j][key] > key_index[key]:
            # j+1에 j번째 학생정보를 복사
            students[j + 1] = students[j]
            # j는 1씩 감소하여 앞으로 이동
            j -= 1
        # 반복문이 끝나면 j+1 위치에 key_index 삽입
        students[j + 1] = key_index

# 퀵 정렬 알고리즘
# 여기서 key는 정렬 기준을 의미한다.
def quick_sort(students, left, right, key):
    if left < right:
        # 피벗을 중심으로 두 부분을 분할하고 피벗의 위치 q를 구함
        q = partition(students, left, right, key)
        # 이후 피벗을 기준으로 왼쪽과 오른쪽을 재귀 함수를 통해서 정렬
        quick_sort(students, left, q - 1, key)
        quick_sort(students, q + 1, right, key)

def partition(students, left, right, key):
    # 피벗을 가장 왼쪽에 있는 값으로 설정
    pivot = students[left]
    # low는 왼쪽에서 두번째 값, left보다 하나 큰 값으로 설정
    low = left + 1
    # high는 오른쪽 값으로 설정
    high = right
    # 해당 코드는 low가 high보다 작을 때까지 반복
    while True:
        # low가 right 범위 안에 있고, low번째 값이 pivot보다 작거나 같으면 low 증가
        while low <= right and students[low][key] <= pivot[key]:
            low += 1
        # high가 left 범위 안에 있고, high번째 값이 pivot보다 크면 high 감소
        while high >= left and students[high][key] > pivot[key]:
            high -= 1
        if low > high:
            # 만약 low가 high보다 크다면 반복문 종료
            break
        # low와 high를 교환
        students[low], students[high] = students[high], students[low]
    # 피벗과 high를 교환
    students[left], students[high] = students[high], students[left]
    return high

# 원형 큐 클래스
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        # 큐가 가득 차 있지 않을 때 rear를 한 칸 이동 후 item 삽입
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue(self):
        # 큐가 비어있지 않을 때 front를 한 칸 이동 후 그 위치의 값 반환
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            item = self.array[self.front]
            self.array[self.front] = None  # 삭제된 자리 초기화
            return item

# 기수 정렬 알고리즘
def radix_sort(A):
    Buckets = 10  # 10진수를 확인하기 위해서 10으로 설정
    Digits = 3  # 정렬할 숫자의 최대 자릿수 (0~999 범위 가정)
    # 버킷 개수만큼 원형 큐 생성
    queues = [ArrayQueue(len(A)) for _ in range(Buckets)]

    n = len(A)
    factor = 1
    for d in range(Digits):
        # 자릿수에 따라 큐에 데이터 삽입
        for i in range(n):
            digit = (A[i] // factor) % Buckets
            queues[digit].enqueue(A[i])

        # 큐에서 데이터를 꺼내 배열로 재구성
        i = 0
        for b in range(Buckets):
            while not queues[b].is_empty():
                A[i] = queues[b].dequeue()
                i += 1

        # 다음 자릿수로 이동
        factor *= Buckets

# 메뉴 기능 추가
def display_menu():
    print("\n정렬 기준을 선택하세요:")
    print("1. 이름을 기준으로 정렬 (알파벳 순서)")
    print("2. 나이를 기준으로 정렬 (오름차순)")
    print("3. 성적을 기준으로 정렬 (오름차순)")
    print("4. 프로그램 종료")

def display_name_or_age():
    print("\n정렬 알고리즘을 선택하세요:")
    print("1. 선택 정렬")
    print("2. 삽입 정렬")
    print("3. 퀵 정렬")

def display_score():
    print("\n정렬 알고리즘을 선택하세요:")
    print("1. 기수 정렬 (성적 기준 전용)")

while True:
    display_menu()
    choice = input("선택: ")

    if choice in ['1', '2', '3']:
        # 정렬을 시작하기 전에 기존에 만들 렌덤 엑셀을 가져옴
        df = pd.read_excel("students_score.xlsx")
        # DataFrame을 리스트[dict] 형태로 변환
        students = df.to_dict('records')

        # 정렬 key 설정
        key = "이름" if choice == '1' else "나이" if choice == '2' else "성적"

        if choice in ['1', '2']:
            # 이름 또는 나이 기준일 때: 선택, 삽입, 퀵 정렬 가능
            display_name_or_age()
            sort_choice = input("정렬 알고리즘 선택: ")

            if sort_choice == '1':
                selection_sort(students, key=key)
                algorithm = "선택 정렬"
            elif sort_choice == '2':
                insertion_sort(students, key=key)
                algorithm = "삽입 정렬"
            elif sort_choice == '3':
                quick_sort(students, 0, len(students) - 1, key=key)
                algorithm = "퀵 정렬"
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
                continue

        else:  # 성적 기준일 때: 기수 정렬만 제공
            display_score()
            sort_choice = input("정렬 알고리즘 선택: ")

            if sort_choice == '1':
                grades = [student['성적'] for student in students]
                radix_sort(grades)
                for i, grade in enumerate(grades):
                    students[i]['성적'] = grade
                algorithm = "기수 정렬"
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
                continue

        # 정렬 결과 출력
        criterion = "이름" if key == "이름" else "나이" if key == "나이" else "성적"
        print(f"\n[{algorithm}]을 사용하여 [{criterion}] 기준으로 정렬된 결과입니다:")
        for student in students:
            print(student)

        # 여기서 사용자에게 파일 저장 여부를 물어봄
        save_decision = input("정렬된 데이터를 파일로 저장하시겠습니까? (y/n): ")
        if save_decision.lower() == 'y':
            save_path = input("정렬된 파일을 저장할 경로를 입력하세요 (예: C:/path/to/sorted_students.xlsx): ")

            # 확장자 체크: xlsx 없으면 pandas에서 오류 발생
            if not save_path.lower().endswith('.xlsx'):
                print("오류: 파일 이름에 .xlsx 확장자를 붙여주세요.")
                continue

            df_sorted = pd.DataFrame(students)
            df_sorted.to_excel(save_path, index=False)
            print(f"정렬된 파일이 {save_path} 에 저장되었습니다.")
        else:
            print("파일을 저장하지 않고 넘어갑니다.")

    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")
