# Alien Symbolic Interpreter (Prototype v12 - GUI Version with Enhanced Output and Mandala)
# Each symbol maps to a concept or function with simulated behavior

import random
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from datetime import datetime
import math
import json
import os

# Symbol-function mapping (with simulated behaviors)
symbols = {
    "●": lambda ctx: ctx.update({"●": "Universe Initialized (Big Bang Triggered)"}),
    "◐": lambda ctx: ctx.update({"◐": "Duality Formed (Half-State Observed)"}),
    "∴": lambda ctx: ctx.update({"∴": [f"State {i}: Energy Level {random.randint(1, 100)}" for i in range(max(2, random.randint(2, 5)))]}),
    "✧": lambda ctx: ctx.update({"✧": f"State Collapsed to {random.choice(ctx.get('∴', ['Unknown State']))}"}),
    "Ψ": lambda ctx: ctx.update({"Ψ": "Quantum Potential Activated"}),
    "∅": lambda ctx: ctx.update({"∅": "Void State (No Energy)"}),
    "꩜": lambda ctx: ctx.update({"꩜": "Dimensional Fold Opened (Spacetime Warped)"}),
    "⧗": lambda ctx: ctx.update({"⧗": f"Entangled Pair Linked: {ctx.get('∴', ['Unknown State 1', 'Unknown State 2'])[0]} ↔ {ctx.get('∴', ['Unknown State 1', 'Unknown State 2'])[1]}" if len(ctx.get('∴', ['Unknown State 1', 'Unknown State 2'])) >= 2 else "Entangled Pair Not Formed (Insufficient States)"}),
    "⇌": lambda ctx: ctx.update({"⇌": "Oscillation Active (Energy Fluctuating)"}),
    "⬠": lambda ctx: ctx.update({"⬠": f"Network Transmission: {ctx.get('⧗', 'No Entanglement')}"}),
    "⇧": lambda ctx: ctx.update({"⇧": "Expanding (Universe Growing)"}),
    "Ω": lambda ctx: ctx.update({"Ω": f"Reality Formed: {ctx.get('✧', 'No Collapse Observed')}"}),
    "⇀": lambda ctx: ctx.update({"⇀": "Subtle Motion (Neutrino-Like Movement)"}),
    "ϕ": lambda ctx: ctx.update({"ϕ": "Spiral Growth (Galactic Formation)"}),
    "∞": lambda ctx: ctx.update({"∞": "Infinite Potential (Unbounded Energy)"}),
}

# Phenomena symbolic dictionary
phenomena = {
    "Quantum Superposition": ("∴ + ◐ = Ψ", "Multiple possibilities coexist in a partial state until forming a quantum state."),
    "Wave Function Collapse": ("Ψ × ✧ = Ω", "A quantum state collapses through observation, generating reality."),
    "Quantum Entanglement": ("(∴ ∞ ∴) = ⧗", "Possibilities united infinitely form a mirrored system."),
    "Quantum Tunneling": ("Ψ + ∅ → ꩜", "Potential crosses the void, creating a dimensional transition."),
    "Wormhole": ("☍ + ✦⇌✦ = ꩜", "Reflected oppositions connect through a fold in spacetime."),
    "Singularity (Black Hole)": ("● × ∅ = ꩜", "Totality collapses into nothingness, generating a dimensional fold."),
    "Hawking Radiation": ("꩜ ⇌ (✧ + ∅)", "The fold oscillates between collapse and void, releasing energy."),
    "Cosmic Inflation": ("∅ + ϕ = ⇧ × ∞", "From the void, growth drives expansion into infinity."),
    "Black Hole Collision": ("(꩜ + ꩜) → ⬠ ⇌ ⇧", "Two folds merge, vibrating in a network and expanding."),
    "Holographic Principle": ("● ⇌ ⬠ = Ω", "Totality is reflected in a network, forming reality."),
    "Casimir Effect": ("∅ × (◐ + ◐) = ⇂", "The void between nearby dualities generates compression."),
    "Galaxy Formation": ("ϕ × ⬠ = ✧ × ⇧", "Growth in a network collapses locally and expands globally."),
    "Neutrinos": ("∴ ⇌ ∞ = ⇀", "Possibilities oscillate infinitely, moving subtly."),
    "Big Bang": ("∅ → ● × ꩜", "From nothing, a totality folds into itself."),
    "Unification of Forces": ("(▲ + ⬠ + ⇧ + ✧) = ●", "Force, network, expansion, and collapse converge into unity."),
    "Exotic Matter": ("∅ ⇌ ⇂ = ꩜", "The void under inverted compression folds space."),
    "Quantum Decoherence": ("Ψ × ⬠ = Ω + ∅", "A quantum state interacts with a network, collapsing and dissipating."),
    "Strings (String Theory)": ("∞ ⇌ ⇧ = ⧗ × ϕ", "Infinite vibrations in expansion form spiraling systems."),
    "Event Horizon": ("● ⇌ ꩜ = ◐", "Totality splits at a fold, hiding half."),
    "Inflaton Field Fluctuations": ("∅ × ϕ ⇌ ⇧ = ∴", "The void in a spiral oscillates with expansion, generating possibilities."),
    "Information Paradox": ("(● + ✧) ⇌ ꩜ = ⬠", "Totality and collapse enter a fold, emerging as a network."),
    "Unruh Effect": ("⇀ × ∅ = ✧", "Motion in the void manifests perceived collapses."),
    "Universe Topology": ("● ⇌ ꩜ × ϕ = ∞", "Totality folds and grows in a spiral, extending infinitely."),
}

# Symbolic signal definitions
signals = {
    "FRB 121102": ["∴", "∞ ⇌ ⇧ = ⧗ × ϕ"],
    "Wow!": ["● ⇌ ✧"],
    "BLC1": ["◐ ⇌ ⬠"],
    "GRB": ["✧ × ꩜"]
}

# Symbolic parser with context and conditionals
def interpret(expression, context):
    if expression.startswith("if"):
        condition = expression[3:].strip(":")
        left, op, right = condition.split()
        left_val = context.get(left, None)
        right_val = context.get(right, None)
        condition_met = (left_val == right_val if op == "==" else left_val != right_val)
        return f"Condition {left} {op} {right} => {condition_met}"

    if "→" in expression:
        origin, target = expression.split("→")
        origin = origin.strip()
        target = target.strip()
        context[target] = context.get(origin, None)
        return f"Transition: {origin} → {target} => {context.get(target)}"

    tokens = expression.replace("=", " = ").split()
    output = []
    for token in tokens:
        if token in symbols:
            symbols[token](context)
            output.append(f"{token}: {context.get(token)}")
        elif token == "=":
            output.append("=")
        else:
            output.append(token)
    return " ".join(output)

# GUI Application
class AlienSymbolicInterpreterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("👽 Alien Symbolic Interpreter (Prototype v12)")
        self.context = {}  # Initialize context for symbolic operations
        self.current_expression = []  # Store the current expression being built
        self.expression_history = []  # Store history of interpreted expressions
        self.favorites = {"phenomena": [], "signals": []}  # Store favorite phenomena and signals
        self.load_favorites()  # Load favorites from file
        self.dark_mode = True  # Fixar dark mode como único

        # Set window size
        self.root.geometry("1000x500")

        # Configure styles for dark mode
        self.style = ttk.Style()

        # Main frame with horizontal layout
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Left Column: Output Area with Tabs
        self.output_frame = ttk.Frame(self.main_frame)
        self.output_frame.grid(row=0, column=0, padx=10, pady=5, sticky=(tk.N, tk.S))
        
        # Tabs for output
        self.output_notebook = ttk.Notebook(self.output_frame)
        self.output_notebook.grid(row=1, column=0, columnspan=2, pady=5)

        # Expressions Tab
        self.expressions_tab = ttk.Frame(self.output_notebook)
        self.output_notebook.add(self.expressions_tab, text="Expressions")
        self.expressions_output = scrolledtext.ScrolledText(self.expressions_tab, width=40, height=20, wrap=tk.WORD)
        self.expressions_output.grid(row=0, column=0, pady=5)
        self.expressions_output.tag_configure("equation", foreground="lightblue")
        self.expressions_output.tag_configure("error", foreground="red")
        self.expressions_output.tag_configure("separator", foreground="gray")
        self.expressions_output.insert(tk.END, "Expression results will appear here.\n\n")

        # Signals Tab
        self.signals_tab = ttk.Frame(self.output_notebook)
        self.output_notebook.add(self.signals_tab, text="Signals")
        self.signals_output = scrolledtext.ScrolledText(self.signals_tab, width=40, height=20, wrap=tk.WORD)
        self.signals_output.grid(row=0, column=0, pady=5)
        self.signals_output.tag_configure("equation", foreground="lightblue")
        self.signals_output.tag_configure("error", foreground="red")
        self.signals_output.tag_configure("separator", foreground="gray")
        self.signals_output.insert(tk.END, "Signal simulation results will appear here.\n\n")

        # Phenomena Tab
        self.phenomena_tab = ttk.Frame(self.output_notebook)
        self.output_notebook.add(self.phenomena_tab, text="Phenomena")
        self.phenomena_output = scrolledtext.ScrolledText(self.phenomena_tab, width=40, height=20, wrap=tk.WORD)
        self.phenomena_output.grid(row=0, column=0, pady=5)
        self.phenomena_output.tag_configure("equation", foreground="lightblue")
        self.phenomena_output.tag_configure("error", foreground="red")
        self.phenomena_output.tag_configure("separator", foreground="gray")
        self.phenomena_output.tag_configure("phenomenon", font=("Arial", 10, "bold"))
        self.phenomena_output.insert(tk.END, "Phenomena explanations will appear here.\n\n")

        # Favorites Tab
        self.favorites_tab = ttk.Frame(self.output_notebook)
        self.output_notebook.add(self.favorites_tab, text="Favorites")
        self.favorites_output = scrolledtext.ScrolledText(self.favorites_tab, width=40, height=20, wrap=tk.WORD)
        self.favorites_output.grid(row=0, column=0, pady=5)
        self.favorites_output.tag_configure("info", foreground="yellow")
        self.favorites_output.tag_configure("separator", foreground="gray")
        self.favorites_output.insert(tk.END, "Your favorite phenomena and signals will appear here.\n")
        self.favorites_output.insert(tk.END, "Double-click items in 'List Phenomena' or 'List Signals' to add/remove favorites.\n")
        self.favorites_output.insert(tk.END, "Select a favorite from the dropdown and click 'Run Favorite' to execute.\n\n")
        self.update_favorites_output()  # Populate the favorites list initially

        # Output controls
        self.clear_output_button = ttk.Button(self.output_frame, text="Clear Output", command=self.clear_output, style="Custom.TButton")
        self.clear_output_button.grid(row=0, column=0, pady=5, sticky=tk.W)
        self.export_output_button = ttk.Button(self.output_frame, text="Export Output", command=self.export_output, style="Custom.TButton")
        self.export_output_button.grid(row=0, column=1, pady=5, sticky=tk.E)

        # Center Column: Build Expression
        self.build_frame = ttk.Frame(self.main_frame)
        self.build_frame.grid(row=0, column=1, padx=10, pady=5, sticky=(tk.N))
        self.build_label = ttk.Label(self.build_frame, text="Build Your Expression:")
        self.build_label.grid(row=0, column=0, pady=5)

        # Current expression display
        self.expression_display = ttk.Label(self.build_frame, text="Current Expression: (empty)", font=("Arial", 12))
        self.expression_display.grid(row=1, column=0, pady=5)

        # Clickable symbols grid
        self.symbols_frame = ttk.Frame(self.build_frame)
        self.symbols_frame.grid(row=2, column=0, pady=5)
        self.symbol_buttons = {}
        row, col = 0, 0
        for symbol in symbols.keys():
            btn = ttk.Button(self.symbols_frame, text=symbol, width=5, command=lambda s=symbol: self.add_symbol(s), style="Custom.TButton")
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.symbol_buttons[symbol] = btn
            col += 1
            if col > 4:  # 5 symbols per row
                col = 0
                row += 1

        # Additional operators (including parentheses)
        self.operator_frame = ttk.Frame(self.build_frame)
        self.operator_frame.grid(row=3, column=0, pady=5)
        ttk.Button(self.operator_frame, text="+", width=5, command=lambda: self.add_symbol("+"), style="Custom.TButton").grid(row=0, column=0, padx=2)
        ttk.Button(self.operator_frame, text="×", width=5, command=lambda: self.add_symbol("×"), style="Custom.TButton").grid(row=0, column=1, padx=2)
        ttk.Button(self.operator_frame, text="=", width=5, command=lambda: self.add_symbol("="), style="Custom.TButton").grid(row=0, column=2, padx=2)
        ttk.Button(self.operator_frame, text="→", width=5, command=lambda: self.add_symbol("→"), style="Custom.TButton").grid(row=0, column=3, padx=2)
        ttk.Button(self.operator_frame, text="(", width=5, command=lambda: self.add_symbol("("), style="Custom.TButton").grid(row=0, column=4, padx=2)
        ttk.Button(self.operator_frame, text=")", width=5, command=lambda: self.add_symbol(")"), style="Custom.TButton").grid(row=0, column=5, padx=2)
        ttk.Button(self.operator_frame, text="Clear", width=10, command=self.clear_expression, style="Custom.TButton").grid(row=0, column=6, padx=2)

        # Interpret built expression
        self.interpret_build_button = ttk.Button(self.build_frame, text="Interpret Built Expression", command=self.interpret_built_expression, style="Custom.TButton")
        self.interpret_build_button.grid(row=4, column=0, pady=5)

        # Simulate a Signal (movido para o build_frame)
        self.signal_label = ttk.Label(self.build_frame, text="Simulate a Signal:")
        self.signal_label.grid(row=5, column=0, pady=5)
        self.signal_var = tk.StringVar()
        self.signal_dropdown = ttk.Combobox(self.build_frame, textvariable=self.signal_var, values=list(signals.keys()), width=27, state="readonly")
        self.signal_dropdown.grid(row=6, column=0, pady=5)
        self.run_signal_button = ttk.Button(self.build_frame, text="Run Signal", command=self.run_signal, style="Custom.TButton")
        self.run_signal_button.grid(row=7, column=0, pady=5)

        # Explain a Phenomenon (movido para o build_frame)
        self.phenomenon_label = ttk.Label(self.build_frame, text="Explain a Phenomenon:")
        self.phenomenon_label.grid(row=8, column=0, pady=5)
        self.phenomenon_var = tk.StringVar()
        self.phenomenon_dropdown = ttk.Combobox(self.build_frame, textvariable=self.phenomenon_var, values=list(phenomena.keys()), width=27, state="readonly")
        self.phenomenon_dropdown.grid(row=9, column=0, pady=5)
        self.explain_phenomenon_button = ttk.Button(self.build_frame, text="Explain Phenomenon", command=self.explain_phenomenon, style="Custom.TButton")
        self.explain_phenomenon_button.grid(row=10, column=0, pady=5)

        # Right Column: Controls
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.grid(row=0, column=2, padx=10, pady=5, sticky=(tk.N))

        # List buttons
        self.symbols_button = ttk.Button(self.controls_frame, text="List Symbols", command=self.list_symbols, style="Custom.TButton")
        self.symbols_button.grid(row=0, column=0, pady=5, sticky=(tk.W, tk.E))
        self.phenomena_button = ttk.Button(self.controls_frame, text="List Phenomena", command=self.list_phenomena, style="Custom.TButton")
        self.phenomena_button.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))
        self.signals_button = ttk.Button(self.controls_frame, text="List Signals", command=self.list_signals, style="Custom.TButton")
        self.signals_button.grid(row=2, column=0, pady=5, sticky=(tk.W, tk.E))

        # View Mandala
        self.mandala_button = ttk.Button(self.controls_frame, text="View Mandala", command=self.view_mandala, style="Custom.TButton")
        self.mandala_button.grid(row=3, column=0, pady=5, sticky=(tk.W, tk.E))

        # Tutorial
        self.tutorial_button = ttk.Button(self.controls_frame, text="Tutorial", command=self.show_tutorial, style="Custom.TButton")
        self.tutorial_button.grid(row=4, column=0, pady=5, sticky=(tk.W, tk.E))

        # Manual Expression Input
        self.expression_label = ttk.Label(self.controls_frame, text="Enter Expression Manually:")
        self.expression_label.grid(row=5, column=0, pady=5)
        self.expression_entry = ttk.Entry(self.controls_frame, width=30)
        self.expression_entry.grid(row=6, column=0, pady=5)
        self.interpret_button = ttk.Button(self.controls_frame, text="Interpret Manual", command=self.interpret_expression, style="Custom.TButton")
        self.interpret_button.grid(row=7, column=0, pady=5, sticky=(tk.W, tk.E))

        # Expression History
        self.history_label = ttk.Label(self.controls_frame, text="Expression History:")
        self.history_label.grid(row=8, column=0, pady=5)
        self.history_var = tk.StringVar()
        self.history_dropdown = ttk.Combobox(self.controls_frame, textvariable=self.history_var, values=["(No history yet)"], width=27, state="readonly")
        self.history_dropdown.grid(row=9, column=0, pady=5)
        self.history_button = ttk.Button(self.controls_frame, text="Run Selected", command=self.run_history_expression, style="Custom.TButton")
        self.history_button.grid(row=10, column=0, pady=5, sticky=(tk.W, tk.E))

        # Favorites
        self.favorites_label = ttk.Label(self.controls_frame, text="Favorites:")
        self.favorites_label.grid(row=11, column=0, pady=5)
        self.favorites_var = tk.StringVar()
        self.favorites_dropdown = ttk.Combobox(self.controls_frame, textvariable=self.favorites_var, values=self.get_favorites_list(), width=27, state="readonly")
        self.favorites_dropdown.grid(row=12, column=0, pady=5)
        self.favorites_button = ttk.Button(self.controls_frame, text="Run Favorite", command=self.run_favorite, style="Custom.TButton")
        self.favorites_button.grid(row=13, column=0, pady=5, sticky=(tk.W, tk.E))

        # Apply styles *after* all widgets are created
        self.configure_styles()

    def configure_styles(self):
        # Forçar o tema "clam" para maior controle sobre os estilos
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Dark mode fixo (cosmic theme)
        self.root.configure(bg="#1a1a2e")
        self.style.configure("TFrame", background="#1a1a2e")
        self.style.configure("TLabel", background="#1a1a2e", foreground="white")
        # Ajustar o estilo dos botões
        self.style.configure("Custom.TButton", background="#16213e", foreground="white", bordercolor="#16213e", focusthickness=0, font=("Arial", 10))
        self.style.map("Custom.TButton", background=[("active", "#0f3460")], foreground=[("active", "white")])
        self.style.configure("TEntry", fieldbackground="#0f3460", foreground="white")
        self.style.configure("TCombobox", fieldbackground="#0f3460", foreground="white")
        self.style.map("TCombobox", fieldbackground=[("readonly", "#0f3460")], selectbackground=[("readonly", "#0f3460")])
        self.style.configure("TCheckbutton", background="#1a1a2e", foreground="white")
        self.expressions_output.configure(bg="#0f3460", fg="white", insertbackground="white")
        self.signals_output.configure(bg="#0f3460", fg="white", insertbackground="white")
        self.phenomena_output.configure(bg="#0f3460", fg="white", insertbackground="white")
        self.favorites_output.configure(bg="#0f3460", fg="white", insertbackground="white")

    def add_symbol(self, symbol):
        self.current_expression.append(symbol)
        self.update_expression_display()

    def clear_expression(self):
        self.current_expression = []
        self.update_expression_display()

    def update_expression_display(self):
        if not self.current_expression:
            self.expression_display.config(text="Current Expression: (empty)")
        else:
            self.expression_display.config(text=f"Current Expression: {' '.join(self.current_expression)}")

    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def check_phenomenon(self, expression):
        # Check if the expression matches any phenomenon
        for pheno, (eq, meaning) in phenomena.items():
            if expression == eq:
                self.phenomena_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
                self.phenomena_output.insert(tk.END, f"{pheno}\n", "phenomenon")
                self.phenomena_output.insert(tk.END, f"{eq}\n", "equation")
                self.phenomena_output.insert(tk.END, f"→ {meaning}\n", "result")
                self.phenomena_output.insert(tk.END, "---\n", "separator")
                self.phenomena_output.see(tk.END)
                break

    def interpret_built_expression(self):
        if not self.current_expression:
            self.expressions_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.expressions_output.insert(tk.END, "Please build an expression using the symbols above.\n", "error")
            self.expressions_output.insert(tk.END, "---\n", "separator")
            return
        expression = " ".join(self.current_expression).strip()  # Normalizar a expressão
        self.context = {}  # Resetar o contexto para cada nova interpretação
        result = interpret(expression, self.context)
        self.expressions_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
        self.expressions_output.insert(tk.END, f">>> {expression}\n", "equation")
        self.expressions_output.insert(tk.END, f"{result}\n", "result")
        self.expressions_output.insert(tk.END, "---\n", "separator")
        self.expressions_output.see(tk.END)
        self.expression_history.append(expression)
        self.history_dropdown["values"] = self.expression_history
        # Check if the expression matches a phenomenon
        self.check_phenomenon(expression)

    def interpret_expression(self):
        expression = self.expression_entry.get().strip()
        if not expression:
            self.expressions_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.expressions_output.insert(tk.END, "Please enter a symbolic expression.\n", "error")
            self.expressions_output.insert(tk.END, "---\n", "separator")
            return
        self.context = {}  # Resetar o contexto
        result = interpret(expression, self.context)
        self.expressions_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
        self.expressions_output.insert(tk.END, f">>> {expression}\n", "equation")
        self.expressions_output.insert(tk.END, f"{result}\n", "result")
        self.expressions_output.insert(tk.END, "---\n", "separator")
        self.expressions_output.see(tk.END)
        self.expression_history.append(expression)
        self.history_dropdown["values"] = self.expression_history
        # Check if the expression matches a phenomenon
        self.check_phenomenon(expression)

    def run_history_expression(self):
        expression = self.history_var.get()
        if not expression or expression == "(No history yet)":
            self.expressions_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.expressions_output.insert(tk.END, "Please select an expression from the history.\n", "error")
            self.expressions_output.insert(tk.END, "---\n", "separator")
            return
        self.context = {}  # Resetar o contexto
        result = interpret(expression, self.context)
        self.expressions_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
        self.expressions_output.insert(tk.END, f">>> {expression}\n", "equation")
        self.expressions_output.insert(tk.END, f"{result}\n", "result")
        self.expressions_output.insert(tk.END, "---\n", "separator")
        self.expressions_output.see(tk.END)
        # Check if the expression matches a phenomenon
        self.check_phenomenon(expression)

    def list_symbols(self):
        popup = tk.Toplevel(self.root)
        popup.title("Available Symbols")
        popup.geometry("500x400")
        popup.configure(bg="#1a1a2e")

        tree = ttk.Treeview(popup, columns=("Symbol", "Meaning"), show="headings")
        tree.heading("Symbol", text="Symbol")
        tree.heading("Meaning", text="Meaning")
        tree.column("Symbol", width=100, anchor="center")
        tree.column("Meaning", width=350)

        for symbol, func in symbols.items():
            self.context = {}
            func(self.context)
            tree.insert("", tk.END, values=(symbol, self.context.get(symbol)), tags=("symbol",))
        
        tree.tag_configure("symbol", foreground="#00BFFF")
        tree.pack(expand=True, fill="both", padx=10, pady=10)

    def list_phenomena(self):
        popup = tk.Toplevel(self.root)
        popup.title("Known Cosmic Phenomena")
        popup.geometry("600x400")
        popup.configure(bg="#1a1a2e")

        tree = ttk.Treeview(popup, columns=("Phenomenon", "Equation", "Meaning", "Favorite"), show="headings")
        tree.heading("Phenomenon", text="Phenomenon")
        tree.heading("Equation", text="Equation")
        tree.heading("Meaning", text="Meaning")
        tree.heading("Favorite", text="Favorite")
        tree.column("Phenomenon", width=200)
        tree.column("Equation", width=150)
        tree.column("Meaning", width=200)
        tree.column("Favorite", width=50)

        for name, (eq, meaning) in phenomena.items():
            tree.insert("", tk.END, values=(name, eq, meaning, "Add" if name not in self.favorites["phenomena"] else "Remove"), tags=("phenomenon", name))
        
        tree.tag_configure("phenomenon", foreground="darkgreen")
        tree.bind("<Double-1>", lambda event: self.toggle_favorite(event, "phenomena"))
        tree.pack(expand=True, fill="both", padx=10, pady=10)

    def list_signals(self):
        popup = tk.Toplevel(self.root)
        popup.title("Available Signals")
        popup.geometry("300x200")
        popup.configure(bg="#1a1a2e")

        tree = ttk.Treeview(popup, columns=("Signal", "Favorite"), show="headings")
        tree.heading("Signal", text="Signal")
        tree.heading("Favorite", text="Favorite")
        tree.column("Signal", width=150, anchor="center")
        tree.column("Favorite", width=50)

        for name in signals:
            tree.insert("", tk.END, values=(name, "Add" if name not in self.favorites["signals"] else "Remove"), tags=("signal", name))
        
        tree.bind("<Double-1>", lambda event: self.toggle_favorite(event, "signals"))
        tree.pack(expand=True, fill="both", padx=10, pady=10)

    def toggle_favorite(self, event, category):
        tree = event.widget
        item = tree.selection()[0]
        name = tree.item(item, "values")[0]
        if category == "phenomena":
            if name in self.favorites["phenomena"]:
                self.favorites["phenomena"].remove(name)
                tree.set(item, "Favorite", "Add")
            else:
                self.favorites["phenomena"].append(name)
                tree.set(item, "Favorite", "Remove")
        elif category == "signals":
            if name in self.favorites["signals"]:
                self.favorites["signals"].remove(name)
                tree.set(item, "Favorite", "Add")
            else:
                self.favorites["signals"].append(name)
                tree.set(item, "Favorite", "Remove")
        self.save_favorites()
        self.favorites_dropdown["values"] = self.get_favorites_list()
        self.update_favorites_output()

    def update_favorites_output(self):
        self.favorites_output.delete(1.0, tk.END)
        self.favorites_output.insert(tk.END, "Your favorite phenomena and signals will appear here.\n")
        self.favorites_output.insert(tk.END, "Double-click items in 'List Phenomena' or 'List Signals' to add/remove favorites.\n")
        self.favorites_output.insert(tk.END, "Select a favorite from the dropdown and click 'Run Favorite' to execute.\n\n")
        if self.favorites["phenomena"]:
            self.favorites_output.insert(tk.END, "Favorite Phenomena:\n", "info")
            for pheno in self.favorites["phenomena"]:
                self.favorites_output.insert(tk.END, f"- {pheno}\n")
        if self.favorites["signals"]:
            self.favorites_output.insert(tk.END, "Favorite Signals:\n", "info")
            for sig in self.favorites["signals"]:
                self.favorites_output.insert(tk.END, f"- {sig}\n")
        self.favorites_output.insert(tk.END, "---\n", "separator")

    def load_favorites(self):
        if os.path.exists("favorites.json"):
            with open("favorites.json", "r") as f:
                self.favorites = json.load(f)

    def save_favorites(self):
        with open("favorites.json", "w") as f:
            json.dump(self.favorites, f)

    def get_favorites_list(self):
        favorites_list = []
        for pheno in self.favorites["phenomena"]:
            favorites_list.append(f"Phenomenon: {pheno}")
        for sig in self.favorites["signals"]:
            favorites_list.append(f"Signal: {sig}")
        return favorites_list if favorites_list else ["(No favorites yet)"]

    def run_favorite(self):
        favorite = self.favorites_var.get()
        if not favorite or favorite == "(No favorites yet)":
            self.favorites_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.favorites_output.insert(tk.END, "Please select a favorite to run.\n", "error")
            self.favorites_output.insert(tk.END, "---\n", "separator")
            return
        if favorite.startswith("Phenomenon: "):
            pheno = favorite.replace("Phenomenon: ", "")
            if pheno in phenomena:
                eq, meaning = phenomena[pheno]
                self.phenomena_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
                self.phenomena_output.insert(tk.END, f"{pheno}\n", "phenomenon")
                self.phenomena_output.insert(tk.END, f"{eq}\n", "equation")
                self.phenomena_output.insert(tk.END, f"→ {meaning}\n", "result")
                self.phenomena_output.insert(tk.END, "---\n", "separator")
                self.phenomena_output.see(tk.END)
                self.favorites_output.insert(tk.END, f"[{self.get_timestamp()}] Result shown in Phenomena tab.\n", "info")
                self.favorites_output.insert(tk.END, "---\n", "separator")
        elif favorite.startswith("Signal: "):
            sig_name = favorite.replace("Signal: ", "")
            if sig_name in signals:
                self.context = {}  # Resetar o contexto
                for line in signals[sig_name]:
                    result = interpret(line, self.context)
                    self.signals_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
                    self.signals_output.insert(tk.END, f">>> {line}\n", "equation")
                    self.signals_output.insert(tk.END, f"{result}\n", "result")
                    self.signals_output.insert(tk.END, "---\n", "separator")
                    self.signals_output.see(tk.END)
                self.favorites_output.insert(tk.END, f"[{self.get_timestamp()}] Result shown in Signals tab.\n", "info")
                self.favorites_output.insert(tk.END, "---\n", "separator")

    def run_signal(self):
        sig_name = self.signal_var.get()
        if not sig_name:
            self.signals_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.signals_output.insert(tk.END, "Please select a signal to simulate.\n", "error")
            self.signals_output.insert(tk.END, "---\n", "separator")
            return
        if sig_name in signals:
            self.context = {}  # Resetar o contexto
            for line in signals[sig_name]:
                result = interpret(line, self.context)
                self.signals_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
                self.signals_output.insert(tk.END, f">>> {line}\n", "equation")
                self.signals_output.insert(tk.END, f"{result}\n", "result")
                self.signals_output.insert(tk.END, "---\n", "separator")
                self.signals_output.see(tk.END)
        else:
            self.signals_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.signals_output.insert(tk.END, f"Unknown signal: {sig_name}\n", "error")
            self.signals_output.insert(tk.END, "---\n", "separator")
        self.signals_output.see(tk.END)

    def explain_phenomenon(self):
        pheno = self.phenomenon_var.get()
        if not pheno:
            self.phenomena_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.phenomena_output.insert(tk.END, "Please select a phenomenon to explain.\n", "error")
            self.phenomena_output.insert(tk.END, "---\n", "separator")
            return
        if pheno in phenomena:
            eq, meaning = phenomena[pheno]
            self.phenomena_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.phenomena_output.insert(tk.END, f"{pheno}\n", "phenomenon")
            self.phenomena_output.insert(tk.END, f"{eq}\n", "equation")
            self.phenomena_output.insert(tk.END, f"→ {meaning}\n", "result")
            self.phenomena_output.insert(tk.END, "---\n", "separator")
        else:
            self.phenomena_output.insert(tk.END, f"[{self.get_timestamp()}] ", "timestamp")
            self.phenomena_output.insert(tk.END, f"Unknown phenomenon: {pheno}\n", "error")
            self.phenomena_output.insert(tk.END, "---\n", "separator")
        self.phenomena_output.see(tk.END)

    def clear_output(self):
        current_tab = self.output_notebook.index(self.output_notebook.select())
        if current_tab == 0:  # Expressions tab
            self.expressions_output.delete(1.0, tk.END)
            self.expressions_output.insert(tk.END, "Expression results will appear here.\n\n")
        elif current_tab == 1:  # Signals tab
            self.signals_output.delete(1.0, tk.END)
            self.signals_output.insert(tk.END, "Signal simulation results will appear here.\n\n")
        elif current_tab == 2:  # Phenomena tab
            self.phenomena_output.delete(1.0, tk.END)
            self.phenomena_output.insert(tk.END, "Phenomena explanations will appear here.\n\n")
        elif current_tab == 3:  # Favorites tab
            self.favorites_output.delete(1.0, tk.END)
            self.favorites_output.insert(tk.END, "Your favorite phenomena and signals will appear here.\n")
            self.favorites_output.insert(tk.END, "Double-click items in 'List Phenomena' or 'List Signals' to add/remove favorites.\n")
            self.favorites_output.insert(tk.END, "Select a favorite from the dropdown and click 'Run Favorite' to execute.\n\n")
            self.update_favorites_output()

    def export_output(self):
        current_tab = self.output_notebook.index(self.output_notebook.select())
        if current_tab == 0:  # Expressions tab
            content = self.expressions_output.get(1.0, tk.END)
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        elif current_tab == 1:  # Signals tab
            content = self.signals_output.get(1.0, tk.END)
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        elif current_tab == 2:  # Phenomena tab
            content = self.phenomena_output.get(1.0, tk.END)
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        elif current_tab == 3:  # Favorites tab
            content = self.favorites_output.get(1.0, tk.END)
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        else:
            return
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)

    def show_tutorial(self):
        popup = tk.Toplevel(self.root)
        popup.title("Tutorial")
        popup.geometry("500x400")
        popup.configure(bg="#1a1a2e")

        tutorial_text = scrolledtext.ScrolledText(popup, width=60, height=20, wrap=tk.WORD, bg="#0f3460", fg="white")
        tutorial_text.pack(padx=10, pady=10, expand=True, fill="both")

        tutorial_content = (
            "Welcome to the Alien Symbolic Interpreter!\n\n"
            "Follow these steps to explore the language of shapes:\n\n"
            "1. **Build an Expression**:\n"
            "   - Click the symbols in the center panel to build an expression (e.g., Ψ + ∴ = ◐).\n"
            "   - Use the operator buttons (+, ×, =, →, (, )) to add operators.\n"
            "   - Click 'Interpret Built Expression' to see the result in the 'Expressions' tab.\n"
            "   - If the expression matches a known phenomenon, it will also appear in the 'Phenomena' tab.\n\n"
            "2. **Enter an Expression Manually**:\n"
            "   - Type an expression in the 'Enter Expression Manually' field (e.g., Ψ = ∴ + ◐).\n"
            "   - Click 'Interpret Manual' to see the result.\n\n"
            "3. **Simulate a Signal**:\n"
            "   - Select a signal (e.g., Wow!) from the 'Simulate a Signal' dropdown.\n"
            "   - Click 'Run Signal' to see the simulation in the 'Signals' tab.\n\n"
            "4. **Explain a Phenomenon**:\n"
            "   - Select a phenomenon (e.g., Big Bang) from the 'Explain a Phenomenon' dropdown.\n"
            "   - Click 'Explain Phenomenon' to see the explanation in the 'Phenomena' tab.\n\n"
            "5. **Manage Favorites**:\n"
            "   - Double-click a phenomenon or signal in the 'List Phenomena' or 'List Signals' windows to add/remove it from favorites.\n"
            "   - View your favorites in the 'Favorites' tab.\n"
            "   - Select a favorite from the 'Favorites' dropdown and click 'Run Favorite' to execute it.\n\n"
            "6. **View the Mandala**:\n"
            "   - Click 'View Mandala' to see a visual representation of the symbols.\n\n"
            "7. **Explore History**:\n"
            "   - After interpreting expressions, they appear in the 'Expression History' dropdown.\n"
            "   - Select an expression and click 'Run Selected' to re-run it.\n\n"
            "Enjoy exploring the universe through shapes!"
        )
        tutorial_text.insert(tk.END, tutorial_content)
        tutorial_text.config(state="disabled")

    def view_mandala(self):
        popup = tk.Toplevel(self.root)
        popup.title("Symbolic Mandala")
        popup.geometry("500x500")
        popup.configure(bg="#1a1a2e")

        canvas = tk.Canvas(popup, width=500, height=500, bg="#0f3460", highlightthickness=0)
        canvas.pack(expand=True, fill="both")

        # Draw some stars in the background
        for _ in range(50):
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            canvas.create_oval(x, y, x+2, y+2, fill="white", outline="white")

        # Center of the mandala
        center_x, center_y = 250, 250
        radius = 150

        # Position symbols in a circle and store their coordinates
        symbol_list = list(symbols.keys())
        num_symbols = len(symbol_list)
        symbol_coords = {}
        for i, symbol in enumerate(symbol_list):
            angle = 2 * math.pi * i / num_symbols
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            canvas.create_text(x, y, text=symbol, font=("Arial", 16), fill="lightblue", tags=("symbol", symbol))
            symbol_coords[symbol] = (x, y)

        # Draw connections between symbols (yellow dashed lines)
        connections = [
            ("Ω", "⇧"),
            ("∴", "⧗"),
            ("Ψ", "✧"),
            ("꩜", "⬠"),
            ("⇌", "⇀"),
            ("◐", "∅"),
            ("●", "∞"),
            ("ϕ", "⇧"),
        ]
        for sym1, sym2 in connections:
            if sym1 in symbol_coords and sym2 in symbol_coords:
                x1, y1 = symbol_coords[sym1]
                x2, y2 = symbol_coords[sym2]
                canvas.create_line(x1, y1, x2, y2, fill="yellow", dash=(4, 4))

        # Position symbols in a circle
        symbol_list = list(symbols.keys())
        num_symbols = len(symbol_list)
        for i, symbol in enumerate(symbol_list):
            angle = 2 * math.pi * i / num_symbols
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            canvas.create_text(x, y, text=symbol, font=("Arial", 16), fill="lightblue", tags=("symbol", symbol))

        # Draw a small central circle
        canvas.create_oval(center_x - 10, center_y - 10, center_x + 10, center_y + 10, fill="#16213e", outline="white")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = AlienSymbolicInterpreterGUI(root)
    root.mainloop()
