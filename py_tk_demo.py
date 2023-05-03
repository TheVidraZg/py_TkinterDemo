import tkinter as tk
from app_cons import *
from db_sql_alchemyrepo import db_init

movies_list = [
    'Gospodar Prstenova',
    'Hobit',
    '1.Maj, 3.dan',
    'Batman',
    'Matrix',
    'Sam u kuci'
]


# FUNKCIJE

def run_app():
    pass

def btn_load_handler():
    lb_movies_var.set(value=movies_list)
    print(f'Pozdrav iz "Btn_load_funkcije" !!!')

def btn_save_handler():
    print(f'Pozdrav iz "Btn_save_funkcije" !!!')

def btn_cancel_handler():
    lb_movies_var.set(value=[])
    print(f'Pozdrav iz "Btn_cancel_funkcije" !!!')

def lb_select_handler(event):
    index = event.widget.curselection()
    value = ''
    for i in index:
        value += ' ' + lb_movies.get(i)
    print(f'{event}')
    print(f'{event.widget}')
    print(f'{index[0]} - {value}')
    lbl_display_element_var.set(f'{index[0]} - {value}')




main_window = tk.Tk()
main_window.title('Python Tkinter demo aplikacija')
main_window.geometry('600x600')

#region APP TITLE
lbl_app_title = tk.Label(main_window, 
                         text='Dobro dosli u Tkinter demo aplikaciju!',
                         font=TITLE_FONT)
lbl_app_title.pack(padx=TITLE_PADX, pady=TITLE_PADY)
#endregion APP TITLE

#region HEADER

frm_header = tk.LabelFrame(main_window,
                           text='Akcije',
                           font=SUBTITLE_FONT)
frm_header.pack(padx=BODY_PADX, pady=BODY_PADY, fill=tk.BOTH)
frm_header.columnconfigure(index= 0, weight=1)
frm_header.columnconfigure(index= 1, weight=4)
frm_header.columnconfigure(index= 2, weight=1)




btn_load= tk.Button(frm_header,
                    text='Ucitaj podatke',
                    command=btn_load_handler,
                    font=BTN_FONT)
btn_load.grid(row=0, column=0,
              sticky=tk.EW,
              padx=BTN_PADX, pady=BTN_PADY,
              ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_save= tk.Button(frm_header,
                    text='Snimi podatke',
                    command=btn_save_handler,
                    font=BTN_FONT)
btn_save.grid(row=0, column=1,
              sticky=tk.EW,
              padx=BTN_PADX, pady=BTN_PADY,
              ipadx=BTN_IPADX, ipady=BTN_IPADY)

btn_cancel= tk.Button(frm_header,
                    text='Odustani',
                    command=btn_cancel_handler,
                    font=BTN_FONT)
btn_cancel.grid(row=0, column=2,
                sticky=tk.EW,
              padx=BTN_LASTPADX, pady=BTN_PADY,
              ipadx=BTN_IPADX, ipady=BTN_IPADY)

#endregion HEADER


#region BODY
frm_body = tk.LabelFrame(main_window,
                         text='Glavni okvir',
                         font=BODY_FONT)
frm_body.pack(padx=BODY_PADX, pady=BODY_PADY, fill='both')

lb_movies_var = tk.StringVar()

lb_movies = tk.Listbox(frm_body,
                       height=8,
                       width=50,
                       font=BODY_FONT,
                       listvariable=lb_movies_var)
lb_movies.pack(padx=BODY_PADX, pady=BODY_PADY,
               fill='both')
lb_movies.bind('<ButtonRelease-1>', lb_select_handler)
#endregion


#region FOOTER
lbl_display_element_var=tk.StringVar()
lbl_display_element_var.set('Prostor za prikaz elemenata')
lbl_display_element = tk.Label(main_window,
                               textvariable=lbl_display_element_var,
                               font=SUBTITLE_FONT)
lbl_display_element.pack(padx=BODY_PADX, pady=TITLE_PADY,
                         fill=tk.BOTH)
#endregion

main_window.mainloop()

if __name__ = '__main__':
    run_app()
    db_init()