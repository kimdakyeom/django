# 장고 1025 실습
## 결과물✨
- 로그인 안했을 때 프로필

![ezgif com-gif-maker](https://user-images.githubusercontent.com/74820869/197703521-a8006a10-3177-42e1-81b1-9f0b1b4c8143.gif)


- 로그인했을 때 팔로우 & 팔로잉

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/74820869/197704722-84728228-397f-49b1-b9d1-4c89f4cac7e8.gif)
## 목표📚

유저(User)와 유저(User)가 N : M 관계로 매핑된 팔로우 기능을 추가로 개발합니다.

## 요구사항💻

### 모델 Model

- 모델 이름 : User
    
    Django AbstractUser 모델 상속 
    
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | followings | 팔로우 | ManyToMany | symmetrical=False, related_name='followers’ |
    |  |  |  |  |

- 모델 이름 : Article
    
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 글 제목 | Char | max_length=80 |
    | content | 글 내용 | Text |  |
    | user | 글 작성자 | ForeignKey | on_delete=models.CASCADE |

### 기능 View

회원관리 **accounts**

회원 팔로우 & 팔로우 취소
팔로우 % 팔로우 목록 표시 및 해당 프로필로 이동

- `POST` http://127.0.0.1:8000/accounts/<int:user_pk>/follow/
- 로그인한 유저만 팔로우 기능을 사용할 수 있습니다.

### 화면 Template

회원 정보 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/
- 팔로우 목록
    
    해당 회원의 팔로우 목록
    
- 팔로잉 목록
    
    해당 회원의 팔로잉 목록
    

- 다른 회원의 프로필 페이지
    - 팔로우 버튼
        
        스스로를 팔로우 할 수 없습니다.
        
        로그인한 유저만 팔로우 기능을 사용할 수 있습니다.
        
        로그인 상태 / 팔로우 상태에 따라 다르게 표현 합니다.