# hair_style_app.py

import streamlit as st
from PIL import Image
import random

# 페이지 설정
st.set_page_config(
    page_title="✨ 헤어스타일 추천 앱",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 사용자 정의 CSS 스타일
st.markdown("""
    <style>
    .title {
        font-size:40px;
        font-weight:bold;
        color:#FF69B4;
        text-align:center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size:24px;
        color:#6A5ACD;
        margin-top: 20px;
    }
    .recommend-box {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 2px 12px #f0f0f0;
        margin-bottom: 30px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">💇‍♀️ 나에게 어울리는 헤어스타일은?</div>', unsafe_allow_html=True)

# 사용자 입력
gender = st.selectbox("👤 성별을 선택해주세요", ["선택 안 함", "여성", "남성"])
face_shape = st.selectbox("😊 얼굴형을 선택해주세요", ["선택 안 함", "계란형", "둥근형", "각진형", "긴형"])
style_preference = st.multiselect("🎨 좋아하는 스타일을 선택하세요", ["러블리", "시크", "내추럴", "댄디", "트렌디"])

st.markdown('<div class="subtitle">🎯 추천 스타일</div>', unsafe_allow_html=True)

# 샘플 이미지 기반 헤어스타일 DB
style_db = {
    "여성": [
        {"name": "러블리 웨이브", "image": "https://i.imgur.com/sJ8v1Hk.jpg", "tags": ["러블리", "내추럴"]},
        {"name": "시크 단발", "image": "https://i.imgur.com/Pl9MURX.jpg", "tags": ["시크", "트렌디"]},
        {"name": "긴 생머리", "image": "https://i.imgur.com/gAMKO5z.jpg", "tags": ["내추럴", "러블리"]}
    ],
    "남성": [
        {"name": "댄디컷", "image": "https://i.imgur.com/5c1RfR7.jpg", "tags": ["댄디", "내추럴"]},
        {"name": "투블럭 스타일", "image": "https://i.imgur.com/nxWv9qU.jpg", "tags": ["트렌디", "시크"]},
        {"name": "리젠트컷", "image": "https://i.imgur.com/xzCPQUG.jpg", "tags": ["댄디", "시크"]}
    ]
}

# 유효한 선택 여부 확인
if gender == "선택 안 함" or face_shape == "선택 안 함" or not style_preference:
    st.info("모든 항목을 선택하시면 스타일을 추천해드립니다 😊")
else:
    # 선택 기반 필터링
    matched_styles = [
        style for style in style_db[gender]
        if any(tag in style["tags"] for tag in style_preference)
    ]

    if matched_styles:
        for style in matched_styles:
            st.markdown('<div class="recommend-box">', unsafe_allow_html=True)
            st.image(style["image"], caption=style["name"], use_column_width=True)
            st.markdown(f"**스타일 태그**: {' · '.join(style['tags'])}")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("조건에 맞는 스타일을 찾을 수 없습니다. 선택 범위를 넓혀보세요.")

# 푸터
st.markdown("---")
st.markdown("© 2025 ✂️ HairStyle Recommender by YourName", unsafe_allow_html=True)
