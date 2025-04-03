# Alien Symbolic Interpreter (Prototype v10 - GUI Version with Clickable Symbols)
# Each symbol maps to a concept or function with simulated behavior

import random
import tkinter as tk
from tkinter import ttk, scrolledtext

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
        self.root.title("👽 Alien Symbolic Interpreter (Prototype v10)")
        self.context = {}  # Initialize context for symbolic operations
        self.current_expression = []  # Store the current expression being built

        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Welcome message
        self.welcome_label = ttk.Label(self.main_frame, text="Welcome to the Alien Symbolic Interpreter!\nExplore the universe through a language of shapes.", justify="center")
        self.welcome_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Output area (scrolled text)
        self.output_area = scrolledtext.ScrolledText(self.main_frame, width=60, height=15, wrap=tk.WORD)
        self.output_area.grid(row=1, column=0, columnspan=3, pady=10)
        self.output_area.insert(tk.END, "Click the buttons below to explore symbols, phenomena, and signals.\nOr build your own expression using the clickable symbols!\n\n")

        # Symbols, Phenomena, Signals buttons
        self.symbols_button = ttk.Button(self.main_frame, text="List Symbols", command=self.list_symbols)
        self.symbols_button.grid(row=2, column=0, padx=5, pady=5)

        self.phenomena_button = ttk.Button(self.main_frame, text="List Phenomena", command=self.list_phenomena)
        self.phenomena_button.grid(row=2, column=1, padx=5, pady=5)

        self.signals_button = ttk.Button(self.main_frame, text="List Signals", command=self.list_signals)
        self.signals_button.grid(row=2, column=2, padx=5, pady=5)

        # Build Expression Section
        self.build_label = ttk.Label(self.main_frame, text="Build Your Expression (Click Symbols Below):")
        self.build_label.grid(row=3, column=0, columnspan=3, pady=5)

        # Current expression display
        self.expression_display = ttk.Label(self.main_frame, text="Current Expression: (empty)", font=("Arial", 12))
        self.expression_display.grid(row=4, column=0, columnspan=3, pady=5)

        # Clickable symbols grid
        self.symbols_frame = ttk.Frame(self.main_frame)
        self.symbols_frame.grid(row=5, column=0, columnspan=3, pady=5)
        self.symbol_buttons = {}
        row, col = 0, 0
        for symbol in symbols.keys():
            btn = ttk.Button(self.symbols_frame, text=symbol, width=5, command=lambda s=symbol: self.add_symbol(s))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.symbol_buttons[symbol] = btn
            col += 1
            if col > 4:  # 5 symbols per row
                col = 0
                row += 1

        # Additional operators
        self.operator_frame = ttk.Frame(self.main_frame)
        self.operator_frame.grid(row=6, column=0, columnspan=3, pady=5)
        ttk.Button(self.operator_frame, text="+", width=5, command=lambda: self.add_symbol("+")).grid(row=0, column=0, padx=2)
        ttk.Button(self.operator_frame, text="×", width=5, command=lambda: self.add_symbol("×")).grid(row=0, column=1, padx=2)
        ttk.Button(self.operator_frame, text="=", width=5, command=lambda: self.add_symbol("=")).grid(row=0, column=2, padx=2)
        ttk.Button(self.operator_frame, text="→", width=5, command=lambda: self.add_symbol("→")).grid(row=0, column=3, padx=2)
        ttk.Button(self.operator_frame, text="Clear", width=10, command=self.clear_expression).grid(row=0, column=4, padx=2)

        # Interpret built expression
        self.interpret_build_button = ttk.Button(self.main_frame, text="Interpret Built Expression", command=self.interpret_built_expression)
        self.interpret_build_button.grid(row=7, column=0, columnspan=3, pady=5)

        # Manual Expression Input
        self.expression_label = ttk.Label(self.main_frame, text="Or Enter a Symbolic Expression Manually (e.g., Ψ = ∴ + ◐):")
        self.expression_label.grid(row=8, column=0, columnspan=3, pady=5)
        self.expression_entry = ttk.Entry(self.main_frame, width=50)
        self.expression_entry.grid(row=9, column=0, columnspan=3, pady=5)
        self.interpret_button = ttk.Button(self.main_frame, text="Interpret Manual Expression", command=self.interpret_expression)
        self.interpret_button.grid(row=10, column=0, columnspan=3, pady=5)

        # Run Signal dropdown and button
        self.signal_label = ttk.Label(self.main_frame, text="Select a Signal to Simulate:")
        self.signal_label.grid(row=11, column=0, columnspan=3, pady=5)
        self.signal_var = tk.StringVar()
        self.signal_dropdown = ttk.Combobox(self.main_frame, textvariable=self.signal_var, values=list(signals.keys()))
        self.signal_dropdown.grid(row=12, column=0, columnspan=3, pady=5)
        self.run_signal_button = ttk.Button(self.main_frame, text="Run Signal", command=self.run_signal)
        self.run_signal_button.grid(row=13, column=0, columnspan=3, pady=5)

        # Explain Phenomenon dropdown and button
        self.phenomenon_label = ttk.Label(self.main_frame, text="Select a Phenomenon to Explain:")
        self.phenomenon_label.grid(row=14, column=0, columnspan=3, pady=5)
        self.phenomenon_var = tk.StringVar()
        self.phenomenon_dropdown = ttk.Combobox(self.main_frame, textvariable=self.phenomenon_var, values=list(phenomena.keys()))
        self.phenomenon_dropdown.grid(row=15, column=0, columnspan=3, pady=5)
        self.explain_phenomenon_button = ttk.Button(self.main_frame, text="Explain Phenomenon", command=self.explain_phenomenon)
        self.explain_phenomenon_button.grid(row=16, column=0, columnspan=3, pady=5)

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

    def interpret_built_expression(self):
        if not self.current_expression:
            self.output_area.insert(tk.END, "\nPlease build an expression using the symbols above.\n")
            return
        expression = " ".join(self.current_expression)
        result = interpret(expression, self.context)
        self.output_area.insert(tk.END, f"\n>>> {expression}\n{result}\n---\n")
        self.output_area.see(tk.END)

    def list_symbols(self):
        self.output_area.insert(tk.END, "\nAvailable Symbols and Their Meanings:\n")
        for symbol, func in symbols.items():
            func(self.context)
            self.output_area.insert(tk.END, f"- {symbol}: {self.context.get(symbol)}\n")
        self.output_area.see(tk.END)

    def list_phenomena(self):
        self.output_area.insert(tk.END, "\nKnown Cosmic Phenomena:\n")
        for name in phenomena:
            self.output_area.insert(tk.END, f"- {name}\n")
        self.output_area.see(tk.END)

    def list_signals(self):
        self.output_area.insert(tk.END, "\nAvailable Signals:\n")
        for name in signals:
            self.output_area.insert(tk.END, f"- {name}\n")
        self.output_area.see(tk.END)

    def interpret_expression(self):
        expression = self.expression_entry.get().strip()
        if not expression:
            self.output_area.insert(tk.END, "\nPlease enter a symbolic expression.\n")
            return
        result = interpret(expression, self.context)
        self.output_area.insert(tk.END, f"\n>>> {expression}\n{result}\n---\n")
        self.output_area.see(tk.END)

    def run_signal(self):
        sig_name = self.signal_var.get()
        if not sig_name:
            self.output_area.insert(tk.END, "\nPlease select a signal to simulate.\n")
            return
        if sig_name in signals:
            for line in signals[sig_name]:
                result = interpret(line, self.context)
                self.output_area.insert(tk.END, f"\n>>> {line}\n{result}\n---\n")
        else:
            self.output_area.insert(tk.END, f"\nUnknown signal: {sig_name}\n")
        self.output_area.see(tk.END)

    def explain_phenomenon(self):
        pheno = self.phenomenon_var.get()
        if not pheno:
            self.output_area.insert(tk.END, "\nPlease select a phenomenon to explain.\n")
            return
        if pheno in phenomena:
            eq, meaning = phenomena[pheno]
            self.output_area.insert(tk.END, f"\n{pheno}\n{eq}\n→ {meaning}\n---\n")
        else:
            self.output_area.insert(tk.END, f"\nUnknown phenomenon: {pheno}\n")
        self.output_area.see(tk.END)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = AlienSymbolicInterpreterGUI(root)
    root.mainloop()
