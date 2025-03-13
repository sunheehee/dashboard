import streamlit as st
# 페이지 설정 (아이콘과 제목 설정)
st.set_page_config(
    page_title="내 소개",
    page_icon="👋",
    layout="wide"
)

# CSS를 사용하여 배경색과 스타일 변경 (도전 과제)
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
    }
    .title {
        color: #1E88E5;
        text-align: center;
    }
    .header {
        color: #0277BD;
    }
    .highlight {
        background-color: #E3F2FD;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 앱 제목 (요구사항 1)
st.markdown("<h1 class='title'>✨ 내 소개 ✨</h1>", unsafe_allow_html=True)

# 프로필 정보를 2개 컬럼으로 표시
col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 이미지 (이모지 사용 - 도전 과제)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("## 🌱👧🏻💻")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # 기본 정보 표시 (요구사항 2)
    st.markdown("<h2 class='header'>기본 정보</h2>", unsafe_allow_html=True)
    st.markdown("<div class='highlight'>", unsafe_allow_html=True)
    st.markdown("**이름**: 장선희")
    st.markdown("**전공**: 중국어문학과 / 국제물류학과")
    st.markdown("**거주지**: 경기도 양주시")
    st.markdown("</div>", unsafe_allow_html=True)

# 취미 섹션 (요구사항 3)
st.markdown("<h2 class='header'>어떤 프로젝트 혹은 도메인에 관심있는지?</h2>", unsafe_allow_html=True)
st.markdown("<div class='highlight'>", unsafe_allow_html=True)
st.markdown("""
* 🌿 1순위 환경
* 👤2순위 소비자행동
* 🏥 3순위 임상병리...?

아직 뚜렷하게 관심이있는 도메인은 확실하지 않습니다.
""")
st.markdown("</div>", unsafe_allow_html=True)

# 자기소개 섹션
st.markdown("<h2 class='header'>자기소개</h2>", unsafe_allow_html=True)
st.markdown("<div class='highlight'>", unsafe_allow_html=True)
st.write("""
안녕하세요! 저는 데이터분석을 공부하고 있는 장선희입니다. 취미로는 밴드부에서 드럼을 연주하고 있고, 런닝을 좋아합니다. 

멋쟁이사자처럼 부트캠프에서 멋있으신 동기분들과 함께 프로젝트를 하며 성장하여, 실력있고 일 잘하는 데이터분석가가 될 것입니다!
""")
st.markdown("</div>", unsafe_allow_html=True)

# 방문자 인사말 섹션 (요구사항 4, 5)
st.markdown("<h2 class='header'>방명록</h2>", unsafe_allow_html=True)
greeting = st.text_input("인사말을 남겨주세요 👋")

if greeting:
    st.markdown("<div class='highlight' style='background-color: #E8F5E9;'>", unsafe_allow_html=True)
    st.success(f"감사합니다, {greeting}! 방문해주셔서 기쁩니다. 😊")
    st.markdown("</div>", unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 멋쟁이사자처럼 프로젝트</p>", unsafe_allow_html=True)
