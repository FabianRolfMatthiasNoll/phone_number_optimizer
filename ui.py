"""
Lean ttk-GUI – no persistence, no extra deps.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from parser import parse_phone_number
from config import DEFAULT_COUNTRY


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Phone Number Optimizer")
        self.geometry("420x250")
        self.resizable(False, False)  # kompakt & fix
        self.configure(padx=16, pady=12)  # Rand­abstand global
        self._build_widgets()

    # ------------------------------------------------------------------
    #   UI-Aufbau
    # ------------------------------------------------------------------
    def _build_widgets(self) -> None:
        # --- Eingabezeile ------------------------------------------------
        input_row = ttk.Frame(self)
        input_row.grid(sticky="we")
        input_row.columnconfigure(1, weight=1)  # Entry dehnt sich

        ttk.Label(input_row, text="Telefonnummer:").grid(row=0, column=0, sticky="e")
        self.in_entry = ttk.Entry(input_row)
        self.in_entry.grid(row=0, column=1, sticky="we", padx=6)
        self.in_entry.focus()
        ttk.Button(input_row, text="Analysieren", command=self._analyse).grid(
            row=0, column=2
        )

        # --- Ergebnisfeld ------------------------------------------------
        out = ttk.LabelFrame(self, text="Analyse")
        out.grid(sticky="we", pady=10)
        for i in range(2):
            out.columnconfigure(i, weight=1)

        self._fields = {}
        row = 0
        for label, key in (
            ("Landes­vorwahl", "country_code"),
            ("Ortskennzahl", "area_code"),
            ("Nummer", "local_number"),
            ("Durchwahl", "extension"),
        ):
            ttk.Label(out, text=f"{label}:").grid(row=row, column=0, sticky="e")
            e = ttk.Entry(out, width=28)
            e.grid(row=row, column=1, sticky="we", pady=2)
            self._fields[key] = e
            row += 1

        ttk.Separator(out).grid(row=row, columnspan=2, sticky="we", pady=4)
        row += 1

        ttk.Label(out, text="E.164:").grid(row=row, column=0, sticky="e")
        self.e164_var = tk.StringVar()
        ttk.Entry(out, textvariable=self.e164_var, state="readonly").grid(
            row=row, column=1, sticky="we"
        )
        row += 1

        ttk.Label(out, text="Lesbar:").grid(row=row, column=0, sticky="e")
        self.human_var = tk.StringVar()
        ttk.Entry(out, textvariable=self.human_var, state="readonly").grid(
            row=row, column=1, sticky="we"
        )

        # --- Statuszeile -------------------------------------------------
        self.status = tk.StringVar()
        ttk.Label(self, textvariable=self.status, foreground="#c00").grid(
            sticky="w", pady=(4, 0)
        )

    # ------------------------------------------------------------------
    #   Callback
    # ------------------------------------------------------------------
    def _analyse(self) -> None:
        raw = self.in_entry.get()
        try:
            res = parse_phone_number(raw, DEFAULT_COUNTRY)
        except ValueError as err:
            messagebox.showerror("Fehler", str(err))
            self.status.set(str(err))
            return

        for k, v in res.items():
            if k in self._fields:
                self._fields[k].delete(0, tk.END)
                self._fields[k].insert(0, v)
        self.e164_var.set(res["e164"])
        self.human_var.set(res["human"])
        self.status.set("")


def run() -> None:
    App().mainloop()
