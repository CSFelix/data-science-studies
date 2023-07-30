import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu # pip install streamlit-option-menu

# https://extras.streamlit.app
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_toggle import st_toggle_switch # pip install streamlit-toggle-switch
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.mandatory_date_range import date_range_picker
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_vertical_slider import vertical_slider # pip install streamlit-vertical-slider

# ---- Horizontal Menu ----
selected = option_menu(
	menu_title=None
	, options=[
		'DataFrame Explorer', 'Colored Header', 'Emoji Rain'
		, 'Toogle Switch', 'Vertical Space', 'Date Range Picker'
		, 'Metric Cards', 'Vertical Slider'
	]
	, default_index=0
	, orientation='horizontal'
	, styles={
		"container": {"padding": "5px"}
	}
)

if selected == 'DataFrame Explorer':
	# ---- DATAFRAME EXPLORER ----
	df = pd.read_excel('./Data.xlsx', engine='openpyxl')
	filtered_df = dataframe_explorer(df)
	st.dataframe(filtered_df, use_container_width=True)

elif selected == 'Colored Header':
	# ---- COLORED HEADER ----
	colored_header(
	    label="What's shaking, bacon?",
	    description="blablabla - description",
	    color_name="violet-70",
	)

elif selected == 'Emoji Rain':
	# ---- EMOJI RAIN ----
	rain(
	    emoji="❄️",
	    font_size=25,
	    falling_speed=5,
	    animation_length="infinite",
	)

elif selected == 'Toogle Switch':
	st.write("## Toggle Switch")
	st_toggle_switch(
	    label="Enable Setting?",
	    key="switch_1",
	    default_value=False,
	    label_after=False,
	    inactive_color="#D3D3D3",  # optional
	    active_color="#11567f",  # optional
	    track_color="#29B5E8",  # optional
	)

elif selected == 'Vertical Space':
	add_n_lines = st.slider("Add n vertical lines below this", 1, 20, 5)
	add_vertical_space(add_n_lines)
	st.write("Here is text after the nth line!")

elif selected == 'Date Range Picker':
	st.write(
	    """
	    This is an example of a date range picker that *always* returns a start and
	    end date, even if the user has only selected one of the dates. Until the
	    user selects both dates, the app will not run.
	    """
	)
	result = date_range_picker("Select a date range")
	st.write("Result:", result)

elif selected == 'Metric Cards':
	col1, col2, col3 = st.columns(3)
	col1.metric(label="Gain", value=5000, delta=1000)
	col2.metric(label="Loss", value=5000, delta=-1000)
	col3.metric(label="No Change", value=5000, delta=0)
	style_metric_cards(background_color='#363636', border_color='aliceblue', border_left_color='blue', border_size_px=1)

elif selected == 'Vertical Slider':
	st.write("## Vertical Slider")
	vertical_slider(
	    key="slider",
	    default_value=25,
	    step=1,
	    min_value=0,
	    max_value=100,
	    track_color="gray",  # optional
	    thumb_color="blue",  # optional
	    slider_color="red",  # optional
	)