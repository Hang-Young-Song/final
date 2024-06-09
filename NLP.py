import streamlit as st
import base64
import webbrowser

# 배경 이미지 설정 함수
def set_background(png_file):
    bin_str = base64.b64encode(png_file.read()).decode()
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: 55%;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 배경 이미지 불러오기
with open("CuPT.png", "rb") as image_file:
    set_background(image_file)

# 페이지 제목과 설명
st.markdown("""
    <style>
    .title-text {
        text-align: center;
        color: blue;
    }
    .main-text {
        text-align: center;
        color: red;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>CuPT - 대학생 소개팅 도우미</h1>", unsafe_allow_html=True)
st.markdown("""
<div class='main-text'>
    <p>대학생을 위한 최고의 소개팅 서비스</p>
    <p>프로필 매칭 서비스, 매력적인 프로필 만들기, 그리고 소개팅 도우미까지!</p>
</div>
""", unsafe_allow_html=True)

# 스타일을 위한 CSS
st.markdown("""
    <style>
    .stButton>button {
        border: 2px solid #4CAF50;
        color: white;
        background-color: #4CAF50;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 12px;
        margin: 10px auto;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .centered-buttons {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

# 버튼 중앙 정렬을 위한 컨테이너
st.markdown("<div class='centered-buttons'>", unsafe_allow_html=True)

# 각 버튼에 대한 클릭 이벤트 설정
if st.button('프로필 매칭 서비스'):
    webbrowser.open_new_tab('https://searchkeyword1.streamlit.app/')
if st.button('매력적인 프로필 만들기'):
    webbrowser.open_new_tab('https://generateprofile.streamlit.app/')
if st.button('소개팅 도우미'):
    webbrowser.open_new_tab('https://assistanttt.streamlit.app/')

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: black;'>
        <h4>CuPT - 당신의 사랑을 응원합니다!</h4>
        <p>© 2024 CuPT. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)
