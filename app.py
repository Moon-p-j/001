import streamlit as st

st.set_page_config(
    page_title="MBTI 테스트",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed",
)

DEFAULT_QUESTIONS = [
    "새로운 사람들과 함께 있을 때 나는 에너지를 얻는 편인가?",
    "나는 구체적인 사실보다 가능성과 미래의 의미에 더 관심이 있는가?",
    "결정을 내릴 때 논리와 객관적인 기준을 우선하는가?",
    "나는 계획을 세우고 정리된 방식으로 일을 진행하는가?",
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');
:root { --ink:#39364B; --muted:#817B96; --purple:#8B79CE; --lavender:#EEE9FF; --mint:#E2F5EF; --peach:#FFF0E5; --border:#E6E0F2; }
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.stApp { background: linear-gradient(145deg, #F8F5FF 0%, #FBF9FF 45%, #F1FAF6 100%); color:var(--ink); }
.block-container { max-width: 760px; padding-top: 2.2rem; padding-bottom: 3rem; }
.hero { text-align:center; padding: 1.2rem 1rem 1.5rem; }
.eyebrow { color:#8170C5; letter-spacing:.18em; font-size:.78rem; font-weight:800; }
.hero h1 { color:#8170C5; font-size:2.6rem; margin:.35rem 0 .35rem; font-weight:800; }
.hero p { color:#817B96; margin:0; font-size:1rem; }
.panel { background:rgba(255,255,255,.88); border:1px solid #E6E0F2; border-radius:24px; padding:1.5rem 1.6rem; box-shadow:0 12px 35px rgba(95,76,145,.07); margin:.7rem 0 1rem; }
.question-number { color:#8170C5; font-weight:800; font-size:.85rem; letter-spacing:.1em; margin-bottom:.5rem; }
.question-text { font-size:1.16rem; font-weight:700; line-height:1.65; margin-bottom:1rem; }
.scale-labels { display:flex; justify-content:space-between; color:#817B96; font-size:.78rem; margin-top:-.45rem; }
.result-type { font-size:4.2rem; line-height:1.15; letter-spacing:.08em; font-weight:800; color:#8170C5; text-align:center; padding:.8rem 0; }
.result-caption { text-align:center; color:#817B96; }
.stButton > button { border-radius:14px; min-height:3rem; font-weight:700; border:1px solid #DCD3F7; }
.stButton > button[kind="primary"] { background:#9483D5; border-color:#9483D5; color:white; }
.stButton > button[kind="primary"]:hover { background:#8170C5; border-color:#8170C5; color:white; }
div[data-testid="stRadio"] > label { font-weight:600; }
footer { visibility:hidden; }
@media (max-width:600px) { .block-container {padding-top:1rem;} .hero h1{font-size:2.1rem;} .panel{padding:1.1rem;border-radius:18px;} .question-text{font-size:1.05rem;} }
</style>
""", unsafe_allow_html=True)

if "questions" not in st.session_state:
    st.session_state.questions = DEFAULT_QUESTIONS.copy()
if "answers" not in st.session_state:
    st.session_state.answers = [None] * 4
if "page" not in st.session_state:
    st.session_state.page = "start"
if "question_index" not in st.session_state:
    st.session_state.question_index = 0


def start_test():
    st.session_state.answers = [None] * 4
    st.session_state.question_index = 0
    st.session_state.questions = DEFAULT_QUESTIONS.copy()
    st.session_state.page = "test"


def get_result(answers):
    letters = [
        "E" if answers[0] > 3 else "I",
        "N" if answers[1] > 3 else "S",
        "T" if answers[2] > 3 else "F",
        "J" if answers[3] > 3 else "P",
    ]
    return "".join(letters)


st.markdown("""
<div class="hero">
  <div class="eyebrow">A LITTLE MOMENT FOR YOU</div>
  <h1>MBTI 테스트 🌷</h1>
  <p>나를 알아가는 작은 질문들</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.page == "start":
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("### ✨ 나에 대해 가볍게 알아봐요")
    st.write("총 4개의 질문에 답하면 간단한 MBTI 유형 결과를 확인할 수 있어요.")
    st.markdown("<div style='background:#E2F5EF;border-radius:14px;padding:12px 14px;color:#4E6B61;font-size:.9rem;'>💡 정답은 없어요. 평소 자신의 모습과 가장 가까운 답을 선택해 주세요.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("테스트 시작하기", type="primary", use_container_width=True):
        start_test()
        st.rerun()
    st.caption("이 테스트는 4개 질문을 바탕으로 한 간단한 참고용 결과이며, 공식 MBTI 검사와는 다릅니다.")

elif st.session_state.page == "test":
    i = st.session_state.question_index
    st.progress((i + 1) / 4, text=f"QUESTION  {i + 1:02d}  /  04")
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(f'<div class="question-number">QUESTION {i + 1:02d} / 04</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="question-text">{st.session_state.questions[i]}</div>', unsafe_allow_html=True)
    labels = {1: "1 · 전혀 아니다", 2: "2", 3: "3 · 보통이다", 4: "4", 5: "5 · 매우 그렇다"}
    previous = st.session_state.answers[i]
    choice = st.radio(
        "나와 얼마나 가까운가요?",
        options=[1, 2, 3, 4, 5],
        index=(previous - 1) if previous else None,
        format_func=lambda x: labels[x],
        horizontal=True,
        key=f"answer_{i}",
        label_visibility="collapsed",
    )
    st.markdown("</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("처음으로" if i == 0 else "이전 질문", use_container_width=True):
            if i == 0:
                st.session_state.page = "start"
            else:
                st.session_state.answers[i] = choice
                st.session_state.question_index -= 1
            st.rerun()
    with col2:
        if st.button("결과 보기" if i == 3 else "다음 질문", type="primary", use_container_width=True):
            if choice is None:
                st.warning("답변을 하나 선택해 주세요.")
            else:
                st.session_state.answers[i] = choice
                if i < 3:
                    st.session_state.question_index += 1
                else:
                    st.session_state.result = get_result(st.session_state.answers)
                    st.session_state.page = "result"
                st.rerun()

elif st.session_state.page == "result":
    result = st.session_state.get("result", get_result(st.session_state.answers))
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;font-size:2rem;'>🌸</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;margin-bottom:0;'>테스트 완료! 수고했어요</h3>", unsafe_allow_html=True)
    st.markdown('<div class="result-caption">당신의 간단 테스트 결과는</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-type">{result}</div>', unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;color:#817B96;font-size:.9rem;'>각 질문에서 선택한 답을 바탕으로 계산했어요.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.info("이 결과는 4개 질문만으로 계산한 간단한 참고용 결과입니다. 정식 심리검사나 공식 MBTI 검사 결과를 대신하지 않습니다.")
    if st.button("처음부터 다시 하기", type="primary", use_container_width=True):
        st.session_state.page = "start"
        st.session_state.answers = [None] * 4
        st.session_state.question_index = 0
        st.rerun()

# Optional password-protected admin tools. Question changes are session-only and do not alter other visitors' tests.
with st.expander("관리자 도구"):
    st.caption("관리자 비밀번호를 Streamlit Cloud의 Secrets에 설정한 경우에만 사용할 수 있습니다. 수정 내용은 현재 관리자 세션에만 적용됩니다.")
    try:
        admin_password = st.secrets.get("ADMIN_PASSWORD", "")
    except Exception:
        admin_password = ""
    if not admin_password:
        st.write("관리자 도구를 사용하려면 배포 설정의 Secrets에 `ADMIN_PASSWORD`를 등록하세요.")
    else:
        supplied = st.text_input("관리자 비밀번호", type="password")
        if supplied == admin_password:
            st.success("관리자 인증 완료")
            edited = []
            for n, question in enumerate(st.session_state.questions, start=1):
                edited.append(st.text_input(f"질문 {n}", value=question, key=f"admin_question_{n}"))
            if st.button("현재 세션에 질문 적용"):
                if all(q.strip() for q in edited):
                    st.session_state.questions = [q.strip() for q in edited]
                    st.success("현재 세션에 적용했습니다. 모든 방문자에게 반영하려면 app.py의 DEFAULT_QUESTIONS를 수정해 다시 배포하세요.")
                else:
                    st.error("질문 4개를 모두 입력해 주세요.")
        elif supplied:
            st.error("비밀번호가 올바르지 않습니다.")
