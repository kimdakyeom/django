# 장고 1026 실습
## 결과물✨
![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/74820869/198835322-7889ecc5-68fd-4ca8-a1a0-38514ae8e335.gif)

## 목표📚

- 댓글 기능을 비동기로 처리합니다.
  - 읽기, 생성, 수정, 삭제

## 요구사항💻

### 모델 Model

### 모델 Model

모델은 아래 조건을 만족해야합니다.

- 모델 이름 : Article
    
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 글 제목 | Char | max_length=80 |
    | content | 글 내용 | Text |  |
    |  |  |  |  |

- 모델 이름 : Comment
    
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | content | 댓글 내용 | Char | max_length=80 |
    | article | 게시글 | ForeignKey | on_delete=models.CASCADE |

### 기능 View

**게시판 articles** 

게시글 목록 조회

- `GET` http://127.0.0.1:8000/article**s**/

게시글 정보 조회

- `GET` http://127.0.0.1:8000/article**s**/<int:article_pk>/
- 해당 게시글(article_pk)에 작성된 댓글 목록 조회

게시글 생성

- `POST` http://127.0.0.1:8000/article**s**[/](http://127.0.0.1:8000/posts/create/)create[/](http://127.0.0.1:8000/posts/create/)

**댓글 comments**

게시글에 작성된 댓글 목록 조회

- `GET` http://127.0.0.1:8000/article**s**/<int:article_pk>/
- 해당 게시글(article_pk)의 댓글 목록 조회

댓글 생성

- `POST` http://127.0.0.1:8000/article**s**/<int:article_pk>/comments/
- 비동기 처리

댓글 수정
- `POST` http://127.0.0.1:8000/article**s**/<int:article_pk>/comments/<int:comment_pk>/update/
- 비동기 처리

댓글 삭제

- `POST` http://127.0.0.1:8000/article**s**/<int:article_pk>/comments/<int:comment_pk>/delete/<int:comment_pk>/delete/
- 비동기 처리

### 화면 Template

게시글 목록 페이지

- `GET` http://127.0.0.1:8000/article**s**/

게시글 정보 페이지

- `GET` http://127.0.0.1:8000/article**s**/<int:article_pk>/
- 댓글 작성 폼
- 댓글 목록
    - 댓글 내용
    - 댓글 수정 버튼
    - 댓글 삭제 버튼

게시글 작성 페이지

- `GET` http://127.0.0.1:8000/article**s**/comments/
- 게시글 작성 폼