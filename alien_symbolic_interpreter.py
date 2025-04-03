# Alien Symbolic Interpreter (Prototype v11 - GUI Version with Horizontal Layout and Improved Listings)
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
        self.root.title("👽 Alien Symbolic Interpreter (Prototype v11)")
        self.context = {}  # Initialize context for symbolic operations
        self.current_expression = []  # Store the current expression being built

        # Main frame with horizontal layout
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Left Column: Output Area
        self.output_frame = ttk.Frame(self.main_frame)
        self.output_frame.grid(row=0, column=0, padx=10, pady=5, sticky=(tk.N, tk.S))
        self.output_label = ttk.Label(self.output_frame, text="Output:")
        self.output_label.grid(row=0, column=0, pady=5)
        self.output_area = scrolledtext.ScrolledText(self.output_frame, width=40, height=20, wrap=tk.WORD)
        self.output_area.grid(row=1, column=0, pady=5)
        self.output_area.insert(tk.END, "Results will appear here.\nClick buttons to explore or build expressions.\n\n")

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
            btn = ttk.Button(self.symbols_frame, text=symbol, width=5, command=lambda s=symbol: self.add_symbol(s))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.symbol_buttons[symbol] = btn
            col += 1
            if col > 4:  # 5 symbols per row
                col = 0
                row += 1

        # Additional operators
        self.operator_frame = ttk.Frame(self.build_frame)
        self.operator_frame.grid(row=3, column=0, pady=5)
        ttk.Button(self.operator_frame, text="+", width=5, command=lambda: self.add_symbol("+")).grid(row=0, column=0, padx=2)
        ttk.Button(self.operator_frame, text="×", width=5, command=lambda: self.add_symbol("×")).grid(row=0, column=1, padx=2)
        ttk.Button(self.operator_frame, text="=", width=5, command=lambda: self.add_symbol("=")).grid(row=0, column=2, padx=2)
        ttk.Button(self.operator_frame, text="→", width=5, command=lambda: self.add_symbol("→")).grid(row=0, column=3, padx=2)
        ttk.Button(self.operator_frame, text="Clear", width=10, command=self.clear_expression).grid(row=0, column=4, padx=2)

        # Interpret built expression
        self.interpret_build_button = ttk.Button(self.build_frame, text="Interpret Built Expression", command=self.interpret_built_expression)
        self.interpret_build_button.grid(row=4, column=0, pady=5)

        # Right Column: Controls
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.grid(row=0, column=2, padx=10, pady=5, sticky=(tk.N))

        # List buttons
        self.symbols_button = ttk.Button(self.controls_frame, text="List Symbols", command=self.list_symbols)
        self.symbols_button.grid(row=0, column=0, pady=5, sticky=(tk.W, tk.E))
        self.phenomena_button = ttk.Button(self.controls_frame, text="List Phenomena", command=self.list_phenomena)
        self.phenomena_button.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))
        self.signals_button = ttk.Button(self.controls_frame, text="List Signals", command=self.list_signals)
        self.signals_button.grid(row=2, column=0, pady=5, sticky=(tk.W, tk.E))

        # Manual Expression Input
        self.expression_label = ttk.Label(self.controls_frame, text="Enter Expression Manually:")
        self.expression_label.grid(row=3, column=0, pady=5)
        self.expression_entry = ttk.Entry(self.controls_frame, width=30)
        self.expression_entry.grid(row=4, column=0, pady=5)
        self.interpret_button = ttk.Button(self.controls_frame, text="Interpret Manual", command=self.interpret_expression)
        self.interpret_button.grid(row=5, column=0, pady=5, sticky=(tk.W, tk.E))

        # Run Signal
        self.signal_label = ttk.Label(self.controls_frame, text="Simulate a Signal:")
        self.signal_label.grid(row=6, column=0, pady=5)
        self.signal_var = tk.StringVar()
        self.signal_dropdown = ttk.Combobox(self.controls_frame, textvariable=self.signal_var, values=list(signals.keys()), width=27)
        self.signal_dropdown.grid(row=7, column=0, pady=5)
        self.run_signal_button = ttk.Button(self.controls_frame, text="Run Signal", command=self.run_signal)
        self.run_signal_button.grid(row=8, column=0, pady=5, sticky=(tk.W, tk.E))

        # Explain Phenomenon
        self.phenomenon_label = ttk.Label(self.controls_frame, text="Explain a Phenomenon:")
        self.phenomenon_label.grid(row=9, column=0, pady=5)
        self.phenomenon_var = tk.StringVar()
        self.phenomenon_dropdown = ttk.Combobox(self.controls_frame, textvariable=self.phenomenon_var, values=list(phenomena.keys()), width=27)
        self.phenomenon_dropdown.grid(row=10, column=0, pady=5)
        self.explain_phenomenon_button = ttk.Button(self.controls_frame, text="Explain Phenomenon", command=self.explain_phenomenon)
        self.explain_phenomenon_button.grid(row=11, column=0, pady=5, sticky=(tk.W, tk.E))

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
        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Available Symbols")
        popup.geometry("500x400")

        # Create a Treeview (table)
        tree = ttk.Treeview(popup, columns=("Symbol", "Meaning"), show="headings")
        tree.heading("Symbol", text="Symbol")
        tree.heading("Meaning", text="Meaning")
        tree.column("Symbol", width=100, anchor="center")
        tree.column("Meaning", width=350)

        # Populate the table
        for symbol, func in symbols.items():
            func(self.context)
            tree.insert("", tk.END, values=(symbol, self.context.get(symbol)), tags=("symbol",))
        
        # Style the table
        tree.tag_configure("symbol", foreground="blue")
        tree.pack(expand=True, fill="both", padx=10, pady=10)

    def list_phenomena(self):
        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Known Cosmic Phenomena")
        popup.geometry("600x400")

        # Create a Treeview (table)
        tree = ttk.Treeview(popup, columns=("Phenomenon", "Equation", "Meaning"), show="headings")
        tree.heading("Phenomenon", text="Phenomenon")
        tree.heading("Equation", text="Equation")
        tree.heading("Meaning", text="Meaning")
        tree.column("Phenomenon", width=200)
        tree.column("Equation", width=150)
        tree.column("Meaning", width=250)

        # Populate the table
        for name, (eq, meaning) in phenomena.items():
            tree.insert("", tk.END, values=(name, eq, meaning), tags=("phenomenon",))
        
        # Style the table
        tree.tag_configure("phenomenon", foreground="darkgreen")
        tree.pack(expand=True, fill="both", padx=10, pady=10)

    def list_signals(self):
        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Available Signals")
        popup.geometry("300x200")

        # Create a Treeview (table)
        tree = ttk.Treeview(popup, columns=("Signal",), show="headings")
        tree.heading("Signal", text="Signal")
        tree.column("Signal", width=200, anchor="center")

        # Populate the table
        for name in signals:
            tree.insert("", tk.END, values=(name,))
        
        tree.pack(expand=True, fill="both", padx=10, pady=10)

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
    root.geometry("1000x500")  # Set a reasonable window size
    app = AlienSymbolicInterpreterGUI(root)
    root.mainloop()
