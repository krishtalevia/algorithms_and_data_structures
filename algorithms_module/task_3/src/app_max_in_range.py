from tkinter import *
from tkinter import ttk

class App:

    def __init__(self, root: Tk):
        self.__root_window = root
        self.user_input_ui = None
        self.output_result = None
        self.__config_window()
        self.__build_main_screen()

    def run(self):
        self.__root_window.mainloop()

    def __config_window(self):
        self.__root_window.title('Max in range')
        self.__root_window.geometry('800x400')
        self.__root_window.resizable(False, False)

    def __build_main_screen(self):
        main_frame = Frame()

        input_message_ui = ttk.Label(
            master=main_frame,
            text='----',
            font=(("Arial", 18))
        )
        input_message_ui.grid(row=0, column=0)

        self.user_input_ui = ttk.Entry(master=main_frame)
        self.user_input_ui.grid(row=0, column=1)

        solver_button = ttk.Button(master=main_frame, text="Solver")
        solver_button.grid(row=1, columnspan=2)

        solver_button.config(command=self.on_click_solver_button_handler)

        output_message = ttk.Label(
            master=main_frame,
            text="Output result:"
        )
        output_message.grid(row=2, column=0)

        self.output_result = ttk.Label(master=main_frame)
        self.output_result.grid(row=2, column=1)

        main_frame.pack()

    def on_click_solver_button_handler(self):
        text = self.user_input_ui.get()

        if text == "":
            print("error!")
            return

        result = count_ones(int(text))

        print(result)

self.output_result.config(text=str(result))


def main():
    root = Tk()  # root window

    app = App(root)

    app.run()


if __name__ == "__main__":
    main()