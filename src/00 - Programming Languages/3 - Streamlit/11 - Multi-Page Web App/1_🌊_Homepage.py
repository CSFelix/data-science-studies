import streamlit as st

# ---- CONFIG ----
# Emojis: https://www.webfx.com/tools/emoji-cheat-sheet
st.set_page_config(
	page_title='Multipage App'
	, page_icon=':bar_chart:'
)

# ---- MAIN CONTENT ----
st.title('Main Page')
st.sidebar.success('Select a page above.')

# ---- SESSION INPUT ----
if 'my_input' not in st.session_state:
	st.session_state['my_input'] = ''

my_input = st.text_input('Tip your name here', st.session_state['my_input'])
submit = st.button('Submit')

if submit:
	st.session_state['my_input'] = my_input
	st.write(f'Hey there, {my_input}')