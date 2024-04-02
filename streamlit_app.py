import streamlit as st

st.markdown("# :rainbowbg[Background colors for text demo]")

with st.expander("Usage"):
    st.markdown("""
    This demo showcases the markdown background color feature. 
    Select a color from the dropdown and type some text to see it rendered with the selected background color.

    The markdown syntax used is `:color-background[text]`, where `color` is the name of the background color and `text` is the text to be rendered.

    Alternative syntax options are `:colorbg[text]`, `:color-bg[text]`, and `:background-color[text]`.

    Supported background colors are :rainbowbg[Rainbow], :redbg[Red], :bluebg[Blue], :greenbg[Green], :violetbg[Violet], :orangebg[Orange], and :graybg[Gray].

    Note: You can also nest colored backgrounds with colored text, e.g. `:redbg[:blue[This is some blue text on a red background]]`.
    """)

col1, col2 = st.columns(2)

with col1:
    # Color options
    color_options = {
        "Rainbow": "rainbowbg",
        "Red": "redbg",
        "Blue": "bluebg",
        "Green": "greenbg",
        "Orange": "orangebg",
        "Gray": "graybg",
        "Violet": "violetbg",
    }

    # User input for color selection
    selected_color = st.radio("Choose a background color", list(color_options.values()), format_func=lambda x: list(color_options.keys())[list(color_options.values()).index(x)].capitalize(), horizontal=True)

    # User input for text
    user_input = st.text_input("Enter your text here:", value="This is some text")

    # Display the colored text
    st.markdown(f":{selected_color}[{user_input}]")

with col2:
    user_input = st.text_input("Enter your text in the syntax of your choice:", value=":rainbow-background[This is some text]")
    st.markdown(user_input)