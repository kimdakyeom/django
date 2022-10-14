# 1012-1013 장고 실습
## 결과물✨
- 회원가입 & 로그인

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/74820869/195754883-a2625f58-7ef0-47bd-9e41-1c2bb05884f8.gif)

- 글 작성 & 수정 & 삭제

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/74820869/195755138-caf829f8-ff97-4ddd-8a3a-7bf5a96acba2.gif)

- 마이페이지 & 회원 정보 수정 & 로그아웃

![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/74820869/195755477-27f0c2af-464d-42b9-bd36-3a9aff0744e7.gif)

- 회원 정보 & 회원 탈퇴

![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/74820869/195755707-0254e429-7a16-45c6-b088-04fbdb06a5e6.gif)

## 목표📚

Django Auth를 활용한 회원관리(회원가입 / 회원 조회 / 로그인 / 로그아웃)가 가능한 서비스를 개발합니다.

## 요구사항💻

### 모델 Model

- 모델 이름 : User
    
    Django **AbstractUser** 모델 상속
    

### **폼 Form**

회원가입

- Django 내장 회원가입 폼 UserCreationForm을 상속받아서 **CustomUserCreationForm** 생성
    
    해당 폼은 아래 필드만 출력
    
    - username
    - email
    - password1
    - password2

로그인

- Django 내장 로그인 폼 **AuthenticationForm** 활용

회원 정보 수정

- Django 내장 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성&활용
    
    해당 폼은 아래 필드만 출력합니다.
    
    - first_name
    - last_name
    - email

### 기능  View

회원가입

- `POST` http://127.0.0.1:8000/accounts/signup/
- **CustomUserCreationForm**을 활용해서 회원가입 구현

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/

로그인

- `POST` http://127.0.0.1:8000/accounts/login/
- **AuthenticationForm**를 활용해서 로그인 구현

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

회원 정보 수정

- `POST` http://127.0.0.1:8000/accounts/<user_pk>/update/
- **CustomUserChangeForm**를 활용해서 회원 정보 수정 구현

회원 탈퇴
- `GET` http://127.0.0.1:8000/userdelete
- `request.user.delete()`

### 화면 Template

네비게이션바, Bootstrap `<nav>`

- 로그인 상태에 따라 다른 화면 출력
    1. 로그인 상태
        - 로그인 한 사용자의 username 출력
            - username을 클릭하면 회원 조회 페이지로 이동
        
        - 로그아웃 버튼
    2. 비 로그인 상태
        - 로그인 페이지 이동 버튼
        - 회원가입 페이지 이동 버튼

메인 페이지 

- `GET` http://127.0.0.1:8000/
- 글 목록
  - 글 제목 클릭 시 글의 detail 페이지로 이동
- 글 detail
  - 글의 작성자가 현재 로그인한 유저이면 수정/삭제 가능
  - 글의 작성자가 현재 로그인한 유저가 아니면 읽기만 가능


로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼

회원 목록 페이지

- `GET` http://127.0.0.1:8000/userspage/
- 회원 목록 출력
- 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/<user_pk>/accounts
- 회원 정보 출력
- 회원 정보 수정 페이지 이동 버튼

회원 정보 수정 페이지

- `GET` http://127.0.0.1:8000/userupdate/
- 탈퇴 버튼 클릭시 회원 탈퇴
- 비밀번호 변경 페이지 이동 버튼

비밀번호 변경 페이지
- `GET` http://127.0.0.1:8000/password/