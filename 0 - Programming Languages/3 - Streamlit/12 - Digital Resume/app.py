# https://pfpmaker.com (website to generate profile images)

from pathlib import Path
import streamlit as st
from PIL import Image

# ---- PATH SETTINGS ----
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'curriculum.pdf'
profile_pic = current_dir / 'assets' / 'profile-pic.png'

# ---- GENERAL SETTINGS ----
PAGE_TITLE = 'Data Scientist | CSFelix'
PAGE_ICON = ':bar_chart:'
NAME = 'Gabriel Felix'
DESCRIPTION = """
Data Science Student, Bachelor in Computer Science and Senior Full-Stack Developer.
"""
EMAIL = 'csfelix08@gmail.com'
SOCIAL_MEDIA = {
	'LinkedIn': 'https://linkedin.com/in/csfelix'
	, 'GitHub': 'https://github.com/csfelix'
	, 'Instagram': 'https://instagram.com/csfelix08'
}
PROJECTS = {
	'🏆 Project 1': 'https://www.google.com'
	, '🏆 Project 2': 'https://www.google.com'
}

# ---- PAGE CONFIG ----
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ---- LOADING CSS, PDF & PROFILE PIC ----
with open(css_file) as f:
	st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
	PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)



# ---- HERO SECTION ----
col1, col2 = st.columns(2, gap='small')

with col1:
	st.image(profile_pic, width=230)

with col2:
	st.title(NAME)
	st.write(DESCRIPTION)
	st.download_button(
		label='📃 Download Resume'
		, data=PDFbyte
		, file_name=resume_file.name
		, mime='application/octet-stream'
	)
	st.write(f'📩 {EMAIL}')

# ---- SOCIAL LINKS ----
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
	cols[index].write(f'[{platform}]({link})')



# ---- EXPERIENCE & QUALIFICATIONS ----
st.write('#')
st.subheader('Experience & Qualifications')
st.write(
	"""
- ✔ bla bla bla
- ✔ ble ble ble
	"""
)

# ---- SKILLS ----
st.write('#')
st.subheader('Hard Skills')
st.write(
	"""
- 😎 bli bli bli
- 😎 blo blo blo
	"""
)


# ---- WORK HISTORY ----
st.write('#')
st.subheader('Work History')
st.write('---')

# ---- JOB 1 ----
st.write('😄 **Help Desk | FX Systems**')
st.write('02/2019 - 10/2022')
st.write(
	"""
- bla bla bla
	"""
)

# ---- JOB 2 ----
st.write('#')
st.write('👨‍💻 **Full-Stack | FX Systems**')
st.write('11/2022 - Present')
st.write(
	"""
- bla bla bla
	"""
)


# ---- PROJECTS & ACCOMPLISHMENTS ----
st.write('#')
st.subheader('Project & Accomplishments')
st.write('----')

for project, link in PROJECTS.items():
	st.write(f'[{project}]({link})')