

plan = """
                    W1

   ┌─┐  ┌─────────────────────────┐  ┌─┐      ──┐
   │ │  └─────────────────────────┘  │ │        │
   │ │                               │ │        │
   │ │  ┌─────────────────────────┐  │ │        │
┌┐ │ │  │                         │  │ │ ┌┐     │                                                ┌─┐
││ │ │  │                         │  │ │ ││     │                                                │ │
││ │ │  │                         │  │ │ ││     │                             D1                 │ │
││ │ │  │                         │  │ │ ││     │             ┌─┐ ┌────────────────────────┐ ┌─┐ │ │
││ │ │  │                         │  │ │ ││     │             │ │ │                        │ │ │ │ │
││ │ │  │                         │  │ │ ││     │             │ │ │                        │ │ │ │ │
││ │ │  │  D1                     │  │ │ ││     │D2       H1  │ │ │                        │ │ │ │ │  H2
││ │ │  │                         │  │ │ ││     │             │ │ │                        │ │ │ │ │
││ │ │  │                         │  │ │ ││     │             │ │ │                        │ │ │ │ │
││ │ │  │                         │  │ │ ││     │             │ │ │                        │ │ │ │ │
││ │ │  │                         │  │ │ ││     │             └─┘ └────────────────────────┘ └─┘ └─┘
││ │ │  │                         │  │ │ ││     │
││ │ │  │                         │  │ │ ││     │
││ │ │  └─────────────────────────┘  │ │ ││     │
││ │ │                               │ │ ││     │
││ │ │  ┌─────────────────────────┐  │ │ ││     │
└┘ └─┘  └─────────────────────────┘  └─┘ └┘   ──┘

┌─────────────────────────────────────────┐
└─────────────────────────────────────────┘
                    W2"""


def getInputFloatWithDefault(label, default):
  answer = input(f"{label}, default={default} (enter for default) = ")
  try:
    value = float(answer)
    return value
  except:
    return default


cabinet_height = getInputFloatWithDefault("Enter Cabintet Height", 87.5)
cabinet_width = getInputFloatWithDefault("Enter Cabintet Width", 45.0)
cabinet_depth = getInputFloatWithDefault("Enter Cabintet Depth", 45.0)
spacing = getInputFloatWithDefault("Enter DrawerSpacing", 0.2)
count = getInputFloatWithDefault("Enter Drawer Count", 3)
wood_thinkness = getInputFloatWithDefault("Enter Plywood Thickness", 1.2)
slider_thinkness = getInputFloatWithDefault("Enter Slider Thickness", 1.27)


spacing_total = (count+1) * spacing

W2 = cabinet_width - (2 * spacing)
W1 = W2 - (2 * wood_thinkness) - (2 * slider_thinkness)

D2 = cabinet_depth - wood_thinkness
D1 = D2 - (2 * wood_thinkness)

H2 = (cabinet_height - spacing_total) / count
H1 = H2 - 4.0

print()
print(plan)
print()

print(f"D1 = {D1:.2f}")
print(f"D2 = {D2:.2f}")

print(f"W1 = {W1:.2f}")
print(f"W2 = {W2:.2f}")

print(f"H1 = {H1:.2f}")
print(f"H2 = {H2:.2f}")

print()

print("Cut list = ")
print(f"{count} x Box bottom       @ {W1:.2f} x {D1:.2f}")
print(f"{count*2} x Box front&back   @ {W1:.2f} x {H1:.2f}")
print(f"{count*2} x Box sides        @ {D2:.2f} x {H1:.2f}")
print(f"{count} x Drawer face      @ {H2:.2f} x {W2:.2f}")

