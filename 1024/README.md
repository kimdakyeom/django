# 장고 1024 실습
## 결과물✨
- 로그인 전 & 후 좋아요

![ezgif com-gif-maker (10)](https://user-images.githubusercontent.com/74820869/197465056-1da9c6ac-dd18-4260-a8c0-fbbb4182235b.gif)

- 마이페이지 & 회원페이지 좋아요 누른 글

![ezgif com-gif-maker (11)](https://user-images.githubusercontent.com/74820869/197466121-1f870142-ac86-40bf-9f1e-4a764fc3ddbd.gif)


## 목표📚

유저(User)와 게시글(Article)이 N : M 관계로 매핑된 좋아요 기능 개발

## 요구사항💻

### 모델 Model

- 모델 이름 : User
    
    Django **AbstractUser** 모델 상속
    

- 모델 이름 : Article
    
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | user | 글 작성자 | ForeignKey | on_delete=models.CASCADE |
    | title | 글 제목 | Char | max_length=80 |
    | content | 글 내용 | Text |  |
    | like_users | 좋아요 | ManyToMany | related_name='like_articles’ |
### 기능 View

**게시판 articles** 

게시글 좋아요 & 좋아요 취소

- `POST` http://127.0.0.1:8000/article**s**/<int:article_pk>/likes/
- 로그인한 유저만 좋아요를 할 수 있습니다.

### 화면 Template

게시글 정보 페이지

- `GET` http://127.0.0.1:8000/article**s**/<int:article_pk>/
- 좋아요 버튼
    
    해당 글이 받은 좋아요 수를 표시합니다.
    
    로그인 상태와 좋아요 상태에 따라 다르게 표현하고, 기능을 제한합니다.

유저 페이지
- 해당 유저가 좋아요 누른 글을 표시한다.