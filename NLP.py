import streamlit as st
import base64

# 배경 이미지 설정 함수
def set_background(png_file):
    bin_str = base64.b64encode(png_file.read()).decode()
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 배경 이미지 불러오기
with open("cupt.png", "rb") as image_file:
    set_background(image_file)

# 페이지 제목과 설명
st.markdown("""
    <style>
    .title-text {
        text-align: center;
        color: black;
        font-family: 'Noto Sans', sans-serif;
        font-weight: 700
    }
    .main-text {
        text-align: center;
        color: black;
    }
    .custom-button {
        display: inline-block;
        padding: 15px 32px;
        font-size: 16px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: black;
        background-color: pink;
        border: none;
        border-radius: 50px;
        box-shadow: 0 9px #999;
        margin: 10px;
    }
    .custom-button:hover {background-color: #ff69b4}
    .custom-button:active {
        background-color: #ff69b4;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
    .centered-buttons {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
        flex-direction: row;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>CuPT - 대학생 소개팅 도우미</h1>", unsafe_allow_html=True)
st.markdown("""
<div class='main-text'>
    <p>대학생을 위한 최고의 소개팅 서비스</p>
    <p>매력적인 프로필 만들기, 프로필 매칭 서비스, 그리고 실시간 소개팅 코칭까지!</p>
</div>
""", unsafe_allow_html=True)

# 버튼을 가로로 정렬하기 위해 Streamlit 컨테이너와 컬럼 사용
st.write("")
st.write("")
cols = st.columns([1, 1, 1])

with cols[0]:
    st.markdown('<a href="https://generateprofile.streamlit.app/" target="_blank" class="custom-button">프로필 만들기</a>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<a href="https://searchkeyword1.streamlit.app/" target="_blank" class="custom-button">프로필 매칭</a>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<a href="https://assistanttt.streamlit.app/" target="_blank" class="custom-button">소개팅 코칭</a>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: black;'>
        <h4>CuPT - 당신의 사랑을 응원합니다!</h4>
        <p>© 2024 CuPT. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)
