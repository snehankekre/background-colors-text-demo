import spacy
import streamlit as st

# Load the small English model from spaCy
nlp = spacy.load("en_core_web_sm")

st.set_page_config(
    page_title="NER with spaCy",
    page_icon="🏷️",
)


def annotate_text(text):
    """Generate annotations for given text."""
    doc = nlp(text)
    annotated_text = ""
    last_idx = 0
    for ent in doc.ents:
        annotated_text += text[last_idx : ent.start_char]
        color = "gray"  # Default color if not matched below
        if ent.label_ in ["PERSON", "NORP", "GPE"]:
            color = "blue"
        elif ent.label_ in ["ORG", "EVENT"]:
            color = "green"
        elif ent.label_ in ["DATE", "TIME"]:
            color = "orange"
        elif ent.label_ in ["MONEY", "QUANTITY", "ORDINAL", "CARDINAL"]:
            color = "red"

        # Use Streamlit's markdown with custom background color
        annotated_text += f":{color}-background[{text[ent.start_char:ent.end_char]}]"
        last_idx = ent.end_char
    annotated_text += text[last_idx:]  # Append any remaining text
    return annotated_text


st.header("NER with spaCy and Streamlit", divider=True)
st.caption(
    """
This demo showcases Named Entity Recognition (NER) using spaCy and Streamlit. 
The text you enter will be analyzed, and named entities will be highlighted with different background colors based on their entity type."""
)

user_input = st.text_area(
    "Enter Text",
    """Elon Musk, the CEO of Tesla, Inc., announced that the company had chosen Berlin as the site for its European Gigafactory. 

The announcement was made on November 12, 2019, during an awards ceremony. 
Tesla plans to invest around $4 billion in this new facility, aiming to start production by 2021. 
This strategic move is expected to boost the economy of Germany and provide thousands of jobs in the region.""",
    height=150,
)

with st.sidebar.expander("Annotation legend", expanded=True):
    st.markdown(
        """
    This demo showcases Named Entity Recognition (NER) using spaCy and Streamlit. 
    The text you enter will be analyzed, and named entities will be highlighted with different background colors based on their entity type.
    
    The colors used are as follows:
    - :blue-background[Blue]: PERSON, NORP, GPE
    - :green-background[Green]: ORG, EVENT
    - :orange-background[Orange]: DATE, TIME
    - :red-background[Red]: MONEY, QUANTITY, ORDINAL, CARDINAL
    - :gray-background[Gray]: Default color
    
    Note: The colors are based on the spaCy entity types, and the color choices are arbitrary.
    """
    )

if st.toggle("Analyze"):
    annotated_text = annotate_text(user_input)
    # Display the annotated text as markdown in Streamlit
    st.markdown(annotated_text)
