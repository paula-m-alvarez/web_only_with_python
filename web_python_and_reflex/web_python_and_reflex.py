import reflex as rx

from web_python_and_reflex import style
from web_python_and_reflex.state import state


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            state.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            value=state.question,
            on_change=state.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=state.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)