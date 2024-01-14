import streamlit as st
import pandas as pd
import plotly.express as px

import base64
from io import StringIO, BytesIO

# ---- FUNCTIONS ----
def generate_excel_download_link(df):
	towrite = BytesIO()
	df.to_excel(towrite, encoding='utf-8', index=False, header=True)
	towrite.seek(0)
	b64 = base64.b64encode(towrite.read()).decode()
	href = f'<a href="data:application/vnd.openxmlformats-officedocumeent.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
	return st.markdown(href, unsafe_allow_html=True)

def generate_html_download_link(fig):
	towrite = StringIO()
	fig.write_html(towrite, include_plotlyjs='cdn')
	towrite = BytesIO(towrite.getvalue().encode())
	b64 = base64.b64encode(towrite.read()).decode()
	href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="plot.html">Download Plot</a>'
	return st.markdown(href, unsafe_allow_html=True)

# ---- PAGE CONFIG ----
st.set_page_config(
	page_title='Excel Plotter'
	, page_icon=':bar_chart:'
	#, layout='wide'
)

# ---- HEADER ----
st.title(':bar_chart: Excel Plotter')
st.subheader('Drag and Drop any Excel File:')

# ---- FILE UPLOAD ----
uploaded_file = st.file_uploader('Choose a XLSX File', type='xlsx')

if uploaded_file:
	st.markdown('----')
	df = pd.read_excel(uploaded_file, engine='openpyxl')
	st.dataframe(df)
	groupby_column = st.selectbox(
		'What would you like to analyse?'
		, ('Ship Mode', 'Segment', 'Category', 'Sub-Category')
	)

	# -- GROUPING DATAFRAME --
	output_columns = ['Sales', 'Profit']
	df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()

	# -- PLOTTING DATAFRAME --
	fig = px.bar(
		df_grouped
		, x=groupby_column
		, y='Sales'
		, color='Profit'
		, color_continuous_scale= ['red', 'yellow', 'green']
		, template='plotly_white'
		, title=f'<b>Sales & Profit by {groupby_column}</b>'
	)
	st.plotly_chart(fig)

	# -- DOWNLOADS SECTION --
	st.subheader('Downloads:')
	generate_excel_download_link(df_grouped)
	generate_html_download_link(fig)