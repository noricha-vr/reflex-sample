"""Welcome to Reflex! This app implements a simple counter."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app's state."""
    count: int = 0

    def increment(self):
        """Increment the count."""
        self.count += 1

    def decrement(self):
        """Decrement the count."""
        self.count = max(0, self.count - 1)


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Modern Counter App",
                class_name="text-3xl font-bold text-indigo-600 mb-6",
            ),
            rx.flex(
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Current Count",
                            class_name="text-lg font-medium text-gray-600",
                        ),
                        rx.heading(
                            State.count,
                            class_name="text-5xl font-bold text-indigo-500",
                        ),
                        class_name="mb-6",
                    ),
                    class_name="bg-white p-8 rounded-lg shadow-md",
                ),
                direction="column",
                class_name="items-center",
            ),
            rx.hstack(
                rx.button(
                    rx.icon("minus"),
                    on_click=State.decrement,
                    class_name="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-l-md transition-colors",
                ),
                rx.button(
                    rx.icon("plus"),
                    on_click=State.increment,
                    class_name="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-r-md transition-colors",
                ),
                spacing="0",
                class_name="mt-6",
            ),
            rx.text(
                "Built with Reflex and Tailwind CSS",
                class_name="text-sm text-gray-500 mt-8",
            ),
            rx.link(
                "View Cinderella Story Landing Page",
                href="/lp",
                class_name="text-indigo-600 hover:text-indigo-800 font-medium mt-4 inline-block transition-colors",
            ),
            spacing="6",
            class_name="py-16 max-w-md mx-auto",
        ),
        class_name="min-h-screen bg-gray-50",
    )


def lp() -> rx.Component:
    return rx.box(
        # Hero Section
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "The Cinderella Story of Web Development",
                        size="1",
                        class_name="text-4xl md:text-5xl font-bold text-center text-indigo-600 mb-4"
                    ),
                    rx.text(
                        "Once upon a time, web development was complex and time-consuming...",
                        class_name="text-xl text-center text-gray-600 mb-8"
                    ),
                    rx.button(
                        "Begin the Magic",
                        class_name="bg-indigo-600 hover:bg-indigo-700 text-white px-8 py-3 rounded-full text-lg font-medium transition-colors",
                        size="3",
                    ),
                    spacing="6",
                    align="center",
                ),
                class_name="max-w-4xl mx-auto px-6 py-24",
            ),
            class_name="bg-gradient-to-b from-purple-50 to-indigo-100 min-h-screen",
        ),
        
        # Story Part 1: Before Reflex
        rx.box(
            rx.container(
                rx.flex(
                    rx.box(
                        rx.image(
                            src="https://images.unsplash.com/photo-1555066931-4365d14bab8c",
                            alt="Frustrated developer",
                            class_name="rounded-lg shadow-lg",
                        ),
                        class_name="w-full md:w-1/2 p-4",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "The Hardship",
                                class_name="text-3xl font-bold text-indigo-700 mb-4"
                            ),
                            rx.text(
                                "Our developer, Ella, worked tirelessly with complex frameworks and endless boilerplate code. While others enjoyed building beautiful applications, she was stuck with mundane tasks and technical limitations.",
                                class_name="text-lg text-gray-700 mb-4"
                            ),
                            rx.text(
                                "Her dreams of creating elegant, responsive web applications seemed impossible with the tools she had.",
                                class_name="text-lg text-gray-700"
                            ),
                            align="start",
                            spacing="4",
                        ),
                        class_name="w-full md:w-1/2 p-4",
                    ),
                    direction="column",
                    class_name="items-center md:flex-row",
                ),
                class_name="max-w-6xl mx-auto px-6 py-20",
            ),
            class_name="bg-white",
        ),
        
        # Story Part 2: The Magic (Reflex)
        rx.box(
            rx.container(
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "The Magical Encounter",
                                class_name="text-3xl font-bold text-indigo-700 mb-4"
                            ),
                            rx.text(
                                "Then, as if by magic, Reflex appeared in her life. Like a fairy godmother, Reflex transformed her development experience with its Python-based simplicity and powerful capabilities.",
                                class_name="text-lg text-gray-700 mb-4"
                            ),
                            rx.text(
                                "\"With reactive state management and beautiful components, you shall build the application of your dreams!\" promised Reflex.",
                                class_name="text-lg italic text-indigo-600"
                            ),
                            align="start",
                            spacing="4",
                        ),
                        class_name="w-full md:w-1/2 p-4 order-2 md:order-1",
                    ),
                    rx.box(
                        rx.image(
                            src="https://images.unsplash.com/photo-1633356122544-f134324a6cee",
                            alt="Magical transformation",
                            class_name="rounded-lg shadow-lg",
                        ),
                        class_name="w-full md:w-1/2 p-4 order-1 md:order-2",
                    ),
                    direction="column",
                    class_name="items-center md:flex-row",
                ),
                class_name="max-w-6xl mx-auto px-6 py-20",
            ),
            class_name="bg-indigo-50",
        ),
        
        # Story Part 3: The Transformation
        rx.box(
            rx.container(
                rx.flex(
                    rx.box(
                        rx.image(
                            src="https://images.unsplash.com/photo-1498050108023-c5249f4df085",
                            alt="Beautiful application",
                            class_name="rounded-lg shadow-lg",
                        ),
                        class_name="w-full md:w-1/2 p-4",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "The Transformation",
                                class_name="text-3xl font-bold text-indigo-700 mb-4"
                            ),
                            rx.text(
                                "With Reflex, Ella transformed her code into beautiful, responsive web applications. Components came together seamlessly, state management was intuitive, and her productivity soared.",
                                class_name="text-lg text-gray-700 mb-4"
                            ),
                            rx.text(
                                "She no longer had to struggle with JavaScript frameworks or complex toolchains. Python's elegance combined with Reflex's power made her development experience magical.",
                                class_name="text-lg text-gray-700"
                            ),
                            align="start",
                            spacing="4",
                        ),
                        class_name="w-full md:w-1/2 p-4",
                    ),
                    direction="column",
                    class_name="items-center md:flex-row",
                ),
                class_name="max-w-6xl mx-auto px-6 py-20",
            ),
            class_name="bg-white",
        ),
        
        # Story Part 4: The Happy Ending
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Happily Ever After",
                        class_name="text-3xl font-bold text-indigo-700 mb-6"
                    ),
                    rx.text(
                        "Ella's applications impressed everyone in the kingdom of web development. Her once impossible dreams became reality, and she continued to build amazing experiences with her trusted companion, Reflex.",
                        class_name="text-xl text-center text-gray-700 mb-8 max-w-3xl"
                    ),
                    rx.text(
                        "Unlike Cinderella's magic that ended at midnight, Reflex's magic continues with every project, empowering developers to create their own happily ever after.",
                        class_name="text-xl text-center text-indigo-600 mb-10 max-w-3xl"
                    ),
                    rx.button(
                        "Start Your Reflex Journey",
                        class_name="bg-indigo-600 hover:bg-indigo-700 text-white px-8 py-4 rounded-full text-lg font-medium transition-colors",
                        size="3",
                    ),
                    align="center",
                    spacing="6",
                ),
                class_name="max-w-6xl mx-auto px-6 py-24",
            ),
            class_name="bg-gradient-to-t from-purple-50 to-indigo-100",
        ),
        
        # Footer
        rx.box(
            rx.container(
                rx.vstack(
                    rx.text(
                        "Built with Reflex - Where Python Magic Meets Web Development",
                        class_name="text-center text-gray-500"
                    ),
                    rx.text(
                        "Images from Unsplash • Story inspired by Cinderella",
                        class_name="text-center text-gray-400 text-sm"
                    ),
                    align="center",
                    spacing="2",
                ),
                class_name="max-w-6xl mx-auto px-6 py-8",
            ),
            class_name="bg-gray-100",
        ),
    )

app = rx.App()
app.add_page(index)
app.add_page(lp, route="/lp")
