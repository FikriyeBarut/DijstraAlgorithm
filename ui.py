import streamlit as st
import time
import cv2
from streamlit_option_menu import option_menu
import numpy as np
import solver

st.set_page_config(
    page_title="Path Planner",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)
st.title('Yol Planlayıcı')
with st.sidebar:
    selected = option_menu("Menu",["Anasayfa","Konum Ayarları"],
        icons=['house',"gear"],menu_icon="cast",default_index=1)
    selected

st.write(f'''<h3>Haritayı Yükleyiniz.</h3>
<p>Yol planlamak istediğiniz dosyayı ekleyip yolu çizdirebilir veya var olan harita üzerinden konum bilgilerini değiştirip yol planı oluşturabilirsiniz.</p>
''',unsafe_allow_html=True)


uploaded_file = st.file_uploader("Resim seçiniz.", ["jpg","jpeg","png"])
st.write('Veya')
use_default_image = st.checkbox('Haritayı Gör')
opencv_image = None
marked_image = None

if use_default_image:
    opencv_image = cv2.imread('maze.jpg')

elif uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

if opencv_image is not None:
    start_x = st.sidebar.slider("Başlangıç X", value= 270 if use_default_image  else 50, min_value=0, max_value=opencv_image.shape[1], key='sx')
    start_y = st.sidebar.slider("Başlangıç Y", value= 10 if use_default_image  else 100, min_value=0, max_value=opencv_image.shape[0], key='sy')
    finish_x = st.sidebar.slider("Bitiş X", value= 325 if use_default_image  else 100, min_value=0, max_value=opencv_image.shape[1], key='fx')
    finish_y = st.sidebar.slider("Bitiş Y", value= 580 if use_default_image  else 100, min_value=0, max_value=opencv_image.shape[0], key='fy')
    marked_image = opencv_image.copy()
    circle_thickness=(marked_image.shape[0]+marked_image.shape[0])//2//100 #ui circle thickness based on img size
    cv2.circle(marked_image, (start_x, start_y), circle_thickness, (0,255,0),-1)
    cv2.circle(marked_image, (finish_x, finish_y), circle_thickness, (255,0,0),-1)
    st.image(marked_image, channels="RGB", width=800)

if marked_image is not None:
    if st.button('Çözdür'):
        with st.spinner('En kısa yol bulunuyor...'):
            path = solver.find_shortest_path(opencv_image,(start_x, start_y),(finish_x, finish_y))
        pathed_image = opencv_image.copy()
        path_thickness = (pathed_image.shape[0]+pathed_image.shape[0])//2//50
        solver.drawPath(pathed_image, path, path_thickness)
        st.image(pathed_image, channels="RGB", width=500)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    st.write(f'<h6>Çeşitli Algoritmaların Yol Bulma Şemaları</h6>',unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)
with col1:
    st.write("Dijstra Algortitması")
    st.image("dj.png")
with col2:
    st.write("Belman-Ford Algortitması")
    st.image("belman.jpg")
with col3:
    st.write("A* Algortitması")
    st.image("a.png")  
 