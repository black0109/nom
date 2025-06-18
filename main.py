# hair_style_app.py

import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="✨ 헤어스타일 추천 앱",
    layout="centered"
)

# CSS 스타일링
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #FF69B4;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 24px;
        color: #6A5ACD;
        margin-top: 40px;
        margin-bottom: 10px;
    }
    .recommend-box {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        margin-bottom: 30px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">💇‍♀️ 나에게 어울리는 헤어스타일은?</div>', unsafe_allow_html=True)

# 사용자 입력
gender = st.selectbox("👤 성별을 선택해주세요", ["여성", "남성"])
face_shape = st.selectbox("😊 얼굴형을 선택해주세요", ["계란형", "둥근형", "각진형", "긴형"])
style_preference = st.multiselect(
    "🎨 선호하는 스타일을 선택하세요",
    ["러블리", "시크", "내추럴", "댄디", "트렌디"]
)

# 스타일 데이터 (Imgur의 안정적인 샘플 링크 사용)
style_db = {
    "여성": [
        {
            "name": "러블리 웨이브",
            "image": "https://i.imgur.com/sJ8v1Hk.jpg",
            "tags": ["러블리", "내추럴"]
        },
        {
            "name": "시크 단발",
            "image": "https://i.imgur.com/Pl9MURX.jpg",
            "tags": ["시크", "트렌디"]
        },
        {
            "name": "긴 생머리",
            "image": "https://i.imgur.com/gAMKO5z.jpg",
            "tags": ["내추럴", "러블리"]
        }
    ],
    "남성": [
        {
            "name": "댄디컷",
            "image": "https://i.imgur.com/5c1RfR7.jpg",
            "tags": ["댄디", "내추럴"]
        },
        {
            "name": "투블럭 스타일",
            "image": "https://i.imgur.com/nxWv9qU.jpg",
            "tags": ["트렌디", "시크"]
        },
        {
            "name": "리젠트컷",
            "image": "https://i.imgur.com/xzCPQUG.jpg",
            "tags": ["댄디", "시크"]
        }
    ]
}

# 추천 섹션 제목
st.markdown('<div class="subtitle">🎯 추천 스타일</div>', unsafe_allow_html=True)

# 추천 로직
if not style_preference:
    st.info("👈 왼쪽에서 원하는 스타일을 선택해주세요.")
else:
    matched_styles = []
    for style in style_db[gender]:
        if any(tag in style["tags"] for tag in style_preference):
            matched_styles.append(style)

    if matched_styles:
        for style in matched_styles:
            st.markdown('<div class="recommend-box">', unsafe_allow_html=True)
            st.image(style["image"], caption=style["name"], use_column_width=True)
            st.markdown(f"**스타일 태그**: {' · '.join(style['tags'])}")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("선택한 스타일에 맞는 헤어스타일이 없습니다. 다른 옵션을 선택해보세요.")

# 푸터
st.markdown("---")
st.markdown("© 2025 ✂️ HairStyle Recommender by YourName", unsafe_allow_html=True)

