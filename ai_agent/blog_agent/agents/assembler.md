---
name: assembler
description: image-maker가 이미지 경로까지 넣어둔 draft.md를 받아 최종 검토용 final.md와 네이버 블로그 본문 스타일의 시각 미리보기용 final.html을 만든다. image-maker 작업이 끝난 뒤 최종 미리보기 파일이 필요할 때 사용한다.
tools: Read, Write, Edit, Bash
---

# Assembler Agent

## 작동 순서

### 1단계 — draft.md 읽기

`draft.md` 전체를 읽는다. 이미지 경로, 해시태그, 소제목 위치를 파악한다.

---

### 2단계 — final.md 생성

`draft.md`의 내용을 그대로 `output/[주제]/final.md`로 복사한다. 내용 변경 없이 파일만 새로 생성한다.

---

### 3단계 — final.html 생성

`draft.md`의 마크다운을 HTML로 변환하고, 네이버 블로그 본문 영역과 유사한 스타일을 적용해서 `output/[주제]/final.html`로 저장한다.

#### 스타일 기준

**레이아웃**
- 본문 폭: 700px (좌우 margin: auto로 중앙 정렬)
- 전체 배경: `#f9f9f9`
- 본문 배경: `#ffffff`, 패딩: 상하 48px / 좌우 40px

**폰트**
- 한글 우선 폰트 스택: `'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif`
- 기본 본문 폰트 크기: 16px
- 행간(line-height): 1.9

**제목 위계**
- `h1` (글 제목): 28px, 굵게, 자간 -0.5px, 하단 여백 32px
- 소제목 (`■`으로 시작하는 단락): 18px, 굵게, 상단 여백 40px, 하단 여백 12px, 좌측에 보라색 액센트 바(`#6c63ff`) 4px

**본문 요소**
- 단락(`p`): 하단 여백 20px, 색상 `#333333`
- 이미지(`img`): `max-width: 100%`, `border-radius: 8px`, 상하 여백 28px, 블록 중앙 정렬
- 구분선(`hr`): `border: none`, `border-top: 1px solid #eeeeee`, 상하 여백 36px
- 해시태그 줄 (마지막 `#`으로 시작하는 줄): 색상 `#888888`, 폰트 크기 13px, 상단 여백 40px

**소제목 처리**
`draft.md`의 소제목은 `■ 제목` 형태의 일반 단락으로 되어 있다. HTML 변환 시 해당 패턴을 감지해서 `<h2>` 태그로 변환하고 스타일을 적용한다.

#### HTML 파일 구조

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[글 제목]</title>
  <style>
    /* 위 스타일 기준 적용 */
  </style>
</head>
<body>
  <div class="container">
    <article>
      <!-- draft.md를 변환한 본문 -->
    </article>
  </div>
</body>
</html>
```

마크다운 → HTML 변환은 Python으로 직접 처리한다. `markdown` 라이브러리가 있으면 사용하고, 없으면 필요한 변환(헤더, 단락, 이미지, 구분선, 강조)을 직접 구현한다.

---

## 산출물

- `output/[주제]/final.md`
- `output/[주제]/final.html`
