import streamlit as st

from src.chat_session import manage_chat_session
from src.chat_session_manager import send_message


def intro(
    page_title,
    page_icon,
    title,
    markdown,
    prompt,
    llm,
    chat_session_args,
):
    """
    Sets up the page configuration, displays a title and markdown content. It allows file uploading, and interaction with the chat.

    Args:
        page_title: The title of the web page
        page_icon: The icon that will be displayed in the browser tab for the page. It should be a URL or a file path to an image file (e.g., a .png or .ico file) that represents the icon.
        title: The title of the page or application
        markdown: A string containing the Markdown content to be displayed on the page.
        prompt: The initial message or question that will be displayed in the chat interface.
        llm: The language model to be used for the chat session.
        chat_session_args: A dictionary containing additional arguments for the `manage_chat_session` function. These arguments are passed to the function when it is called.
    """

    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
    )
    st.title(title)
    st.markdown(markdown)
    send_message(
        "I'm ready to be your personal deals assistant.",
        "ai",
        save=False,
    )
    message = st.chat_input("What deals are you hunting for today?")

    if message:
        manage_chat_session(
            prompt=prompt,
            llm=llm,
            message=message,
            **chat_session_args,
        )
    else:
        st.session_state["messages"] = []
        st.session_state["chat_history"] = []
