# Slide 1

## The Linux Kernel DPLL SubsystemHugo Ongetta-Dagnoni

NEX

---

# Slide 2

Provides a general interface to configure devices that use DPLLs (Digital Phase Locked Loops)

Utilises an underlying Netlink protocol to receive & request changes to a DPLL’s configuration information 

An alternative to the sysfs interface

## Introduction to the API

NEX

---

# Slide 3

First introduced in version 6.7 and continuously updated to provide more capabilities
Available at kernel.org & on RHEL 9.4, CentOS Stream 9, OCP 4.14

Further patches are expected by end of year

It’s strongly suggested to use latest available kernel release

## History & Development

NEX

---

# Slide 4

The sysfs interface was designed to be used as an out-of-tree solution with Intel proprietary configuration options.

New API was created to be used upstream & industry-wide and was later backported
New patches can be submitted according to community needs

Support for sysfs will continue
With support eventually ending

## Transitioning from the sysfs Interface

NEX

---

# Slide 5

Uses a general purpose YNL utility to encode & decode netlink messages

Bases these messages on a DPLL YAML specification passed in as a parameter

Can then pass in request to dump/edit info with --dump & --do flags

Boilerplate for using API

## How does it work?

![Image 1](DPLL API P3335 Presentation_images/slide_5_image_1.png)

NEX

---

# Slide 6

Retrieve information on all DPLL devices with netlink command device-get & --dump flag:
	./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --dump device-get

## --dump device-get

![Image 2](DPLL API P3335 Presentation_images/slide_6_image_2.png)

Example Command Output

NEX

---

# Slide 7

Retrieve information on a specific DPLL device with netlink command device-get & --do flag:
	./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do device-get --json 	‘{“id”:<id>}’
	where: 	<id> = id of DPLL of interest

## --do device-get

![Image 3](DPLL API P3335 Presentation_images/slide_7_image_3.png)

Example Command Output

NEX

---

# Slide 8

Retrieve information on all DPLL pins with netlink command         pin-get & --dump flag:
	./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --dump pin-get

## --dump pin-get

Command Output

![Image 4](DPLL API P3335 Presentation_images/slide_8_image_4.png)

Snippet of Example Command Output

NEX

---

# Slide 9

Retrieve information on a specific DPLL pin with netlink command pin-get & --do flag:
	./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do pin-get --json 	‘{“id”:<id>}’
	where: 	<id> = id of pin of interest

## --do pin-get

Example Command Output

![Image 5](DPLL API P3335 Presentation_images/slide_9_image_5.png)

NEX

---

# Slide 10

![Image 6](DPLL API P3335 Presentation_images/slide_10_image_6.png)

Modify a pin’s attributes with netlink command pin-set & --do flag:
	./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do pin-set --json 	‘{“id”:<id>, “<attr>”: “<value>”}’
	where: 	<id> = id of pin of interest
		<attr> = attribute to be modified, 
		<value> = value to assign to 	attribute

## --do pin-set

Example Command Output

NEX

---

# Slide 11

![Image 7](DPLL API P3335 Presentation_images/slide_11_image_7.png)

![Image 8](DPLL API P3335 Presentation_images/slide_11_image_8.png)

## --do pin-set

Before Command

After Command

NEX

---

# Slide 12

Modify a pin’s attributes on their directly connected DPLL(s) with netlink command pin-set & --do flag: 
	./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do pin-set --json 	‘{“id”:<id>, “parent-device”: {“parent-id”:<p_id>, “<attr>”:”<value>”}}’
	where: 	<id> = id of pin of interest,
		<p_id> = id of parent DPLL,
		<attr> = attribute to be modified, 
		<value> = value to assign to 	attribute

## --do pin-set on Parent DPLL

Example Command Output

![Image 9](DPLL API P3335 Presentation_images/slide_12_image_9.png)

NEX

---

# Slide 13

![Image 10](DPLL API P3335 Presentation_images/slide_13_image_10.png)

![Image 11](DPLL API P3335 Presentation_images/slide_13_image_11.png)

## --do pin-set on Parent DPLL

Before Command

After Command

NEX

---

# Slide 14

![Image 12](DPLL API P3335 Presentation_images/slide_14_image_12.png)

Modify a child pin’s attributes on their parent pin with netlink command pin-set & --do flag: 
	./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do pin-set --json 	‘{“id”:<id>, “parent-pin”: {“parent-id”:<p_id>, “<attr>”:”<value>”}}’
	where: 	<id> = id of pin of interest
		<p_id> = id of parent pin
		<attr> = attribute to be modified, 
		<value> = value to assign to 	attribute

## --do pin-set on Parent Pin

Example Command Output

![Image 13](DPLL API P3335 Presentation_images/slide_14_image_13.png)

NEX

---

# Slide 15

## --do pin-set on Parent Pin

![Image 14](DPLL API P3335 Presentation_images/slide_15_image_14.png)

![Image 15](DPLL API P3335 Presentation_images/slide_15_image_15.png)

Before Command

After Command

NEX

---

# Slide 16

![Image 16](DPLL API P3335 Presentation_images/slide_16_image_16.png)

## --do pin-set on Parent Pin

Output after pin-get

NEX

---

# Slide 17

Concatenate multiple --do operations with --multi flag: 
	./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --multi <do_operation> --multi 	<do_operation> … 
	where: 	<do_operation> = operation that would be encapsulated with a --do flag. 
				E.g. pin-get ‘{“id”:20}’

## --multi flag

Example Command

![Image 17](DPLL API P3335 Presentation_images/slide_17_image_17.png)

NEX

---

# Slide 18

## --multi flag

![Image 18](DPLL API P3335 Presentation_images/slide_18_image_18.png)

Example Command Output

NEX

---

# Slide 19

## Live Demonstration

NEX

---

# Slide 20

## Thank you Any questions?

With Special Thanks to 
Arkadiusz Kubalewski, Zoli Fodor, Przemek Korba & Stephen P Mroczek

NEX

---
