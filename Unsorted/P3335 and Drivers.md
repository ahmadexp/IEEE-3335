# Slide 1

## P3335 and Drivers

Doug Arnold
2024-09-18

---

# Slide 2

## Driver stack

Hardware

Register map

Translation layer

Software API

Specific to timecard manufacturer
Based on P3335 hardware specifications

Specific to open-source project:
Specific programming language
Specific supported operating system(s)
Based on P3335 information model

Note P3335 does not directly specify any layer of this stack

---

# Slide 3

## P3335 Information Model

List of timecard attributes
May be bundled in structures
Each attribute characterized as:
Static (get only)
Dynamic (get only)
Configurable (set and get)
Attribute data types
For example: Uinterget32 in units of seconds

---
