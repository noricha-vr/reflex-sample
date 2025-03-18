"""Welcome to Reflex! This app implements a simple counter."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app's state."""
    count: int = 0

    def increment(self):
        """Increment the count."""
        self.count += 1


def index() -> rx.Component:
    return rx.vstack(
        rx.heading(State.count),
        rx.button("カウントアップ", on_click=State.increment),
    )


app = rx.App()
app.add_page(index)
