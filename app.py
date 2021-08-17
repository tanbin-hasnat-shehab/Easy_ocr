import easyocr as ocr

import streamlit as st

def about():
    st.write(
        '''
        contact email - tanbinhasnat04@gmail.com
        ''')
def main():
    st.title("circle Detection App :sunglasses: ")
    st.write("**Using the Haar cascade Classifiers**")
    activities = ["Home", "About"]
    choice = st.sidebar.selectbox("Pick something fun", activities)
    if choice == "Home":
        st.write("Go to the About section from the sidebar to learn more about it.")
        image_file = st.file_uploader("Upload image", type=['jpeg', 'png', 'jpg', 'webp'])
	reader=ocr.Reader(['en','bn'])
	results=reader.readtext(image_file)
	text=''
	for result in results:
		text+=result[1] + '\n'
	st.write(text)
elif choice == "About":
	about()

if __name__ == "__main__":
    main()







