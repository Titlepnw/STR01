import streamlit as st

st.header("Panuwat Sittirat")
st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('นาย ภานุวัฒน์ สิทธิรัตน์')
st.subheader('สาขาวิชาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./p/pf.jpg')
with col2:
    st.image('./p/pg.jpg')