from tkinter import *
from tkinter import ttk
from tkinter import messagebox

TIMES = []
HOURS = []
MINUTES = []
SECONDS = []
i = 0
n = 1
time_label = None
labels = []

def add_times():
    # pass
    # time_frame = ttk.LabelFrame(root, height=200, width=600, padding=(20, 20), relief=RAISED, text="Course Times")
    # time_frame.grid(row=11, column=1, columnspan=6, padx=30, pady=30)
    global i, n, time_label, time_info
    entered_hour = hour_entry.get()
    entered_minute = minutes_entry.get()
    entered_seconds = seconds_entry.get()
    if len(entered_hour) == 1:
        entered_hour = "0" + entered_hour
    elif len(entered_hour) == 0:
            entered_hour = "00"
    if len(entered_minute) == 1:
        entered_minute = "0" + entered_minute
    elif len(entered_minute) == 0:
        entered_minute = "00"
    if len(entered_seconds) == 1:
        entered_seconds = "0" + entered_seconds
    elif len(entered_seconds) == 0:
        entered_seconds = "00"
    time_info = entered_hour + 'h: ' + entered_minute + 'm: ' + entered_seconds + 's'
    TIMES.append(time_info)
    HOURS.append(entered_hour)
    MINUTES.append(entered_minute)
    SECONDS.append(entered_seconds)

    if len(TIMES) >= 61:
        error = messagebox.showerror('Error', "I'm sorry, I cannot calculate any more values!")
        del TIMES[-1]
        return error

    # if len(TIMES) <= 10:
    #     i += 1
    #     n += 1
    #     time_label = Label(time_frame, text=str(n)+'.  '+time_info+' ')
    #     time_label.grid(row=i, column=1, padx=10, pady=10)
    # if (len(TIMES) > 10) and (len(TIMES) <= 20):
    #     i = 1
    #     n = 10
    #     for time in TIMES[10:20]:
    #         n += 1
    #         time_label = Label(time_frame, text=str(n)+'.  '+time+' ')
    #         time_label.grid(row=i, column=2, padx=10, pady=10)
    #         i += 1
    # if (len(TIMES) > 20) and (len(TIMES) <= 30):
    #     i = 1
    #     n = 20
    #     for time in TIMES[20:30]:
    #         n += 1
    #         time_label = Label(time_frame, text=str(n)+'.  '+time+' ')
    #         time_label.grid(row=i, column=3, padx=10, pady=10)
    #         i += 1
    # if (len(TIMES) > 30) and (len(TIMES) <= 40):
    #     i = 1
    #     n = 30
    #     for time in TIMES[30:40]:
    #         n += 1
    #         time_label = Label(time_frame, text=str(n)+'.  '+time+' ')
    #         time_label.grid(row=i, column=4, padx=10, pady=10)
    #         i += 1
    # if (len(TIMES) > 40) and (len(TIMES) <= 50):
    #     i = 1
    #     n = 40
    #     for time in TIMES[40:50]:
    #         n += 1
    #         time_label = Label(time_frame, text=str(n)+'.  '+time+' ')
    #         time_label.grid(row=i, column=5, padx=10, pady=10)
    #         i += 1
    add_times_labels()
    hour_entry.delete(0, END)
    minutes_entry.delete(0, END)
    seconds_entry.delete(0, END)
    return TIMES, time_label, time_info, HOURS, MINUTES, SECONDS


def add_times_labels():
    global i, n, time_label, time_info, labels
    if len(TIMES) <= 15:
        i += 1
        time_label = Label(time_frame1, text=str(n)+'.  '+time_info+' ')
        labels.append(time_label)
        time_label.grid(row=i, column=0, padx=5, pady=5)
        n += 1
    if (len(TIMES) > 15) and (len(TIMES) <= 30):
        i = 1
        n = 16
        for time in TIMES[15:30]:
            time_label = Label(time_frame1, text=str(n)+'.  '+time+' ')
            labels.append(time_label)
            time_label.grid(row=i, column=1, padx=5, pady=5)
            i += 1
            n += 1
    if (len(TIMES) > 30) and (len(TIMES) <= 45):
        i = 1
        n = 31
        for time in TIMES[30:45]:
            time_label = Label(time_frame1, text=str(n)+'.  '+time+' ')
            labels.append(time_label)
            labels.append(time_label)
            time_label.grid(row=i, column=2, padx=5, pady=5)
            i += 1
            n += 1
    if (len(TIMES) > 45) and (len(TIMES) <= 60):
        i = 1
        n = 46
        for time in TIMES[45:60]:
            time_label = Label(time_frame1, text=str(n)+'.  '+time+' ')
            labels.append(time_label)
            time_label.grid(row=i, column=3, padx=5, pady=5)
            i += 1
            n += 1
    # if (len(TIMES) > 40) and (len(TIMES) <= 50):
    #     i = 1
    #     n = 40
    #     for time in TIMES[40:50]:
    #         n += 1
    #         time_label = Label(time_frame5, text=str(n)+'.  '+time+' ')
    #         labels.append(time_label)
    #         time_label.grid(row=i, column=5, padx=5, pady=5)
    #         i += 1
    return TIMES, time_label, time_info, HOURS, MINUTES, SECONDS, labels, n


def remove_time():
    # pass
    global labels, n
    index = int(remove_entry.get())
    n = index
    labels[index-1].destroy()
    del labels[index-1]
    print(labels)
    print(len(labels))
    for label in labels[index-1:]:
        label.config(text=str(n)+'.  '+TIMES[n]+' ')
        n += 1
    del TIMES[index-1]
    n = len(TIMES) + 1
    return n


def clear_list():
    # pass
    global n
    for label in labels[:]:
        label.grid_forget()
        del TIMES[:]
        del labels[:]
    n = 0
    return n


def calculate():
    # pass
    total_hours = 0
    total_minutes = 0
    total_seconds = 0
    for hours in HOURS:
        hour = int(hours)
        total_hours += hour
    for minutes in MINUTES:
        minute = int(minutes)
        total_minutes += minute
    for seconds in SECONDS:
        second = int(seconds)
        total_seconds += second

    total_sec = total_seconds % 60
    final_total_minutes = ((total_minutes % 60) + (total_seconds // 60)) % 60
    final_total_hours = ((total_hours % 24) + (total_minutes // 60)  + (final_total_minutes // 60)) % 24
    days = (total_hours // 24 + total_minutes // 60 // 24 + total_seconds // 60 // 60 // 24) + final_total_hours // 24

    if len(TIMES) == 0:
        total_time = "The total time is 0 day/s, 0 hour/s, 0 minute/s, " \
                     "and 0 seconds"
    else:
        total_time = "The total time is {} day/s, {} hour/s, {} minute/s, " \
                 "and {} seconds".format(days, final_total_hours, final_total_minutes, total_sec)
    total_time_label.config(text=total_time)
    total_time_label.pack()


def show_times():
    # pass
    print(TIMES)
    print(len(TIMES))
    for index, val in enumerate(labels):
        print(index, val)


root = Tk()
root.geometry("750x950+300+20")
# root.iconbitmap("course_calc.ico")
root.title("Course Time Calculator")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)

# Create LABELS and ENTRIES for TIME
hours_label = Label(root, text="Hours")
hour_entry = Entry(root)
minutes_label = Label(root, text="Minutes")
minutes_entry = Entry(root)
seconds_label = Label(root, text="Seconds")
seconds_entry = Entry(root)
add_button = Button(root, text="Add", bd=5, font=("monospace", 8, "bold", "underline"), fg="#009", command=add_times,
                    width=15)
calculate_button = Button(root, text="Calculate course time", bd=5, command=calculate,
                          font=("monospace", 8, "bold", "underline"), fg="#009")
# show_list_button = Button(root, text="Show List", command=show_times, bd=5,
#                           font=("monospace", 8, "bold", "underline"), fg="#009")        # Tester button
clear_list_button = Button(root, text="Clear List", command=clear_list, bd=5,
                           font=("monospace", 8, "bold", "underline"), fg="#009")
remove_entry = Entry(root)
remove_button = Button(root, text="Remove time #", command=remove_time, bd=5,
                       font=("monospace", 8, "bold", "underline"), fg="#009")
main_time_frame = ttk.LabelFrame(root, height=200, width=600,  padding=(5, 5), relief=RAISED, text="Course Times")
time_frame1 = ttk.Frame(main_time_frame)
time_frame2 = ttk.Frame(main_time_frame)
time_frame3 = ttk.Frame(main_time_frame)
time_frame4 = ttk.Frame(main_time_frame)
time_frame5 = ttk.Frame(main_time_frame)

total_course_time = ttk.LabelFrame(root, height=100, width=600, padding=(20, 20),
                                   relief=RAISED, text="Total Course Times")
hours_label.grid(row=0, column=0, sticky="e")
minutes_label.grid(row=1, column=0, sticky="e")
seconds_label.grid(row=2, column=0, sticky="e")
hour_entry.grid(row=0, column=1, pady=10)
minutes_entry.grid(row=1, column=1, pady=10)
seconds_entry.grid(row=2, column=1, pady=10)
add_button.grid(row=0, column=2, padx=10, pady=10)
calculate_button.grid(row=1, column=2)
# show_list_button.grid(row=2, column=2, padx=10)       # Tester button
clear_list_button.grid(row=2, column=2, padx=10)
remove_entry.grid(row=3, column=2, padx=0, pady=20)
remove_button.grid(row=3, column=1)
main_time_frame.grid(row=4, column=0, columnspan=5, padx=0, pady=0)
time_frame1.grid(row=0, column=0)
time_frame2.grid(row=0, column=1)
time_frame3.grid(row=0, column=2)
time_frame4.grid(row=0, column=3)
time_frame5.grid(row=0, column=4)
total_course_time.grid(row=5, column=0, columnspan=3, padx=0, pady=30)
total_time_label = Label(total_course_time, padx=40, pady=40)
root.mainloop()
