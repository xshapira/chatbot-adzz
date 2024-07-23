from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from src.chat_model import ChatCallbackHandler, ChatModel
from src.manage import intro
from src.utils import load_file


def configure_chat_model():
    chat_model = ChatModel()
    chat_model.llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.1,
        streaming=True,
        callbacks=[
            ChatCallbackHandler(),
        ],
    )
    messages = [
        SystemMessagePromptTemplate.from_template(
            load_file("./prompt_templates/document_gpt/system_message.txt")
        ),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
    chat_model.prompt = ChatPromptTemplate.from_messages(messages=messages)
    chat_model.memory_llm = ChatOpenAI(
        temperature=0.1,
    )
    return chat_model


def run_chat_session(chat_model):
    intro_config = {
        "page_title": "CouponGuru",
        "page_icon": "💰",
        "title": "CouponGuru",
        "markdown": load_file("./markdowns/document_gpt.md"),
        "prompt": chat_model.prompt,
        "llm": chat_model.llm,
        "chat_session_args": {
            "_file_path": "files",
            "_cache_dir": "embeddings",
            "_embeddings": OpenAIEmbeddings(),
        },
    }

    intro(**intro_config)


def main() -> None:
    chat_model = configure_chat_model()
    chat_model.configure_chat_memory(chat_model.memory_llm)
    run_chat_session(chat_model)


if __name__ == "__main__":
    main()
