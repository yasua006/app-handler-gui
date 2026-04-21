from subprocess import run as sprun, CompletedProcess
import tkinter as tk
import atexit


def execution_permission() -> None:
    sprun(["chmod", "+x", "./main.bash"])


def open_app(app_name: str) -> None:
    # print(f"Opening {app_name}...")

    open_option = "1"
    sprun(["./main.bash"], input=f"{open_option}\n{app_name}\n", text=True)

def close_app(app_name: str) -> None:
    # print(f"Closing {app_name}...")

    close_option = "2"
    sprun(["./main.bash"], input=f"{close_option}\n{app_name}\n", text=True)

def show_privilege() -> str:
    show_option = "4"
    result: CompletedProcess[str] = sprun(["./main.bash"], input=f"{show_option}\n",
        text=True, capture_output=True)

    return result.stdout

def switch_privilege() -> None:
    switch_option = "5"
    sprun(["./main.bash"], input=f"{switch_option}\n", text=True)

def show_supported_platforms() -> str:
    show_sp_option = "6"
    result: CompletedProcess[str] = sprun(["./main.bash"], input=f"{show_sp_option}\n",
        text=True, capture_output=True)

    return result.stdout

def handle_switch(label: tk.Label) -> None:
    switch_privilege()
    new_privilege_lvl: str = show_privilege()
    label.config(text=f"Privilege: {new_privilege_lvl}")


def main() -> None:
    execution_permission()

    privilege_lvl: str = show_privilege()
    what_app: str = input("App name to manage: ")

    root = tk.Tk()
    root.attributes("-topmost", True)

    root.title("App Handler GUI")
    root.configure(bg="black")
    root.minsize(width=500, height=500)
    root.maxsize(width=600, height=600)
    root.geometry("550x550")
    
    frame = tk.Frame(root, width=200, height=200)
    frame.pack(padx=100, pady=100) 
    
    title = tk.Label(frame, text=f"Managing {what_app}",
        font=("TkDefaultFont", 16, "bold"))
    title.pack()

    show_privilege_desc = tk.Label(frame, text=f"Privilege: {privilege_lvl}")
    show_privilege_desc.pack(pady=25)

    open_app_btn = tk.Button(frame, text="Open",
        command=lambda: open_app(what_app))
    open_app_btn.pack()

    close_app_btn = tk.Button(frame, text="Close",
        command=lambda: close_app(what_app))
    close_app_btn.pack()

    switch_privilege_btn = tk.Button(frame, text="Switch privilege",
        command=lambda: handle_switch(show_privilege_desc))
    switch_privilege_btn.pack()

    supported_platforms = tk.Label(frame, text=show_supported_platforms())
    supported_platforms.pack()

    root.mainloop()

@atexit.register
def main_window_closed() -> None:
    print("\nClosed App Handler GUI\n")

if __name__ == '__main__':
    main()
