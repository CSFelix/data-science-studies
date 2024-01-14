import streamlit as st
from streamlit_option_menu import option_menu # pip install streamlit-option-menu

# ---- 1 Example: As Sidebar Menu ----
with st.sidebar:
	selected = option_menu(
		#menu_title=None
		menu_title='Main Menu'
		, options=['Home', 'Projects', 'Contact']
		, menu_icon='cast'
		, default_index=0
	)

# st.title(f'You have selected {selected}')

if selected == 'Home':
	st.title(f'You have selected {selected}')

elif selected == 'Projects':
	st.title(f'You have selected {selected}')

elif selected == 'Contact':
	st.title(f'You have selected {selected}')

# ---- 2 Example: As Horizontal Menu ----
selected = option_menu(
	menu_title=None
	, options=['Home', 'Projects', 'Contact']
	, default_index=0
	, orientation='horizontal'
	, styles={
		"container": {"padding": "5px"}
	}
)

# st.title(f'You have selected {selected}')

if selected == 'Home':
	st.title(f'You have selected {selected}')

elif selected == 'Projects':
	st.title(f'You have selected {selected}')

elif selected == 'Contact':
	st.title(f'You have selected {selected}')