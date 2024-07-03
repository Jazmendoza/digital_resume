from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Justin Mendoza Resume.docx"
profile_pic = current_dir / "assets" / "profile-pic.png"

# ---GENERAL SETTINGS ---

PAGE_TITLE = "Digital CV | Justin Mendoza"
PAGE_ICON = ":wave:"
NAME = "Justin Mendoza"
DESCRIPTION = """
UX/UI DESIGNER | WEB DESIGNER | GRAPHIC DESIGNER
"""
EMAIL = "mendozajustinkl@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/justin-mendoza-a562b7206/", 
    "GitHub": "https://github.com/Jazmendoza"
}

PROJECTS = {
    "Hawker Heroes": "https://shorturl.at/LAmG8", 
    "MetaNose": "https://shorturl.at/LAmG8",
    "Penclusive": "https://shorturl.at/LAmG8"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC --
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width= 230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=":wave: Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application.octet-stream"
    )
st.write(":wave:", EMAIL)

#---SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---

st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✅ 4 Years experience in UX and UI Design
- ✅ Strong hands on experience and knowledge in Figma and Adobe XD
- ✅ Good understanding of Design Principles and User Experience Design Concepts
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- ➡️ Prototyping Softwares: Figma, Adobe XD
- ➡️ Visual Design Softwares: Photoshop, Procreate,  Canva

"""
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
st.write("Marketing Designer | Just Bento")
st.write("04/23 - 01/25")
st.write(
    """
- Conceptualized and designed compelling marketing materials, including brochures, social media graphics, and advertisements, to enhance brand visibility and engagement. 
- Lead market research and requirements gathering.
- Developed brand logos and comprehensive style guides to ensure consistent brand representation across all platforms. Identify stakeholders and establish collaboration platforms

"""
)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
