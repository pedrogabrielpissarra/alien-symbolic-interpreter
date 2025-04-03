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
def evaluate_subexpression(subexpr, context):
    subexpr = subexpr.strip("()")
    tokens = subexpr.replace("=", " = ").split()
    output = []
    for token in tokens:
        if token in symbols:
            symbols[token](context)
            output.append(context.get(token))
        else:
            output.append(token)
    return " ".join(map(str, output))

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

        while "(" in origin and ")" in origin:
            start = origin.rindex("(")
            end = origin.find(")", start)
            if end == -1:
                return f"Error: Unmatched parentheses in {origin}"
            subexpr = origin[start:end+1]
            subresult = evaluate_subexpression(subexpr, context)
            origin = origin[:start] + subresult + origin[end+1:]

        tokens = origin.replace("=", " = ").split()
        output = []
        for token in tokens:
            if token in symbols:
                symbols[token](context)
                output.append(context.get(token))
            else:
                output.append(token)
        result = " ".join(map(str, output))
        context[target] = result
        return f"Transition: {origin} → {target} => {context.get(target)}"

    while "(" in expression and ")" in expression:
        start = expression.rindex("(")
        end = expression.find(")", start)
        if end == -1:
            return f"Error: Unmatched parentheses in {expression}"
        subexpr = expression[start:end+1]
        subresult = evaluate_subexpression(subexpr, context)
        expression = expression[:start] + subresult + expression[end+1:]

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
        self.context = {}
        self.current_expression = []
        self.expression_history = []
        self.favorites = {"phenomena": [], "signals": []}
        self.load_favorites()
        self.dark_mode = True  # Dark mode fixo

        self.root.geometry("1000x500")
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
        self.update_favorites_output()

        # Tutorial Tab
        self.tutorial_tab = ttk.Frame(self.output_notebook)
        self.output_notebook.add(self.tutorial_tab, text="Tutorial")
        self.tutorial_output = scrolledtext.ScrolledText(self.tutorial_tab, width=40, height=20, wrap=tk.WORD)
        self.tutorial_output.grid(row=0, column=0, pady=5)
        self.tutorial_output.tag_configure("title", font=("Arial", 12, "bold"), foreground="lightblue")
        self.tutorial_output.tag_configure("section", font=("Arial", 10, "bold"), foreground="white")
        self.tutorial_output.tag_configure("text", foreground="white")
        self.tutorial_output.insert(tk.END, "Alien Symbolic Interpreter Tutorial\n\n", "title")
        self.tutorial_output.insert(tk.END, "Welcome to the Alien Symbolic Interpreter!\n\n", "text")
        self.tutorial_output.insert(tk.END, "Follow these steps to explore the language of shapes:\n\n", "section")
        self.tutorial_output.insert(tk.END, "1. Build an Expression:\n", "section")
        self.tutorial_output.insert(tk.END, "   - Click the symbols in the center panel to build an expression (e.g., Ψ + ∴ = ◐).\n", "text")
        self.tutorial_output.insert(tk.END, "   - Use the operator buttons (+, ×, =, →, (, )) to add operators.\n", "text")
        self.tutorial_output.insert(tk.END, "   - Click 'Interpret Built Expression' to see the result in the 'Expressions' tab.\n", "text")
        self.tutorial_output.insert(tk.END, "   - If the expression matches a known phenomenon, it will also appear in the 'Phenomena' tab.\n\n", "text")
        self.tutorial_output.insert(tk.END, "2. Enter an Expression Manually:\n", "section")
        self.tutorial_output.insert(tk.END, "   - Type an expression in the 'Enter Expression Manually' field (e.g., Ψ = ∴ + ◐).\n", "text")
        self.tutorial_output.insert(tk.END, "   - Click 'Interpret Manual' to see the result.\n\n", "text")
        self.tutorial_output.insert(tk.END, "3. Simulate a Signal:\n", "section")
        self.tutorial_output.insert(tk.END, "   - Select a signal (e.g., Wow!) from the 'Simulate a Signal' dropdown.\n", "text")
        self.tutorial_output.insert(tk.END, "   - Click 'Run Signal' to see the simulation in the 'Signals' tab.\n\n", "text")
        self.tutorial_output.insert(tk.END, "4. Explain a Phenomenon:\n", "section")
        self.tutorial_output.insert(tk.END, "   - Select a phenomenon (e.g., Big Bang) from the 'Explain a Phenomenon' dropdown.\n", "text")
        self.tutorial_output.insert(tk.END, "   - Click 'Explain Phenomenon' to see the explanation in the 'Phenomena' tab.\n\n", "text")
        self.tutorial_output.insert(tk.END, "5. Manage Favorites:\n", "section")
        self.tutorial_output.insert(tk.END, "   - Double-click a phenomenon or signal in the 'List Phenomena' or 'List Signals' windows to add/remove it from favorites.\n", "text")
        self.tutorial_output.insert(tk.END, "   - View your favorites in the 'Favorites' tab.\n", "text")
        self.tutorial_output.insert(tk.END, "   - Select a favorite from the 'Favorites' dropdown and click 'Run Favorite' to execute it.\n\n", "text")
        self.tutorial_output.insert(tk.END, "6. View the Mandala:\n", "section")
        self.tutorial_output.insert(tk.END, "   - Click 'View Mandala' to see a visual representation of the symbols.\n\n", "text")
        self.tutorial_output.insert(tk.END, "7. Explore History:\n", "section")
        self.tutorial_output.insert(tk.END, "   - After interpreting expressions, they appear in the 'Expression History' dropdown.\n", "text")
        self.tutorial_output.insert(tk.END, "   - Select an expression and click 'Run Selected' to re-run it.\n\n", "text")
        self.tutorial_output.insert(tk.END, "Enjoy exploring the universe through shapes!\n", "text")
        self.tutorial_output.config(state="disabled")

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
            if col > 4:
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

        # Simulate a Signal
        self.signal_label = ttk.Label(self.build_frame, text="Simulate a Signal:")
        self.signal_label.grid(row=5, column=0, pady=5)
        self.signal_var = tk.StringVar()
        self.signal_dropdown = ttk.Combobox(self.build_frame, textvariable=self.signal_var, values=list(signals.keys()), width=27, state="readonly")
        self.signal_dropdown.grid(row=6, column=0, pady=5)
        self.run_signal_button = ttk.Button(self.build_frame, text="Run Signal", command=self.run_signal, style="Custom.TButton")
        self.run_signal_button.grid(row=7, column=0, pady=5)

        # Explain a Phenomenon
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

        # Apply styles
        self.configure_styles()

    def configure_styles(self):
        self.root.configure(bg="#1a1a2e")
        self.style.configure("TFrame", background="#1a1a2e")
        self.style.configure("TLabel", background="#1a1a2e", foreground="white")
        self.style.configure("Custom.TButton", background="#16213e", foreground="white", bordercolor="#16213e", focusthickness=0)
        self.style.map("Custom.TButton", background=[("active", "#0f3460")], foreground=[("active", "white")])
        self.style.configure("TEntry", fieldbackground="#0f3460", foreground="white")
        self.style.configure("TCombobox", fieldbackground="#0f3460", foreground="white")
        self.style.map("TCombobox", fieldbackground=[("readonly", "#0f3460")], selectbackground=[("readonly", "#0f3460")])
        self.style.configure("TCheckbutton", background="#1a1a2e", foreground="white")
        self.expressions_output.configure(bg="#0f3460", fg="white", insertbackground="white")
        self.signals_output.configure(bg="#0f3460", fg="white", insertbackground="white")
        self.phenomena_output.configure(bg="#0f3460", fg="white", insertbackground="white")
        self.favorites_output.configure(bg="#0f3460", fg="white", insertbackground="white")
        self.tutorial_output.configure(bg="#0f3460", fg="white", insertbackground="white")

    def add_symbol(self, symbol):
        self.current_expression.append(symbol)
        self.expression_display.config(text=f"Current Expression: {' '.join(self.current_expression)}")

    def clear_expression(self):
        self.current_expression = []
        self.expression_display.config(text="Current Expression: (empty)")

    def interpret_built_expression(self):
        if not self.current_expression:
            self.expressions_output.insert(tk.END, "[Error] No expression to interpret.\n", "error")
            return
        expression = " ".join(self.current_expression).strip()
        self.context = {}
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = interpret(expression, self.context)
        self.expressions_output.insert(tk.END, f"[{timestamp}] >>> {expression}\n{result}\n", "equation")
        self.expressions_output.insert(tk.END, "-" * 50 + "\n", "separator")
        self.expression_history.append(expression)
        self.history_dropdown.config(values=self.expression_history)
        self.check_phenomena(expression.strip())

    def interpret_expression(self):
        expression = self.expression_entry.get().strip()
        if not expression:
            self.expressions_output.insert(tk.END, "[Error] Please enter an expression.\n", "error")
            return
        self.context = {}
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = interpret(expression, self.context)
        self.expressions_output.insert(tk.END, f"[{timestamp}] >>> {expression}\n{result}\n", "equation")
        self.expressions_output.insert(tk.END, "-" * 50 + "\n", "separator")
        self.expression_history.append(expression)
        self.history_dropdown.config(values=self.expression_history)
        self.check_phenomena(expression)

    def run_history_expression(self):
        selected_expression = self.history_var.get()
        if not selected_expression or selected_expression == "(No history yet)":
            self.expressions_output.insert(tk.END, "[Error] No expression selected from history.\n", "error")
            return
        self.context = {}
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = interpret(selected_expression, self.context)
        self.expressions_output.insert(tk.END, f"[{timestamp}] >>> {selected_expression}\n{result}\n", "equation")
        self.expressions_output.insert(tk.END, "-" * 50 + "\n", "separator")
        self.check_phenomena(selected_expression)

    def check_phenomena(self, expression):
        for phenomenon, (symbolic_expression, explanation) in phenomena.items():
            if expression == symbolic_expression:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.phenomena_output.insert(tk.END, f"[{timestamp}] Phenomenon Detected: {phenomenon}\n", "phenomenon")
                self.phenomena_output.insert(tk.END, f"Expression: {expression}\nExplanation: {explanation}\n", "equation")
                self.phenomena_output.insert(tk.END, "-" * 50 + "\n", "separator")

    def run_signal(self):
        signal_name = self.signal_var.get()
        if not signal_name:
            self.signals_output.insert(tk.END, "[Error] Please select a signal to simulate.\n", "error")
            return
        signal_expressions = signals.get(signal_name, [])
        self.context = {}
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.signals_output.insert(tk.END, f"[{timestamp}] Simulating Signal: {signal_name}\n", "equation")
        for expr in signal_expressions:
            result = interpret(expr, self.context)
            self.signals_output.insert(tk.END, f"Expression: {expr}\n{result}\n", "equation")
        self.signals_output.insert(tk.END, "-" * 50 + "\n", "separator")

    def explain_phenomenon(self):
        phenomenon_name = self.phenomenon_var.get()
        if not phenomenon_name:
            self.phenomena_output.insert(tk.END, "[Error] Please select a phenomenon to explain.\n", "error")
            return
        symbolic_expression, explanation = phenomena.get(phenomenon_name, ("Unknown", "No explanation available."))
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.phenomena_output.insert(tk.END, f"[{timestamp}] Phenomenon: {phenomenon_name}\n", "phenomenon")
        self.phenomena_output.insert(tk.END, f"Symbolic Expression: {symbolic_expression}\nExplanation: {explanation}\n", "equation")
        self.phenomena_output.insert(tk.END, "-" * 50 + "\n", "separator")

    def list_symbols(self):
        popup = tk.Toplevel(self.root)
        popup.title("List of Symbols")
        popup.geometry("400x400")
        popup.configure(bg="#1a1a2e")
        text = scrolledtext.ScrolledText(popup, width=50, height=20, wrap=tk.WORD, bg="#0f3460", fg="white")
        text.pack(pady=10)
        for symbol in symbols.keys():
            self.context = {}
            symbols[symbol](self.context)
            text.insert(tk.END, f"{symbol}: {self.context.get(symbol, 'No description')}\n")
        text.config(state="disabled")
        ttk.Button(popup, text="Close", command=popup.destroy, style="Custom.TButton").pack(pady=5)

    def list_phenomena(self):
        popup = tk.Toplevel(self.root)
        popup.title("List of Phenomena")
        popup.geometry("600x400")
        popup.configure(bg="#1a1a2e")
        text = scrolledtext.ScrolledText(popup, width=70, height=20, wrap=tk.WORD, bg="#0f3460", fg="white")
        text.pack(pady=10)
        for phenomenon, (symbolic_expression, explanation) in phenomena.items():
            favorite_marker = "★" if phenomenon in self.favorites["phenomena"] else "☆"
            text.insert(tk.END, f"{favorite_marker} {phenomenon}: {symbolic_expression}\nExplanation: {explanation}\n\n")
        text.config(state="normal")
        text.tag_configure("phenomenon", font=("Arial", 10, "bold"))
        text.bind("<Double-1>", lambda event: self.toggle_favorite_phenomenon(text, event))
        ttk.Button(popup, text="Close", command=popup.destroy, style="Custom.TButton").pack(pady=5)

    def list_signals(self):
        popup = tk.Toplevel(self.root)
        popup.title("List of Signals")
        popup.geometry("400x400")
        popup.configure(bg="#1a1a2e")
        text = scrolledtext.ScrolledText(popup, width=50, height=20, wrap=tk.WORD, bg="#0f3460", fg="white")
        text.pack(pady=10)
        for signal, expressions in signals.items():
            favorite_marker = "★" if signal in self.favorites["signals"] else "☆"
            text.insert(tk.END, f"{favorite_marker} {signal}: {', '.join(expressions)}\n")
        text.config(state="normal")
        text.bind("<Double-1>", lambda event: self.toggle_favorite_signal(text, event))
        ttk.Button(popup, text="Close", command=popup.destroy, style="Custom.TButton").pack(pady=5)

    def toggle_favorite_phenomenon(self, text_widget, event):
        index = text_widget.index(f"{event.x},{event.y} linestart")
        line = text_widget.get(index, f"{index} lineend")
        phenomenon_name = line.split(":")[0].strip()[2:]
        if phenomenon_name in phenomena:
            if phenomenon_name in self.favorites["phenomena"]:
                self.favorites["phenomena"].remove(phenomenon_name)
            else:
                self.favorites["phenomena"].append(phenomenon_name)
            self.save_favorites()
            self.update_favorites_output()
            self.favorites_dropdown.config(values=self.get_favorites_list())
            text_widget.delete("1.0", tk.END)
            for phenomenon, (symbolic_expression, explanation) in phenomena.items():
                favorite_marker = "★" if phenomenon in self.favorites["phenomena"] else "☆"
                text_widget.insert(tk.END, f"{favorite_marker} {phenomenon}: {symbolic_expression}\nExplanation: {explanation}\n\n")

    def toggle_favorite_signal(self, text_widget, event):
        index = text_widget.index(f"{event.x},{event.y} linestart")
        line = text_widget.get(index, f"{index} lineend")
        signal_name = line.split(":")[0].strip()[2:]
        if signal_name in signals:
            if signal_name in self.favorites["signals"]:
                self.favorites["signals"].remove(signal_name)
            else:
                self.favorites["signals"].append(signal_name)
            self.save_favorites()
            self.update_favorites_output()
            self.favorites_dropdown.config(values=self.get_favorites_list())
            text_widget.delete("1.0", tk.END)
            for signal, expressions in signals.items():
                favorite_marker = "★" if signal in self.favorites["signals"] else "☆"
                text_widget.insert(tk.END, f"{favorite_marker} {signal}: {', '.join(expressions)}\n")

    def save_favorites(self):
        with open("favorites.json", "w") as f:
            json.dump(self.favorites, f)

    def load_favorites(self):
        try:
            with open("favorites.json", "r") as f:
                self.favorites = json.load(f)
        except FileNotFoundError:
            self.favorites = {"phenomena": [], "signals": []}

    def get_favorites_list(self):
        favorites_list = []
        for phenomenon in self.favorites["phenomena"]:
            favorites_list.append(f"Phenomenon: {phenomenon}")
        for signal in self.favorites["signals"]:
            favorites_list.append(f"Signal: {signal}")
        return favorites_list if favorites_list else ["(No favorites yet)"]

    def update_favorites_output(self):
        self.favorites_output.delete("1.0", tk.END)
        self.favorites_output.insert(tk.END, "Your favorite phenomena and signals will appear here.\n")
        self.favorites_output.insert(tk.END, "Double-click items in 'List Phenomena' or 'List Signals' to add/remove favorites.\n")
        self.favorites_output.insert(tk.END, "Select a favorite from the dropdown and click 'Run Favorite' to execute.\n\n")
        if self.favorites["phenomena"]:
            self.favorites_output.insert(tk.END, "Favorite Phenomena:\n", "info")
            for phenomenon in self.favorites["phenomena"]:
                symbolic_expression, explanation = phenomena.get(phenomenon, ("Unknown", "No explanation available."))
                self.favorites_output.insert(tk.END, f"- {phenomenon}: {symbolic_expression}\n")
            self.favorites_output.insert(tk.END, "\n")
        if self.favorites["signals"]:
            self.favorites_output.insert(tk.END, "Favorite Signals:\n", "info")
            for signal in self.favorites["signals"]:
                expressions = signals.get(signal, [])
                self.favorites_output.insert(tk.END, f"- {signal}: {', '.join(expressions)}\n")
        self.favorites_output.insert(tk.END, "-" * 50 + "\n", "separator")

    def run_favorite(self):
        selected_favorite = self.favorites_var.get()
        if not selected_favorite or selected_favorite == "(No favorites yet)":
            self.favorites_output.insert(tk.END, "[Error] No favorite selected.\n", "error")
            return
        if selected_favorite.startswith("Phenomenon: "):
            phenomenon_name = selected_favorite[len("Phenomenon: "):]
            self.phenomenon_var.set(phenomenon_name)
            self.explain_phenomenon()
        elif selected_favorite.startswith("Signal: "):
            signal_name = selected_favorite[len("Signal: "):]
            self.signal_var.set(signal_name)
            self.run_signal()

    def clear_output(self):
        self.expressions_output.delete("1.0", tk.END)
        self.signals_output.delete("1.0", tk.END)
        self.phenomena_output.delete("1.0", tk.END)
        self.favorites_output.delete("1.0", tk.END)
        self.expressions_output.insert(tk.END, "Expression results will appear here.\n\n")
        self.signals_output.insert(tk.END, "Signal simulation results will appear here.\n\n")
        self.phenomena_output.insert(tk.END, "Phenomena explanations will appear here.\n\n")
        self.update_favorites_output()

    def export_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file_path:
            return
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("=== Expressions ===\n")
            f.write(self.expressions_output.get("1.0", tk.END))
            f.write("\n=== Signals ===\n")
            f.write(self.signals_output.get("1.0", tk.END))
            f.write("\n=== Phenomena ===\n")
            f.write(self.phenomena_output.get("1.0", tk.END))
            f.write("\n=== Favorites ===\n")
            f.write(self.favorites_output.get("1.0", tk.END))
        self.favorites_output.insert(tk.END, f"[Info] Output exported to {file_path}\n", "info")

    def view_mandala(self):
        popup = tk.Toplevel(self.root)
        popup.title("Symbolic Mandala")
        popup.geometry("400x400")
        popup.configure(bg="#1a1a2e")
        canvas = tk.Canvas(popup, width=300, height=300, bg="#0f3460", highlightthickness=0)
        canvas.pack(pady=20)
        num_symbols = len(symbols)
        radius = 120
        center_x, center_y = 150, 150
        for i, symbol in enumerate(symbols.keys()):
            angle = (2 * math.pi * i) / num_symbols - (math.pi / 2)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            canvas.create_text(x, y, text=symbol, font=("Arial", 14), fill="white")
        canvas.create_oval(center_x - 10, center_y - 10, center_x + 10, center_y + 10, fill="#16213e", outline="white")
        ttk.Button(popup, text="Close", command=popup.destroy, style="Custom.TButton").pack(pady=5)

    def show_tutorial(self):
        self.output_notebook.select(self.tutorial_tab)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AlienSymbolicInterpreterGUI(root)
    root.mainloop()
