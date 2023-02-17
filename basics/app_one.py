import streamlit as st 

st.title("Demo App 😂😂")

n1=st.number_input('enter number')
n2=st.number_input('enter another number')
name=st.text_input('enter your name')
c1,c2,c3,c4,c5,c6=st.columns(6) 
add=c1.button("Add")
sub=c2.button("Sub")
mul=c3.button("Mul")
div=c4.button("div")
exp=c5.button("power")
mod=c6.button("Modulus")
st.success(name)
if add:
    r=int(n1)+int(n2)
    st.success(r)
if sub:
    r=int(n1)-int(n2)
    st.success(r)
if mul:
    r=int(n1)*int(n2)
    st.success(r)
if div:
    r=int(n1)/int(n2)
    st.success(r)
if exp:
    r=int(n1)**int(n2)
    st.success(r)
if mod:
    r=int(n1)%int(n2)
    st.success(r)