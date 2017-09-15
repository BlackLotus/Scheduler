#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Scheduler - Task scheduling and calendar
Copyright 2017 Juliette Monsel <j_4321@protonmail.com>
code based on http://effbot.org/zone/tkinter-autoscrollbar.htm

Scheduler is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Scheduler is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


Notification class and script
"""

from tkinter import Tk
from tkinter.ttk import Label, Button, Style
import sys

class Notification(Tk):
    def __init__(self, text=''):
        Tk.__init__(self)
        self.overrideredirect(True)
        self.withdraw()
        self.columnconfigure(0, weight=1)
        self.attributes('-type', 'notification')
        self.attributes('-alpha', 0.75)
        self.configure(bg='black')
        self.style = Style(self)
        self.style.theme_use('clam')
        self.style.configure('notif.TLabel', background='black', foreground='white')
        self.style.configure('notif.TButton', background='#252525',
                        darkcolor='black', lightcolor='#4C4C4C',
                        bordercolor='#737373', foreground='white')
        self.style.map('notif.TButton', background=[('active', '#4C4C4C')])
        Label(self, text=text, style='notif.TLabel').grid(row=0, column=0, padx=10, pady=10)
        Button(self, text='Ok', command=self.destroy,
               style='notif.TButton').grid(row=1, column=0, padx=10, pady=(0, 10))
        self.blink_alternate = True
        self.deiconify()
        self.update_idletasks()
        self.geometry('%ix%i+0+0' % (self.winfo_screenwidth(), self.winfo_height()))
        self.after(500, self.blink)

    def blink(self):
        if self.blink_alternate:
            self.style.configure('notif.TButton', foreground='red', background='gray')
            self.style.configure('notif.TLabel', foreground='red', background='gray')
            self.configure(bg='gray')
        else:
            self.style.configure('notif.TButton', foreground='white', background='#252525')
            self.style.configure('notif.TLabel', foreground='white', background='black')
            self.configure(bg='black')
        self.blink_alternate = not self.blink_alternate
        self.after(500, self.blink)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = Notification(sys.argv[1])
        n.mainloop()
    else:
        n = Notification('test')
        n.mainloop()