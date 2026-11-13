import os
from playwright.sync_api import sync_playwright

OUTPUT_DIR = r"d:\ok_son\ai_agent\blog_agent\output\삼척-가족여행-낚시\images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

COMMON_STYLE = """
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    width: 1080px;
    font-family: 'Pretendard', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: #ffffff;
    -webkit-font-smoothing: antialiased;
    word-break: keep-all;
  }
  .container {
    width: 1080px;
    padding: 56px 64px;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    position: relative;
    overflow: hidden;
  }
  .header-badge {
    display: inline-block;
    background: rgba(56, 189, 248, 0.15);
    border: 1px solid rgba(56, 189, 248, 0.45);
    color: #38bdf8;
    font-size: 20px;
    font-weight: 700;
    padding: 8px 20px;
    border-radius: 999px;
    margin-bottom: 18px;
    letter-spacing: 0.5px;
  }
  .section-title {
    font-size: 38px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.3;
    margin-bottom: 12px;
  }
  .section-sub {
    font-size: 22px;
    color: #a0a0b0;
    margin-bottom: 36px;
    line-height: 1.45;
  }
  .accent-mark {
    position: absolute;
    top: 44px;
    right: 64px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 22px;
    color: rgba(56, 189, 248, 0.45);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 8px 16px;
    border-radius: 10px;
  }
"""

THUMBNAIL_HTML = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1080px;
    height: 1080px;
    font-family: 'Pretendard', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
    word-break: keep-all;
  }
  .bg-circle-1 {
    position: absolute;
    width: 520px;
    height: 520px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.12) 0%, rgba(56, 189, 248, 0) 70%);
    top: -120px;
    left: -120px;
  }
  .bg-circle-2 {
    position: absolute;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.14) 0%, rgba(99, 102, 241, 0) 70%);
    bottom: -160px;
    right: -120px;
  }
  .frame {
    width: 920px;
    height: 920px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 36px;
    background: rgba(255, 255, 255, 0.02);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 72px;
    text-align: center;
    position: relative;
  }
  .top-tag {
    font-family: 'Consolas', 'Malgun Gothic', monospace;
    font-size: 24px;
    font-weight: 700;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.14);
    border: 1px solid rgba(56, 189, 248, 0.4);
    padding: 12px 28px;
    border-radius: 999px;
    margin-bottom: 42px;
    letter-spacing: 1px;
  }
  .main-title {
    font-size: 62px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.32;
    margin-bottom: 36px;
    letter-spacing: -1px;
  }
  .main-title .highlight {
    color: #38bdf8;
  }
  .divider {
    width: 96px;
    height: 5px;
    background: #38bdf8;
    border-radius: 999px;
    margin-bottom: 36px;
  }
  .sub-title {
    font-size: 30px;
    font-weight: 500;
    color: #a0a0b0;
    line-height: 1.5;
  }
  .accent-corner {
    position: absolute;
    bottom: 44px;
    right: 48px;
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(56, 189, 248, 0.35);
    padding: 14px 24px;
    border-radius: 16px;
    font-family: 'Consolas', 'Malgun Gothic', monospace;
    font-size: 22px;
    color: #e2e8f0;
  }
  .accent-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #38bdf8;
  }
</style>
</head>
<body>
  <div class="bg-circle-1"></div>
  <div class="bg-circle-2"></div>
  <div class="frame">
    <div class="top-tag">국내 가족여행 · 동해 바다낚시 가이드</div>
    <h1 class="main-title">
      11월 삼척 가족여행<br>
      <span class="highlight">1박 2일 코스</span><br>
      바다낚시·대게·숙소 총정리
    </h1>
    <div class="divider"></div>
    <p class="sub-title">
      제철 어종·금어기 주의사항 · 명소 3곳 · 맛집 5곳 · 4인 숙소 5곳
    </p>
    <div class="accent-corner">
      <span class="accent-dot"></span>
      <span>#SAMCHEOK_1N2D</span>
    </div>
  </div>
</body>
</html>
"""

# body-1: 유형 4 — 인용/강조 박스 (11월 중순 삼척 가족여행 핵심 요약)
BODY_1_HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  {COMMON_STYLE}
  .quote-box {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(56, 189, 248, 0.35);
    border-left: 8px solid #38bdf8;
    border-radius: 20px;
    padding: 44px 48px;
    margin-bottom: 32px;
  }}
  .quote-mark {{
    font-size: 56px;
    line-height: 1;
    color: #38bdf8;
    font-family: Georgia, serif;
    margin-bottom: 12px;
  }}
  .quote-text {{
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.48;
    margin-bottom: 20px;
  }}
  .quote-text span {{
    color: #38bdf8;
  }}
  .quote-sub {{
    font-size: 22px;
    color: #a0a0b0;
    line-height: 1.5;
  }}
  .pillars {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
  }}
  .pillar {{
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 22px 20px;
    text-align: center;
  }}
  .pillar-label {{
    font-size: 18px;
    color: #38bdf8;
    font-weight: 700;
    margin-bottom: 8px;
  }}
  .pillar-val {{
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 6px;
  }}
  .pillar-desc {{
    font-size: 16px;
    color: #a0a0b0;
  }}
</style>
</head>
<body>
  <div class="container" id="container">
    <div class="accent-mark">&lt;OVERVIEW /&gt;</div>
    <div class="header-badge">11월 중순 삼척 가족여행 핵심 요약</div>
    <h2 class="section-title">에메랄드빛 해안 절경과 생활낚시를 한 번에</h2>
    <p class="section-sub">강원대 삼척캠퍼스 기준 차량 10~30분 내 주요 항구·해변·맛집 밀집</p>
    <div class="quote-box">
      <div class="quote-mark">“</div>
      <div class="quote-text">
        낮에는 <span>해상케이블카·레일바이크</span>로 동해 절경을 달리고,<br>
        해 질 녘에는 평탄한 내항에서 <span>가자미·학꽁치 손맛</span>을 본 뒤,<br>
        저녁에는 따뜻한 <span>대게·홍게와 곰치국</span>으로 채우는 1박 2일 코스
      </div>
      <div class="quote-sub">
        — 삼척시청 교통·기후 통계 및 국립수산과학원 11월 표층 수온(16~18℃) 기준 맞춤 설계
      </div>
    </div>
    <div class="pillars">
      <div class="pillar">
        <div class="pillar-label">바다낚시</div>
        <div class="pillar-val">안전 포인트 6곳</div>
        <div class="pillar-desc">덕산·맹방·후진·장호항</div>
      </div>
      <div class="pillar">
        <div class="pillar-label">핵심 관광</div>
        <div class="pillar-val">해안 명소 3곳</div>
        <div class="pillar-desc">레일바이크·케이블카·초곡길</div>
      </div>
      <div class="pillar">
        <div class="pillar-label">제철 식도락</div>
        <div class="pillar-val">검증 맛집 5곳</div>
        <div class="pillar-desc">대게·홍게·곰치국·한정식</div>
      </div>
      <div class="pillar">
        <div class="pillar-label">맞춤 숙박</div>
        <div class="pillar-val">4인 숙소 5곳</div>
        <div class="pillar-desc">리조트·시립카라반·독채</div>
      </div>
    </div>
  </div>
</body>
</html>
"""

# body-2: 유형 3 — 핵심 포인트 카드 (11월 삼척 가족 바다낚시 어종·안전 포인트·금어기)
BODY_2_HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  {COMMON_STYLE}
  .cards-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }}
  .card {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 30px 32px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .card.warning {{
    border: 1px solid rgba(248, 113, 113, 0.5);
    background: rgba(248, 113, 113, 0.06);
  }}
  .card-num {{
    display: inline-block;
    width: fit-content;
    font-family: 'Consolas', monospace;
    font-size: 18px;
    font-weight: 700;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.15);
    padding: 6px 14px;
    border-radius: 8px;
  }}
  .card.warning .card-num {{
    color: #f87171;
    background: rgba(248, 113, 113, 0.18);
  }}
  .card-title {{
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.35;
  }}
  .card-desc {{
    font-size: 20px;
    color: #cbd5e1;
    line-height: 1.55;
  }}
  .card-tag {{
    margin-top: auto;
    padding-top: 12px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-size: 18px;
    color: #94a3b8;
    font-weight: 600;
  }}
  .card.warning .card-tag {{
    color: #fca5a5;
  }}
</style>
</head>
<body>
  <div class="container" id="container">
    <div class="accent-mark">&lt;FISHING_GUIDE /&gt;</div>
    <div class="header-badge">11월 중순 삼척 가족 바다낚시 핵심 포인트</div>
    <h2 class="section-title">채비별 주력 어종 &amp; 안전 포인트·금어기 수칙</h2>
    <p class="section-sub">표층 수온 16~18℃ 알짜 시즌 · 외항 테트라포드 진입 금지 및 법정 금어기 준수</p>
    <div class="cards-grid">
      <div class="card">
        <span class="card-num">POINT 01 · 원투낚시</span>
        <div class="card-title">참가자미 · 문치가자미(도다리) · 붕장어</div>
        <div class="card-desc">모래 바닥이 펼쳐진 맹방해변 백사장이나 덕산항·궁촌항 내항에서 청갯지렁이 미끼로 손쉽게 입질을 받습니다.</div>
        <div class="card-tag">✔ 문치가자미·참가자미 20cm 이하 방류 필수</div>
      </div>
      <div class="card">
        <span class="card-num">POINT 02 · 찌·민장대·루어</span>
        <div class="card-title">학꽁치 · 전갱이 · 감성돔 · 무늬오징어</div>
        <div class="card-desc">낮에는 카드채비로 학꽁치·망상어·전갱이 마릿수 손맛을 보고, 밤에는 가로등 주변에서 볼락(15cm↑)을 노립니다.</div>
        <div class="card-tag">✔ 감성돔 25cm 이하 / 볼락 15cm 이하 방류 필수</div>
      </div>
      <div class="card">
        <span class="card-num">POINT 03 · 가족 안전 명소</span>
        <div class="card-title">덕산항 · 후진항 · 맹방해변 · 장호항 배낚시</div>
        <div class="card-desc">화장실·주차장이 가깝고 발판이 평탄한 내항 위주로 출조하며, 초보 가족은 장호항 2시간 가자미 배낚시(3만 원)를 추천합니다.</div>
        <div class="card-tag">✔ 어린이 구명조끼 필수 · 선상낚시 전원 신분증 지참</div>
      </div>
      <div class="card warning">
        <span class="card-num">POINT 04 · 법정 주의사항</span>
        <div class="card-title">쥐노래미 금어기 &amp; 임원항 TTP 출입통제</div>
        <div class="card-desc">11월 1일~12월 31일은 쥐노래미 법정 금어기(혼획 시 즉시 방류, 위반 시 과태료 80만 원)이며, 임원항 동방파제 TTP는 출입통제구역입니다.</div>
        <div class="card-tag">⚠ 무단 진입 시 100만 원 이하 과태료 부과</div>
      </div>
    </div>
  </div>
</body>
</html>
"""

# body-3: 유형 3 — 핵심 포인트 카드 (삼척 가볼만한곳 3곳 & 11월 동절기 운영시간)
BODY_3_HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  {COMMON_STYLE}
  .cards-stack {{
    display: flex;
    flex-direction: column;
    gap: 22px;
  }}
  .spot-card {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 28px 34px;
    display: grid;
    grid-template-columns: 90px 1fr 280px;
    align-items: center;
    gap: 28px;
  }}
  .spot-num {{
    width: 76px;
    height: 76px;
    border-radius: 18px;
    background: rgba(56, 189, 248, 0.15);
    border: 1px solid rgba(56, 189, 248, 0.45);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Consolas', monospace;
    font-size: 30px;
    font-weight: 800;
    color: #38bdf8;
  }}
  .spot-main {{
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .spot-title {{
    font-size: 27px;
    font-weight: 800;
    color: #ffffff;
  }}
  .spot-desc {{
    font-size: 19px;
    color: #cbd5e1;
    line-height: 1.45;
  }}
  .spot-meta {{
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    padding: 16px 20px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .meta-row {{
    font-size: 17px;
    color: #e2e8f0;
    line-height: 1.4;
  }}
  .meta-row strong {{
    color: #38bdf8;
  }}
  .meta-warn {{
    color: #fbbf24;
    font-weight: 700;
    font-size: 17px;
  }}
</style>
</head>
<body>
  <div class="container" id="container">
    <div class="accent-mark">&lt;ATTRACTIONS_3 /&gt;</div>
    <div class="header-badge">삼척 가볼 만한 곳 추천 3선</div>
    <h2 class="section-title">낚시 포인트와 5~15분 거리 해안 명소 &amp; 동절기 시간</h2>
    <p class="section-sub">11월 동절기 단축 운영 및 사전 예매/현장 발권 여부를 출발 전 꼭 확인하세요</p>
    <div class="cards-stack">
      <div class="spot-card">
        <div class="spot-num">01</div>
        <div class="spot-main">
          <div class="spot-title">삼척해양레일바이크 (궁촌 ↔ 용화)</div>
          <div class="spot-desc">5.4km 해안선 곰솔 숲과 화려한 루미나리에 레이저 터널 코스 (무료 셔틀 복귀)</div>
        </div>
        <div class="spot-meta">
          <div class="meta-row"><strong>요금:</strong> 4인승 35,000원</div>
          <div class="meta-row"><strong>동절기:</strong> 일 5회 (4회차 14:30)</div>
          <div class="meta-warn">★ 온라인 사전 예매 필수</div>
        </div>
      </div>
      <div class="spot-card">
        <div class="spot-num">02</div>
        <div class="spot-main">
          <div class="spot-title">삼척해상케이블카 (용화역 ↔ 장호역)</div>
          <div class="spot-desc">에메랄드빛 장호항 바다 위 874m 상공을 따뜻하게 가로지르는 파노라마 캐빈</div>
        </div>
        <div class="spot-meta">
          <div class="meta-row"><strong>요금:</strong> 대인 왕복 10,000원</div>
          <div class="meta-row"><strong>운영:</strong> 09:00~18:00 (마감 17:10)</div>
          <div class="meta-warn">★ 예약 없음 · 당일 현장 발권</div>
        </div>
      </div>
      <div class="spot-card">
        <div class="spot-num">03</div>
        <div class="spot-main">
          <div class="spot-title">초곡용굴촛대바위길 (해안 데크 산책로)</div>
          <div class="spot-desc">평탄한 660m 해안 데크길과 56m 출렁다리, 촛대바위 비경 (왕복 40~50분 소요)</div>
        </div>
        <div class="spot-meta">
          <div class="meta-row"><strong>요금:</strong> 입장료·주차비 무료</div>
          <div class="meta-row"><strong>동절기:</strong> 09:00~17:00 운영</div>
          <div class="meta-warn">★ 16:00 입장 마감 (15시 전 도착)</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

# body-4: 유형 1 — 비교 표 (삼척 가족여행 맛집 5곳 & 11월 대게·홍게 팁)
BODY_4_HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  {COMMON_STYLE}
  table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 18px;
    overflow: hidden;
    margin-bottom: 24px;
  }}
  th {{
    background: rgba(56, 189, 248, 0.16);
    color: #38bdf8;
    font-size: 20px;
    font-weight: 800;
    padding: 18px 20px;
    text-align: left;
    border-bottom: 1px solid rgba(255, 255, 255, 0.14);
  }}
  td {{
    padding: 18px 20px;
    font-size: 19px;
    color: #e2e8f0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    line-height: 1.4;
  }}
  tr:last-child td {{
    border-bottom: none;
  }}
  .name-cell {{
    font-weight: 800;
    color: #ffffff;
    font-size: 21px;
    white-space: nowrap;
  }}
  .price-badge {{
    display: inline-block;
    background: rgba(255, 255, 255, 0.08);
    padding: 4px 12px;
    border-radius: 8px;
    font-size: 18px;
    color: #38bdf8;
    font-weight: 700;
  }}
  .tip-banner {{
    background: rgba(251, 191, 36, 0.1);
    border: 1px solid rgba(251, 191, 36, 0.4);
    border-radius: 14px;
    padding: 18px 24px;
    font-size: 19px;
    color: #fde68a;
    line-height: 1.5;
  }}
  .tip-banner strong {{
    color: #fbbf24;
  }}
</style>
</head>
<body>
  <div class="container" id="container">
    <div class="accent-mark">&lt;DINING_5 /&gt;</div>
    <div class="header-badge">삼척 가족여행 맛집 5곳 비교</div>
    <h2 class="section-title">대게·홍게 풀코스부터 아침 곰치국·한정식까지</h2>
    <p class="section-sub">아이와 부모님 입맛을 모두 만족시키는 시간대별 검증 식당 5선</p>
    <table>
      <thead>
        <tr>
          <th>식당명 (위치)</th>
          <th>대표 메뉴</th>
          <th>가격대 기준</th>
          <th>가족 추천 포인트</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="name-cell">① 삼척보스대게 본점</td>
          <td>대게·홍게 + 모둠회·볶음밥 풀코스</td>
          <td><span class="price-badge">싯가 (세트 구성)</span></td>
          <td>숙소 무료 픽업·샌딩, 저녁 만찬 최적</td>
        </tr>
        <tr>
          <td class="name-cell">② 삼척항 대게거리·회센터</td>
          <td>선주 직판 홍게·대게, 자연산 가자미회</td>
          <td><span class="price-badge">싯가 / 회 3~6만</span></td>
          <td>유통 마진 줄인 가성비 직판장 밀집</td>
        </tr>
        <tr>
          <td class="name-cell">③ 바다횟집 (정하동)</td>
          <td>묵은지 곰치국 · 반건조 장치찜</td>
          <td><span class="price-badge">곰치국 약 2만 원</span></td>
          <td>30년 전통 노포, 2일 차 아침 해장 추천</td>
        </tr>
        <tr>
          <td class="name-cell">④ 일미담 (삼척해변)</td>
          <td>영양돌솥밥 · 생선구이 · 간장게장</td>
          <td><span class="price-badge">1.5만 ~ 3.5만 원</span></td>
          <td>강원대 캠퍼스 8분, 호불호 없는 한정식</td>
        </tr>
        <tr>
          <td class="name-cell">⑤ 물꼬기 (새천년도로)</td>
          <td>생선구이 + 물회 + 회덮밥 + 대게라면</td>
          <td><span class="price-badge">1인 1.4~1.6만 원</span></td>
          <td>4가지 바다 별미를 한 상에 먹는 가성비</td>
        </tr>
      </tbody>
    </table>
    <div class="tip-banner">
      <strong>💡 11월 중순 게 요리 주문 팁:</strong> 동해 연안 대게 금어기는 11월 30일까지(12월 1일 위판 개시)입니다. 100% 국내산 제철 가성비는 살이 꽉 찬 <strong>홍게(붉은대게)</strong>를 고르시고, 대게는 수입산·먼바다 조업분 원산지와 수율을 확인하세요!
    </div>
  </div>
</body>
</html>
"""

# body-5: 유형 1 — 비교 표 (4인 가족 삼척 숙소 5곳 비교)
BODY_5_HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  {COMMON_STYLE}
  table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 18px;
    overflow: hidden;
  }}
  th {{
    background: rgba(56, 189, 248, 0.16);
    color: #38bdf8;
    font-size: 20px;
    font-weight: 800;
    padding: 18px 20px;
    text-align: left;
    border-bottom: 1px solid rgba(255, 255, 255, 0.14);
  }}
  td {{
    padding: 20px;
    font-size: 19px;
    color: #e2e8f0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    line-height: 1.45;
  }}
  tr:last-child td {{
    border-bottom: none;
  }}
  .stay-name {{
    font-weight: 800;
    color: #ffffff;
    font-size: 21px;
    white-space: nowrap;
  }}
  .zone-tag {{
    display: inline-block;
    font-size: 17px;
    font-weight: 700;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.14);
    padding: 4px 10px;
    border-radius: 6px;
  }}
  .rate-text {{
    color: #fbbf24;
    font-weight: 700;
    white-space: nowrap;
  }}
</style>
</head>
<body>
  <div class="container" id="container">
    <div class="accent-mark">&lt;FAMILY_STAY_5 /&gt;</div>
    <div class="header-badge">4인 가족 맞춤형 삼척 숙소 5곳 비교</div>
    <h2 class="section-title">호캉스 리조트 vs 오션뷰 공공 카라반 vs 기차 독채</h2>
    <p class="section-sub">여행 스타일(부모님 동반·캠낚 감성·아이 체험)에 맞춰 선택하는 권역별 베스트 숙소</p>
    <table>
      <thead>
        <tr>
          <th>숙소명</th>
          <th>권역</th>
          <th>4인 추천 객실</th>
          <th>11월 요금대</th>
          <th>핵심 매력 &amp; 낚시·관광 동선</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="stay-name">① 쏠비치 삼척</td>
          <td><span class="zone-tag">북부 해변</span></td>
          <td>패밀리 / 스위트</td>
          <td class="rate-text">10만 후반~30만 원대</td>
          <td>사계절 온수풀, 후진항·삼척해변 맛집 5분</td>
        </tr>
        <tr>
          <td class="stay-name">② 장호비치캠핑장</td>
          <td><span class="zone-tag">남부 장호항</span></td>
          <td>카라반 4인용(B)</td>
          <td class="rate-text">평일 10만 / 주말 12만</td>
          <td>시립 오션뷰 카라반, 배낚시·케이블카 도보 3분</td>
        </tr>
        <tr>
          <td class="stay-name">③ 하이원 추추파크</td>
          <td><span class="zone-tag">내륙 도계읍</span></td>
          <td>네이처빌 / 큐브빌</td>
          <td class="rate-text">10만 ~ 16만 원대</td>
          <td>독채 4~6인, 스위치백 기차·대금굴 15분</td>
        </tr>
        <tr>
          <td class="stay-name">④ 맹방비치캠핑장</td>
          <td><span class="zone-tag">중부 맹방</span></td>
          <td>루프탑하우스(4인)</td>
          <td class="rate-text">데크 2~3만 / 하우스 별도</td>
          <td>해송 숲 시립 캠핑장, 바로 앞 백사장 원투낚시</td>
        </tr>
        <tr>
          <td class="stay-name">⑤ 시소소·장호항펜션</td>
          <td><span class="zone-tag">삼척/장호</span></td>
          <td>오션뷰 가족실</td>
          <td class="rate-text">시즌·객실별 상이</td>
          <td>개별 자쿠지·사우나·조식(시소소) / 스파(장호항)</td>
        </tr>
      </tbody>
    </table>
  </div>
</body>
</html>
"""

# body-6: 유형 2 — 단계별 다이어그램 (11/14~11/15 1박 2일 동선 요약)
BODY_6_HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  {COMMON_STYLE}
  .day-block {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 26px 26px;
    margin-bottom: 24px;
  }}
  .day-block:last-child {{
    margin-bottom: 0;
  }}
  .day-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
    gap: 16px;
  }}
  .day-badge {{
    font-size: 20px;
    font-weight: 800;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.15);
    padding: 8px 16px;
    border-radius: 10px;
    white-space: nowrap;
  }}
  .day-note {{
    font-size: 17px;
    color: #94a3b8;
    font-weight: 600;
    white-space: nowrap;
  }}
  .steps-row {{
    display: flex;
    align-items: stretch;
    justify-content: space-between;
    gap: 6px;
    width: 100%;
  }}
  .step-box {{
    flex: 1 1 0;
    min-width: 0;
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    padding: 16px 12px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .step-box.active {{
    border-color: rgba(56, 189, 248, 0.55);
    background: rgba(56, 189, 248, 0.08);
  }}
  .step-num {{
    font-family: 'Consolas', monospace;
    font-size: 15px;
    font-weight: 800;
    color: #38bdf8;
  }}
  .step-time {{
    font-size: 15px;
    color: #fbbf24;
    font-weight: 700;
  }}
  .step-name {{
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.3;
  }}
  .step-sub {{
    font-size: 15px;
    color: #a0a0b0;
    line-height: 1.35;
  }}
  .arrow {{
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 800;
    color: #38bdf8;
    flex: 0 0 auto;
  }}
</style>
</head>
<body>
  <div class="container" id="container">
    <div class="accent-mark">&lt;ROUTE_1N2D /&gt;</div>
    <div class="header-badge">11/14(토) 06:00 출발 기준 1박 2일 동선 다이어그램</div>
    <h2 class="section-title">강원대 삼척캠퍼스 → 해안 절경 → 골든타임 낚시 → 대게 만찬</h2>
    <p class="section-sub">동절기 입장 마감(16:00)과 일몰 피딩 타임(15:30~17:30)에 맞춘 무낭비 시간표</p>

    <div class="day-block">
      <div class="day-header">
        <span class="day-badge">DAY 1 · 11/14(토) 북부 시내 → 중·남부 해안 동선</span>
        <span class="day-note">구간 이동 각 7~18분 내외</span>
      </div>
      <div class="steps-row">
        <div class="step-box">
          <span class="step-num">STEP 1</span>
          <span class="step-time">10:00 ~ 12:50</span>
          <div class="step-name">강원대 캠퍼스 &amp; 점심</div>
          <div class="step-sub">일미담 또는 물꼬기</div>
        </div>
        <div class="arrow">→</div>
        <div class="step-box">
          <span class="step-num">STEP 2</span>
          <span class="step-time">13:10 ~ 14:10</span>
          <div class="step-name">초곡용굴 촛대바위길</div>
          <div class="step-sub">16시 마감 전 산책</div>
        </div>
        <div class="arrow">→</div>
        <div class="step-box">
          <span class="step-num">STEP 3</span>
          <span class="step-time">14:30 ~ 15:30</span>
          <div class="step-name">삼척해양 레일바이크</div>
          <div class="step-sub">4회차 탑승 (사전예매)</div>
        </div>
        <div class="arrow">→</div>
        <div class="step-box active">
          <span class="step-num">STEP 4</span>
          <span class="step-time">15:35 ~ 17:30</span>
          <div class="step-name">해거름 가족 바다낚시</div>
          <div class="step-sub">궁촌·덕산항·맹방해변</div>
        </div>
        <div class="arrow">→</div>
        <div class="step-box">
          <span class="step-num">STEP 5</span>
          <span class="step-time">18:30 ~ 20:30</span>
          <div class="step-name">대게·홍게 풀코스</div>
          <div class="step-sub">보스대게·삼척항회센터</div>
        </div>
      </div>
    </div>

    <div class="day-block">
      <div class="day-header">
        <span class="day-badge">DAY 2 · 11/15(일) 일출·해장 → 장호항 체험 → 귀가</span>
        <span class="day-note">정체 전 14:30 귀가 출발</span>
      </div>
      <div class="steps-row">
        <div class="step-box">
          <span class="step-num">STEP 6</span>
          <span class="step-time">07:00 ~ 09:50</span>
          <div class="step-name">동해 일출 &amp; 곰치국</div>
          <div class="step-sub">바다횟집 곰치국·장치찜</div>
        </div>
        <div class="arrow">→</div>
        <div class="step-box">
          <span class="step-num">STEP 7</span>
          <span class="step-time">10:30 ~ 11:20</span>
          <div class="step-name">삼척해상 케이블카</div>
          <div class="step-sub">용화↔장호역 왕복</div>
        </div>
        <div class="arrow">→</div>
        <div class="step-box active">
          <span class="step-num">STEP 8</span>
          <span class="step-time">11:20 ~ 13:10</span>
          <div class="step-name">장호항 가자미 배낚시</div>
          <div class="step-sub">2시간 선상 체험/산책</div>
        </div>
        <div class="arrow">→</div>
        <div class="step-box">
          <span class="step-num">STEP 9</span>
          <span class="step-time">13:20 ~ 14:30</span>
          <div class="step-name">로컬 별미 &amp; 특산물</div>
          <div class="step-sub">막국수·물닭갈비·건어물</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

# body-7: 유형 4 — 인용/강조 박스 (장호항 선상 배낚시 체크리스트 & 기상 악화 시 플랜 B)
BODY_7_HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  {COMMON_STYLE}
  .highlight-card {{
    background: rgba(56, 189, 248, 0.08);
    border: 2px solid rgba(56, 189, 248, 0.45);
    border-radius: 22px;
    padding: 38px 44px;
    text-align: center;
    margin-bottom: 26px;
  }}
  .hl-quote {{
    font-size: 31px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.45;
    margin-bottom: 16px;
  }}
  .hl-quote span {{
    color: #38bdf8;
  }}
  .hl-sub {{
    font-size: 20px;
    color: #cbd5e1;
    line-height: 1.5;
  }}
  .dual-box {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
  }}
  .sub-panel {{
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 16px;
    padding: 24px 28px;
  }}
  .panel-title {{
    font-size: 22px;
    font-weight: 800;
    color: #fbbf24;
    margin-bottom: 10px;
  }}
  .panel-list {{
    font-size: 19px;
    color: #e2e8f0;
    line-height: 1.6;
  }}
</style>
</head>
<body>
  <div class="container" id="container">
    <div class="accent-mark">&lt;TIPS_PLAN_B /&gt;</div>
    <div class="header-badge">선상 체험 수칙 &amp; 날씨 변수 대응 가이드</div>
    <h2 class="section-title">장호항 가자미 배낚시 핵심 수칙 &amp; 기상 악화 시 플랜 B</h2>
    <p class="section-sub">장비 없는 초보 가족도 2시간 만에 마릿수 손맛을 보는 선상 체험 체크리스트</p>
    <div class="highlight-card">
      <div class="hl-quote">
        “장호항 가자미 체험 배낚시는 <span>1인 약 30,000원(2시간)</span>으로<br>
        아이들도 연안 모래 바닥에서 줄줄이 참가자미 손맛을 볼 수 있습니다.”
      </div>
      <div class="hl-sub">
        출항 30분 전 멀미약 복용 권장 · 초등학생/영유아 포함 승선자 전원 신분증(등본 등) 지참 필수
      </div>
    </div>
    <div class="dual-box">
      <div class="sub-panel">
        <div class="panel-title">✔ 장호항 배낚시 준비 체크리스트</div>
        <div class="panel-list">
          • 사전 전화·온라인 예약 및 기상 확인<br>
          • 전원 신분증(소아는 주민등록등본) 지참<br>
          • 미끼·채비 별도(5,000~10,000원 현장 구매)
        </div>
      </div>
      <div class="sub-panel">
        <div class="panel-title">☔ 강풍·풍랑주의보 시 내륙 플랜 B</div>
        <div class="panel-list">
          • 연중 10~15℃ 포근한 <strong>대금굴·환선굴</strong> 모노레일<br>
          • <strong>하이원 추추파크</strong> 스위치백 기차 &amp; 키즈관<br>
          • <strong>쏠비치 삼척 오션플레이</strong> 사계절 온수풀
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

IMAGES = [
    ("thumbnail.png", THUMBNAIL_HTML, True),
    ("body-1.png", BODY_1_HTML, False),
    ("body-2.png", BODY_2_HTML, False),
    ("body-3.png", BODY_3_HTML, False),
    ("body-4.png", BODY_4_HTML, False),
    ("body-5.png", BODY_5_HTML, False),
    ("body-6.png", BODY_6_HTML, False),
    ("body-7.png", BODY_7_HTML, False),
]

def main():
    with sync_playwright() as p:
        browser = None
        for kwargs in [{"channel": "msedge"}, {"channel": "chrome"}, {}]:
            try:
                browser = p.chromium.launch(**kwargs)
                print(f"Launched browser with {kwargs}")
                break
            except Exception as e:
                print(f"Launch failed with {kwargs}: {e}")
        if browser is None:
            raise RuntimeError("Could not launch Chromium/Edge/Chrome")
        for filename, html, is_square in IMAGES:
            out_path = os.path.join(OUTPUT_DIR, filename)
            if is_square:
                page = browser.new_page(viewport={"width": 1080, "height": 1080})
                page.set_content(html)
                page.wait_for_timeout(150)
                page.screenshot(path=out_path)
                page.close()
                print(f"Saved {filename} (1080x1080)")
            else:
                page = browser.new_page(viewport={"width": 1080, "height": 800})
                page.set_content(html)
                page.wait_for_timeout(150)
                height = page.evaluate("document.getElementById('container').offsetHeight")
                page.set_viewport_size({"width": 1080, "height": height})
                page.wait_for_timeout(100)
                page.screenshot(path=out_path)
                page.close()
                print(f"Saved {filename} (1080x{height})")
        browser.close()

if __name__ == "__main__":
    main()
