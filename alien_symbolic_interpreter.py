# Alien Symbolic Interpreter (Prototype v7 - CLI Version with Enhanced UX)
# Each symbol maps to a concept or function with simulated behavior

import random

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

# Example expressions for demonstration
examples = [
    ("Ψ = ∴ + ◐", "Simulates quantum superposition: combining possibilities and a split condition to form a quantum state."),
    ("run Wow!", "Runs the Wow! Signal simulation: a totality oscillating into a collapse."),
    ("explain Big Bang", "Explains the Big Bang phenomenon using its symbolic equation and meaning.")
]

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

# CLI runner for symbolic scripts
def run_script(script_lines, context):
    for line in script_lines:
        print(f">>> {line}")
        print(interpret(line, context))
        print("---")

# Main CLI loop
if __name__ == "__main__":
    context = {}  # Initialize an empty context for each session
    print("👽 Welcome to the Alien Symbolic Interpreter (Prototype v7) 👽")
    print("This tool simulates a 'language of shapes' for cosmic signals and phenomena.")
    print("Explore the universe through symbolic equations inspired by real physics!")
    print("\nHow to Use:")
    print("- Type 'help' to see all available commands.")
    print("- Type 'symbols' to list all available symbols and their meanings.")
    print("- Type 'signals' to list preset cosmic signals (e.g., Wow!, FRB 121102).")
    print("- Type 'phenomena' to list known cosmic phenomena (e.g., Quantum Superposition).")
    print("- Type 'examples' to see example commands to get started.")
    print("- Type 'run SIGNAL_NAME' to simulate a signal (e.g., 'run Wow!').")
    print("- Type 'explain PHENOMENON_NAME' to learn about a phenomenon (e.g., 'explain Big Bang').")
    print("- Or type a symbolic expression directly (e.g., 'Ψ = ∴ + ◐').")
    print("- Type 'exit' to quit.")
    print("\nTry starting with 'examples' or 'help' to get a feel for the tool!")

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "exit":
            print("Goodbye, human. Keep exploring the cosmos!")
            break

        elif user_input.lower() == "help":
            print("\nAvailable Commands:")
            print("- help: Show this help message.")
            print("- symbols: List all available symbols and their meanings.")
            print("- signals: List preset cosmic signals (e.g., Wow!, FRB 121102).")
            print("- phenomena: List known cosmic phenomena (e.g., Quantum Superposition).")
            print("- examples: Show example commands to get started.")
            print("- run SIGNAL_NAME: Simulate a cosmic signal (e.g., 'run Wow!').")
            print("- explain PHENOMENON_NAME: Learn about a phenomenon (e.g., 'explain Big Bang').")
            print("- [expression]: Type a symbolic expression directly (e.g., 'Ψ = ∴ + ◐').")
            print("- exit: Quit the program.")

        elif user_input.lower() == "symbols":
            print("\nAvailable Symbols and Their Meanings:")
            for symbol, func in symbols.items():
                func(context)  # Update context to get the meaning
                print(f"- {symbol}: {context.get(symbol)}")

        elif user_input.lower() == "signals":
            print("\nAvailable Signals:")
            for name in signals:
                print(f"- {name}")

        elif user_input.lower() == "phenomena":
            print("\nKnown Cosmic Phenomena:")
            for name in phenomena:
                print(f"- {name}")

        elif user_input.lower() == "examples":
            print("\nExample Commands to Get Started:")
            for cmd, desc in examples:
                print(f"- '{cmd}': {desc}")

        elif user_input.startswith("run "):
            sig_name = user_input[4:].strip()
            if sig_name in signals:
                run_script(signals[sig_name], context)
            else:
                print(f"Unknown signal: {sig_name}. Type 'signals' to see available options.")

        elif user_input.startswith("explain "):
            pheno = user_input[8:].strip()
            if pheno in phenomena:
                eq, meaning = phenomena[pheno]
                print(f"\n{pheno}\n{eq}\n→ {meaning}")
            else:
                print(f"Unknown phenomenon: {pheno}. Type 'phenomena' to see available options.")

        else:
            print(interpret(user_input, context))
