
import streamlit as st
import cv2
import add_faces
import anothertest
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# def extract_faces():
#    add_faces.add_face()

# def identify_image():
#    anothertest.test()

def main():
    
    st.title("FACE ATTENDANCE SYSTEM")
    st.header("If you are new here Add your Face..")
    name = st.text_input("Enter Your Name: ")
    addface=st.button("ADD FACE")
    if addface:
        if name:
            return add_faces.add_face(name)
    st.write("----------------------------------------------------")    
    st.header("To take attendance scan the Face..")
    img=cv2.imread("background.png")
    st.image(img,width=500,channels="BGR")
    scan=st.button("SCAN")
    if scan:
        return anothertest.test()
    st.write("----------------------------------------------------")  
    st.header("To see the Attendance click below..")
    database=st.button("SHOW DATABASE")
    if database:
        # count=st_autorefresh(interval=2000,limit=100,key="fizzbuzzcount")
        # if count==0:
        #     st.write("Count is zero")
        # elif count%3==0 and count%5==0:
        #     st.write("Fizzbuzz")
        # elif count%3==0:
        #     st.write("Fizz")
        # elif count%5==0:
        #     st.write("Buzz")
        # else:
        #     st.write(f"Count:{count}")                

        df=pd.read_csv("attendance/attendance_" + date + ".csv")
        
        st.dataframe(df.style.highlight_max(axis=0))
if __name__ == "__main__":
    main()

    