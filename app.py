import streamlit as st

st.title("Note Summary and Quiz Generator")
st.markdown("Upload Upto 3 images to generate Note Summary and quizzes")
st.devider()
with st.sidebar :
    st.heder ("Control panel")
   images= st.file_uploader("Upload your notes here", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
   if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded images")
            
            col = st.columns(len(images))

            

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
