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

menu=st.selectbox("どれを表示しますか",("選択無し","今日のごはん", "ごはんリスト"))

if menu=="ごはんリスト":
    col1,col2,col3 = st.columns(3)
    with col1:
       st.header("1")
       st.image("1.jpg",caption='中華風おかゆ')
    
    with col2:
       st.header("2")
       st.image("2.jpg",caption='京風親子うどん')
       
    with col3:
       st.header("3")
       st.image("3.jpg",caption='野菜と卵のぞうすい')
    
    col4, col5,col6 = st.columns(3)
    with col4:
       st.header("4")
       st.image("4.jpg",caption='カオマンガイ')
    
    with col5:
       st.header("5")
       st.image("5.jpg",caption='親子丼')
       
    with col6:
       st.header("6")
       st.image("6.jpg",caption="野菜炒め")
       
    col7, col8,col9 = st.columns(3) 
     
    with col7:
        st.header("7")
        st.image("7.jpg",caption='カレー')
    
    with col8:
        st.header("8")
        st.image("8.jpg",caption='お好み焼き')
        
    with col9:
        st.header("9")
        st.image("9.jpg",caption='からあげ')  

elif menu=="今日のごはん":    
    condition1=st.slider("今日のだるさを教えてください（１…だるい，１０…だるくない）",1,5,10)
       
    condition2=st.slider("どれくらい疲れていますか（１…疲れている，１０…疲れていない）",1,5,10)
    
    condition3=st.slider("今日の顔色はどうですか（１…悪い，１０…良い）",1,5,10)
    
    st.write(condition1 + condition2 + condition3)
    kekka = condition1 + condition2 + condition3
    
    if 0 <= kekka and kekka <= 10: 
        photonumber=random.randint(1,3)
        st.image(str(photonumber)+".jpg")          
    
    elif 11 <= kekka and kekka <= 20:
        photonumber=random.randint(4,6)
        st.image(str(photonumber)+".jpg") 
        
    else:
        photonumber=random.randint(7,9)
        st.image(str(photonumber)+".jpg") 

elif menu=="選択無し":
    None
    