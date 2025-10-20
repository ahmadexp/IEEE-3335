• Provides a general interface to configure devices that use DPLLs (Digital Phase Locked Loops)

• Utilises an underlying Netlink protocol to receive & request changes to a DPLL's configuration information

• An alternative to the sysfs interface

First introduced in version 6.7 and continuously updated to provide more capabilities
  Available at [kernel.org &](https://www.kernel.org/) on RHEL 9.4, CentOS Stream 9, OCP 4.14
Further patches are expected by end of year
It's strongly suggested to use latest available kernel release

### How does it work?

Uses a general purpose YNL utility to encode & decode netlink messages
Bases these messages on a DPLL YAML specification passed in as a parameter
Can then pass in request to dump/edit info with --dump & -do flags

```
python3 ./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml
```

Boilerplate for using API

Retrieve information on all DPLL devices with netlink command device-get & --dump flag:

./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --dump device-get

Retrieve information on a specific DPLL device with netlink command device-get & --do flag:

```
./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do device-get --json
'{"id":<id>}'
where: <id> = id of DPLL of interest
```

Retrieve information on all DPLL pins with netlink command pin-get & --dump flag:

./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --dump pin-get

```
Command Output
```

Snippet of Example Command Output

Retrieve information on a specific DPLL pin with netlink command pin-get & --do flag:

```
./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do pin-get --json
'{"id":<id>}'
where: <id> = id of pin of interest
```

# Modify a pin's attributes with netlink command pin-set & --do flag:

```
./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do pin-set --json
'{"id":<id>, "<attr>": "<value>"}'
where: <id> = id of pin of interest
         <attr> = attribute to be modified, 
         <value> = value to assign to attribute
```

Before Command After Command

Modify a pin's attributes on their directly connected DPLL(s) with netlink command pin-set & --do flag:

```
./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do pin-set --json
'{"id":<id>, "parent-device": {"parent-id":<p_id>, "<attr>":"<value>"}}'
where: <id> = id of pin of interest,
         <p_id> = id of parent DPLL,
         <attr> = attribute to be modified, 
         <value> = value to assign to attribute
```

Before Command After Command

Modify a child pin's attributes on their parent pin with netlink command pin-set & --do flag:

```
./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --do pin-set --json
'{"id":<id>, "parent-pin": {"parent-id":<p_id>, "<attr>":"<value>"}}'
where: <id> = id of pin of interest
         <p_id> = id of parent pin
         <attr> = attribute to be modified, 
         <value> = value to assign to attribute
```

Before Command

After Command

Output after pin -get

# Concatenate multiple --do operations with --multi flag:

```
./tools/net/ynl/cli.py --spec Documentation/netlink/specs/dpll.yaml --multi <do_operation> --multi 
<do_operation> …
```

```
where: <do_operation> = operation that would be encapsulated with a --do flag.
```

E.g. pin-get '{"id":20}'

Example Command

With Special Thanks to Arkadiusz Kubalewski, Zoli Fodor, Przemek Korba & Stephen P Mroczek