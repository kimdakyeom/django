# 1021 토이 프로젝트
## 결과물✨
- 로그인

![ezgif com-gif-maker (6)](https://user-images.githubusercontent.com/74820869/197373105-84eae821-5ac5-42f1-a271-f4136e861fcd.gif)

- 글 생성 & 수정

![ezgif com-gif-maker (7)](https://user-images.githubusercontent.com/74820869/197373161-8cd0a46e-bf28-46a5-acd5-72fc95e8ac47.gif)

- 댓글 생성 & 삭제

![ezgif com-gif-maker (8)](https://user-images.githubusercontent.com/74820869/197373201-0b0cf709-6d77-4c7c-afab-7bf6fbc44a1d.gif)

- 대댓글 생성

![ezgif com-gif-maker (9)](https://user-images.githubusercontent.com/74820869/197373219-6eb96ca2-03f7-4b3d-8a2a-28b7a184fcd8.gif)


## 목표📚

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- **CRUD** 구현
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- Django **Auth** 활용 회원 관리 구현
- Media 활용 동적 파일 다루기
- 모델간 **1 : N 관계** 매핑 코드 작성 및 활용
    - 유저 - 리뷰
    - 리뷰 - 댓글
    - 유저 - 댓글

### 요구사항💻
#### 회원 가입
앱 App 생성

- 앱 이름 : accounts

모델 Model 작성

- 모델 이름 : User
- Django AbstractUser 모델 상속

폼 Form 작성

- Django 내장폼 UserCreationForm을 상속받은 CustomUserCreationForm 작성

기능 View 

- `POST` accounts/signup/
- CustomUserCreationForm 활용

화면 Template

- `GET` accounts/signup/
- 회원가입 폼

---

#### 로그인
기능 View

- `POST` accounts/signup/
- 내장 폼 AuthenticationForm 활용

화면 Template

- `GET` accounts/signup/
- 로그인 폼
- 회원가입 페이지 이동 버튼

---

#### 로그아웃
기능 View

- `POST` account/logout

---

#### 리뷰 작성
앱 App 생성

앱 이름 : reviews

모델 Model 생성

모델 이름 : Review

- 모델 필드
    
    
    | 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | user | 리뷰 작성자 |  |  |
    | title | 리뷰 제목 |  |  |
    | content | 리뷰 내용 |  |  |
    | movie_name | 영화 이름 |  |  |
    | grade | 영화 평점 |  |  |
    | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
    | updated_at | 리뷰 수정시간 | DateTime | auto_now = True |

기능 View

- `POST` reviews/create/

화면 Template

- `GET` reviews/create/
- 리뷰 작성 폼

---

#### 리뷰 목록 조회
**기능 View**

- `GET` reviews/

**화면 Template**

- `GET` reviews/

---

#### 리뷰 정보 조회
**기능 View**

- `GET` reviews/<int:review_pk>/

**화면 Template**

- `GET` reviews/<int:review_pk>/
- 리뷰 수정 / 삭제 버튼
    - 수정 / 삭제 버튼은 해당 리뷰 작성자에게만 출력합니다.
- 댓글 작성 폼
    - 댓글 작성 폼은 로그인 사용자에게만 출력합니다.
- 댓글 목록

---

#### 리뷰 정보 수정
**기능 View** 

- `POST` reviews/<int:review_pk>/update/
- 데이터를 생성한 사용자만 수정할 수 있습니다.

**화면 Template** 

- `GET` reviews/<int:review_pk>/update/
- 리뷰 수정 폼

---

#### 리뷰 삭제
**기능 View**

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

---

#### 댓글 작성
reviews 앱에 구현

모델 Model 생성

모델 이름 : Comment

- 모델 필드
    
    
    | 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | review | 참조 리뷰 |  |  |
    | user | 댓글 작성자 |  |  |
    | content | 댓글 내용 |  |  |
    | updated_at | 댓글 작성시간 | DateTime | auto_now = True |

기능 View 

- `POST` reviews/<int:review_pk>/comments/
- 로그인한 사용자만 댓글을 생성할 수 있습니다.

화면 Template 

- `GET` reviews/<int:review_pk>/
- 리뷰 정보 조회 페이지 하단에 댓글 작성 폼 출력

---

#### 댓글 목록 조회

기능 View

- `GET` reviwes/<int:review_pk>/

화면 Template

- `GET` reviews/<int:review_pk>/
- 리뷰 정보 조회 페이지 하단에 댓글 목록 출력

---

#### 댓글 삭제

기능 View

- `POST` reviews/<int:review_pk>/comments/<int:comment_pk>/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

화면 Template

- `GET` reviews/<int:review_pk>/
- 각 댓글에 리뷰 삭제 버튼 추가
    - 삭제 버튼은 해당 댓글 작성자에게만 출력합니다.

#### 대댓글 작성
reviews 앱에 구현

모델 Model 생성

모델 이름 : ReComment

- 모델 필드
    
    
    | 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | comment | 참조 리뷰 |  |  |
    | user | 댓글 작성자 |  |  |
    | body | 댓글 내용 |  |  |
    | updated_at | 대댓글 작성시간 | DateTime | auto_now = True |

기능 View 

- `POST` reviews/<int:comment_pk>/recomments/

화면 Template 

- `GET` reviews/<int:review_pk>/
- 리뷰 정보 조회 페이지 하단에 답글 버튼을 누르면 대댓글 작성 폼 출력

---