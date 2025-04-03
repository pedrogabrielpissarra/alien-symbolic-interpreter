# Alien Symbolic Interpreter (Prototype v8 - GUI Version with Tkinter)
# Each symbol maps to a concept or function with simulated behavior

import random
import tkinter as tk
from tkinter import ttk, scrolledtext

# Symbol-function mapping (with simulated behaviors)
symbols = {
    "●": lambda ctx: ctx.update({"●": "Universe Initialized"}),
    "◐": lambda ctx: ctx.update({"◐": "Condition Split"}),
    "∴": lambda ctx: ctx.update({"∴": ["Option A", "Option B", "Option C"]}),
    "✧": lambda ctx: ctx.update({"✧": random.choice(ctx.get("∴", ["Unknown"]))}),
    "Ψ": lambda ctx: ctx.update({"Ψ": "Quantum Potential"}),
    "∅": lambda ctx: ctx.update({"∅": None}),
    "꩜": lambda ctx: ctx.update({"꩜": "Dimensional Fold Opened"}),
    "⧗": lambda ctx: ctx.update({"⧗": "Entangled Pair Linked"}),
    "⇌": lambda ctx: ctx.update({"⇌": "Oscillation Active"}),
    "⬠": lambda ctx: ctx.update({"⬠": "Network Transmission"}),
    "⇧": lambda ctx: ctx.update({"⇧": "Expanding"}),
    "Ω": lambda ctx: ctx.update({"Ω": ctx.get("✧", "Observed Reality")}),
    "⇀": lambda ctx: ctx.update({"⇀": "Subtle Motion"}),
    "ϕ": lambda ctx: ctx.update({"ϕ": "Spiral Growth"}),
    "∞": lambda ctx: ctx.update({"∞": "Infinite Potential"}),
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
    "FRB 121102": ["∞ ⇌ ⇧ = ⧗ × ϕ"],
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
        return f"{origin} → {target} => {context.get(target)}"

    tokens = expression.replace("=", " = ").split()
    output = []
    for token in tokens:
        if token in symbols:
            symbols[token](context)
            output.append(f"{token} => {context.get(token)}")
        elif token == "=":
            output.append("=")
        else:
            output.append(token)
    return " ".join(output)

# GUI Application
class AlienSymbolicInterpreterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("👽 Alien Symbolic Interpreter (Prototype v8)")
        self.context = {}  # Initialize context for symbolic operations

        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Welcome message
        self.welcome_label = ttk.Label(self.main_frame, text="Welcome to the Alien Symbolic Interpreter!\nExplore the universe through a language of shapes.", justify="center")
        self.welcome_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Output area (scrolled text)
        self.output_area = scrolledtext.ScrolledText(self.main_frame, width=60, height=15, wrap=tk.WORD)
        self.output_area.grid(row=1, column=0, columnspan=3, pady=10)
        self.output_area.insert(tk.END, "Click the buttons below to explore symbols, phenomena, and signals.\nOr enter a symbolic expression and click 'Interpret'.\n\n")

        # Symbols button
        self.symbols_button = ttk.Button(self.main_frame, text="List Symbols", command=self.list_symbols)
        self.symbols_button.grid(row=2, column=0, padx=5, pady=5)

        # Phenomena button
        self.phenomena_button = ttk.Button(self.main_frame, text="List Phenomena", command=self.list_phenomena)
        self.phenomena_button.grid(row=2, column=1, padx=5, pady=5)

        # Signals button
        self.signals_button = ttk.Button(self.main_frame, text="List Signals", command=self.list_signals)
        self.signals_button.grid(row=2, column=2, padx=5, pady=5)

        # Expression input
        self.expression_label = ttk.Label(self.main_frame, text="Enter a Symbolic Expression (e.g., Ψ = ∴ + ◐):")
        self.expression_label.grid(row=3, column=0, columnspan=3, pady=5)
        self.expression_entry = ttk.Entry(self.main_frame, width=50)
        self.expression_entry.grid(row=4, column=0, columnspan=3, pady=5)

        # Interpret button
        self.interpret_button = ttk.Button(self.main_frame, text="Interpret Expression", command=self.interpret_expression)
        self.interpret_button.grid(row=5, column=0, columnspan=3, pady=5)

        # Run Signal dropdown and button
        self.signal_label = ttk.Label(self.main_frame, text="Select a Signal to Simulate:")
        self.signal_label.grid(row=6, column=0, columnspan=3, pady=5)
        self.signal_var = tk.StringVar()
        self.signal_dropdown = ttk.Combobox(self.main_frame, textvariable=self.signal_var, values=list(signals.keys()))
        self.signal_dropdown.grid(row=7, column=0, columnspan=3, pady=5)
        self.run_signal_button = ttk.Button(self.main_frame, text="Run Signal", command=self.run_signal)
        self.run_signal_button.grid(row=8, column=0, columnspan=3, pady=5)

        # Explain Phenomenon dropdown and button
        self.phenomenon_label = ttk.Label(self.main_frame, text="Select a Phenomenon to Explain:")
        self.phenomenon_label.grid(row=9, column=0, columnspan=3, pady=5)
        self.phenomenon_var = tk.StringVar()
        self.phenomenon_dropdown = ttk.Combobox(self.main_frame, textvariable=self.phenomenon_var, values=list(phenomena.keys()))
        self.phenomenon_dropdown.grid(row=10, column=0, columnspan=3, pady=5)
        self.explain_phenomenon_button = ttk.Button(self.main_frame, text="Explain Phenomenon", command=self.explain_phenomenon)
        self.explain_phenomenon_button.grid(row=11, column=0, columnspan=3, pady=5)

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
