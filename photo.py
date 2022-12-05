# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
#from PIL import Image
import random
st.title("今日のごはんはなににしよう")
st.write("体調を入力すると今日の晩ごはんにおすすめのメニューを表示します")

menu=st.selectbox("どれを表示しますか",("選択なし","今日のごはん", "ごはんリスト","めいのおすすめ"))

if menu=="ごはんリスト":
    col1,col2,col3 = st.columns(3)
    with col1:
       st.header("1")
       st.image("1.JPG",caption='中華風おかゆ')
    
    with col2:
       st.header("2")
       st.image("2.JPG",caption='京風親子うどん')
       
    with col3:
       st.header("3")
       st.image("3.JPG",caption='野菜と卵のぞうすい')
    
    col4, col5,col6 = st.columns(3)
    with col4:
       st.header("4")
       st.image("4.JPG",caption='カオマンガイ')
    
    with col5:
       st.header("5")
       st.image("5.JPG",caption='親子丼')
       
    with col6:
       st.header("6")
       st.image("6.JPG",caption="野菜炒め")
       
    col7, col8,col9 = st.columns(3) 
     
    with col7:
        st.header("7")
        st.image("7.JPG",caption='カレー')
    
    with col8:
        st.header("8")
        st.image("8.JPG",caption='お好み焼き')
        
    with col9:
        st.header("9")
        st.image("9.JPG",caption='からあげ')  

elif menu=="今日のごはん":    
    condition1=st.slider("今日のだるさを教えてください（１…だるい，１０…だるくない）",1,5,10)
       
    condition2=st.slider("どれくらい疲れていますか（１…疲れている，１０…疲れていない）",1,5,10)
    
    condition3=st.slider("今日の顔色はどうですか（１…悪い，１０…良い）",1,5,10)
    
    kekka = condition1 + condition2 + condition3
    
    if 0 <= kekka and kekka <= 10: 
        photonumber=random.randint(1,3)
        if st.button(label="表示ボタン",key=1):
            st.image(str(photonumber)+".JPG")
                  
    
    elif 11 <= kekka and kekka <= 20:
        photonumber=random.randint(4,6)
        if st.button(label="表示ボタン",key=2):
            st.image(str(photonumber)+".JPG")
        
    else:
        photonumber=random.randint(7,9)
        if st.button(label="表示ボタン",key=3):
            st.image(str(photonumber)+".JPG")
                    
elif menu=="選択なし":
    st.write('')
    
elif menu=="めいのおすすめ":
    st.image("kani.jpg")

    
    