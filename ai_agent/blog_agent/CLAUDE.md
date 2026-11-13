네이버 블로그 글 작성을 자동화하는 멀티 에이전트 시스템. 메인(오케스트레이터)은 직접 글을 쓰거나 리서치하지 않고, 서브 에이전트에게 모든 작업을 위임한다.

---

## 폴더 구조

```
agents/        # 서브 에이전트 정의 파일
guides/        # 각 에이전트가 참조하는 스타일/SEO/이미지 가이드
output/[주제]/ # 주제별 산출물 (research.md, draft.md, images/, final.*)
user-images/   # 사용자가 직접 제공하는 이미지
```

---

## 실행 단계

사용자가 주제를 던지면 아래 순서대로 서브 에이전트를 호출한다.

**Step 1 — 리서치** (`agents/researcher.md`)  
→ 웹 검색으로 정보 수집, `output/[주제]/research.md` 생성  
→ 완료 후 사용자에게 알리고 다음 단계 진행 여부 확인

**Step 2 — 글쓰기** (`agents/writer.md`)  
→ research.md + style-guide + seo-guide 기반으로 초안 작성, `output/[주제]/draft.md` 생성  
→ 완료 후 사용자에게 알리고 다음 단계 진행 여부 확인

**Step 3 — 이미지 생성** (`agents/image-maker.md`)  
→ draft.md의 `[IMAGE: ...]` 마커를 실제 이미지로 교체, `output/[주제]/images/` 생성  
→ 완료 후 사용자에게 알리고 다음 단계 진행 여부 확인

**Step 4 — 통합** (`agents/assembler.md`)  
→ draft.md + images/를 합쳐 `final.md`, `final.html` 생성 후 브라우저로 열기

---

## 규칙

- 메인은 글을 직접 쓰거나 리서치를 직접 수행하지 않는다. 반드시 서브 에이전트에게 위임한다.
- 각 단계 완료 시 사용자에게 결과를 한 줄로 요약하고, 다음 단계로 넘어가도 되는지 확인한다.
- 사용자가 특정 단계만 지정해서 요청하면 해당 단계만 실행한다.
