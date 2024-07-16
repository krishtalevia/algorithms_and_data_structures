from tkinter import *
from tkinter import ttk
from rotate_and_reverse import *

class App:

    def __init__(self, root: Tk):
        self.__root_window = root
        self.user_input_ui = None
        self.output_result = None
        self.k_num_ui = None
        self.__config_window()
        self.__build_main_screen()

    def run(self):
        self.__root_window.mainloop()

    def __config_window(self):
        self.__root_window.title('Rotate and reverse')
        self.__root_window.geometry('800x400')
        self.__root_window.resizable(False, False)

    def __build_main_screen(self):
        main_frame = Frame()

        input_message_ui = ttk.Label(
            master=main_frame,
            text='Введите список:',
            font=("Arial", 18)
        )
        input_message_ui.grid(row=0, column=0, pady=10)

        self.user_input_ui = ttk.Entry(master=main_frame, width=40)
        self.user_input_ui.grid(row=0, column=1, pady=10)

        k_num_label = ttk.Label(
            master=main_frame,
            text='Кол-во сдвигов:',
            font=('Arial', 14)
        )
        k_num_label.grid(row=1, column=0, pady=10)

        self.k_num_ui = ttk.Entry(master=main_frame, width=20)
        self.k_num_ui.grid(row=1, column=1, pady=10)

        solver_button = ttk.Button(master=main_frame, text='Решить')
        solver_button.grid(row=3, columnspan=2)

        solver_button.config(command=self.on_click_solver_button_handler)

        output_message = ttk.Label(
            master=main_frame,
            text='Результат:',
            font=('Arial', 14)
        )
        output_message.grid(row=4, column=0, pady=10)

        self.output_result = ttk.Label(master=main_frame, font=('Arial', 14))
        self.output_result.grid(row=4, column=1, pady=10)

        main_frame.pack()

    def on_click_solver_button_handler(self):
        list_text = self.user_input_ui.get()
        k_num_text = self.k_num_ui.get()

        try:
            if not list_text or not k_num_text:
                self.output_result.config(text='Все поля должны быть заполнены!')
                return

            lst = list_text.split(',')
            for i in range(0, len(lst), 1):
                lst[i] = int(lst[i])

            k = int(k_num_text)

            result = rotate_and_reverse(lst, k)
            self.output_result.config(text=f'{result}')

        except Exception:
            self.output_result.config(text='Ошибка!')

def main():
    root = Tk()

    app = App(root)

    app.run()


if __name__ == "__main__":
    main()