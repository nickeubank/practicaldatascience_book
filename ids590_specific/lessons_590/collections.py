import numpy as np
import numpy.random as npr

heart_rates = [
    159,
    82,
    138,
    132,
    127,
    90,
    147,
    113,
    139,
    79,
    145,
    109,
    129,
    77,
    92,
    155,
    74,
    130,
    109,
    131,
]

poohs_contacts = set(
    [
        "Piglet",
        "Rabbit",
        "Eeyore",
        "Piglet",
        "Piglet",
        "Eeyore",
        "Christopher",
        "Roo",
        "Rabbit",
        "Piglet",
        "Piglet",
        "Rabbit",
        "Owl",
    ]
)


owls_contacts = set(
    [
        "Eeyore",
        "Eeyore",
        "Rabbit",
        "Eeyore",
        "Piglet",
        "Eeyore",
        "Rabbit",
        "Piglet",
        "Piglet",
        "Rabbit",
        "Christopher",
    ]
)


poohs_contacts.difference(owls_contacts)
poohs_contacts.intersection(owls_contacts)



politicians = dict()

politicians["Lyra"] = ["Pantalaimon", "Lee Scoresby", "Iorek"]
politicians["Lord Asriel"] = ["Ms. Coulter"]
