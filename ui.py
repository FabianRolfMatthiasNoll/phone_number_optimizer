"""
ttk-GUI ohne Persistenz – zeigt dynamisch Mobil-/Ortskennzahl,
sowie Land und Region / Carrier.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from parser import parse_phone_number
from config import DEFAULT_COUNTRY


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Phone Number Optimizer")
        self.geometry("420x310")
        self.resizable(False, False)
        self.configure(padx=16, pady=12)
        self._build_widgets()

    # ------------------------------------------------------------------ #
    #  UI-Aufbau
    # ------------------------------------------------------------------ #
    def _build_widgets(self) -> None:
        # Eingabezeile
        input_row = ttk.Frame(self)
        input_row.grid(sticky="we")
        input_row.columnconfigure(1, weight=1)

        ttk.Label(input_row, text="Telefonnummer:").grid(row=0, column=0, sticky="e")
        self.in_entry = ttk.Entry(input_row)
        self.in_entry.grid(row=0, column=1, sticky="we", padx=6)
        self.in_entry.focus()
        ttk.Button(input_row, text="Analysieren", command=self._analyse).grid(
            row=0, column=2
        )

        # Ergebnisfeld
        out = ttk.LabelFrame(self, text="Analyse")
        out.grid(sticky="we", pady=10)
        for i in range(2):
            out.columnconfigure(i, weight=1)

        self._fields = {}
        row = 0

        # Landesvorwahl
        ttk.Label(out, text="Landes­vorwahl:").grid(row=row, column=0, sticky="e")
        e = ttk.Entry(out, width=28)
        e.grid(row=row, column=1, sticky="we", pady=2)
        self._fields["country_code"] = e
        row += 1

        # (Orts|Mobil)-Kennzahl
        self._label_ac = tk.StringVar(value="Ortskennzahl")
        ttk.Label(out, textvariable=self._label_ac).grid(row=row, column=0, sticky="e")
        e = ttk.Entry(out, width=28)
        e.grid(row=row, column=1, sticky="we", pady=2)
        self._fields["area_code"] = e
        row += 1

        # Nummer
        ttk.Label(out, text="Nummer:").grid(row=row, column=0, sticky="e")
        e = ttk.Entry(out, width=28)
        e.grid(row=row, column=1, sticky="we", pady=2)
        self._fields["local_number"] = e
        row += 1

        # Durchwahl
        ttk.Label(out, text="Durchwahl:").grid(row=row, column=0, sticky="e")
        e = ttk.Entry(out, width=28)
        e.grid(row=row, column=1, sticky="we", pady=2)
        self._fields["extension"] = e
        row += 1

        ttk.Separator(out).grid(row=row, columnspan=2, sticky="we", pady=4)
        row += 1

        # E.164
        ttk.Label(out, text="E.164:").grid(row=row, column=0, sticky="e")
        self.e164_var = tk.StringVar()
        ttk.Entry(out, textvariable=self.e164_var, state="readonly").grid(
            row=row, column=1, sticky="we"
        )
        row += 1

        # Lesbar
        ttk.Label(out, text="Lesbar:").grid(row=row, column=0, sticky="e")
        self.human_var = tk.StringVar()
        ttk.Entry(out, textvariable=self.human_var, state="readonly").grid(
            row=row, column=1, sticky="we"
        )
        row += 1

        # Land
        ttk.Label(out, text="Land:").grid(row=row, column=0, sticky="e")
        self.country_var = tk.StringVar()
        ttk.Entry(out, textvariable=self.country_var, state="readonly").grid(
            row=row, column=1, sticky="we"
        )
        row += 1

        # Region / Carrier
        ttk.Label(out, text="Region / Carrier:").grid(row=row, column=0, sticky="e")
        self.region_var = tk.StringVar()
        ttk.Entry(out, textvariable=self.region_var, state="readonly").grid(
            row=row, column=1, sticky="we"
        )

        # Statuszeile
        self.status = tk.StringVar()
        ttk.Label(self, textvariable=self.status, foreground="#c00").grid(
            sticky="w", pady=(4, 0)
        )

    # ------------------------------------------------------------------ #
    #  Callback
    # ------------------------------------------------------------------ #
    def _analyse(self) -> None:
        raw = self.in_entry.get()
        try:
            res = parse_phone_number(raw, DEFAULT_COUNTRY)
        except ValueError as err:
            messagebox.showerror("Fehler", str(err))
            self.status.set(str(err))
            return

        # Label dynamisch setzen
        if res["country_code"] == "+49" and res["area_code"].startswith("1"):
            self._label_ac.set("Mobil­kennzahl")
        else:
            self._label_ac.set("Ortskennzahl")

        # Felder befüllen
        for k, v in res.items():
            if k in self._fields:
                f = self._fields[k]
                f.delete(0, tk.END)
                f.insert(0, v)

        self.e164_var.set(res["e164"])
        self.human_var.set(res["human"])
        self.country_var.set(res["country_name"])
        self.region_var.set(res["area_desc"] or res["carrier_name"])
        self.status.set("")


def run() -> None:
    App().mainloop()
