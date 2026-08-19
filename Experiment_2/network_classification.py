# Network Device and Transmission Media Classification

network_info = {
    "Switch": {
        "layer": "Layer 2 - Data Link",
        "function": "Connects devices within a LAN and forwards frames using MAC addresses."
    },

    "Router": {
        "layer": "Layer 3 - Network",
        "function": "Connects different networks and forwards packets using IP addresses."
    },

    "Bridge": {
        "layer": "Layer 2 - Data Link",
        "function": "Connects and filters traffic between LAN segments using MAC addresses."
    },

    "Access Point": {
        "layer": "Layer 2 - Data Link",
        "function": "Provides wireless access and connects wireless devices to a wired LAN."
    },

    "Twisted Pair Cable": {
        "layer": "Layer 1 - Physical",
        "function": "Transmits data using electrical signals through copper wires."
    },

    "Coaxial Cable": {
        "layer": "Layer 1 - Physical",
        "function": "Transmits data using electrical signals through a copper conductor."
    },

    "Fiber Optic Cable": {
        "layer": "Layer 1 - Physical",
        "function": "Transmits data using pulses of light through optical fibers."
    },

    "Wireless": {
        "layer": "Layer 1 - Physical",
        "function": "Transmits data through radio waves without physical cables."
    }
}


def classification_report(items):
    print("\n========== NETWORK CLASSIFICATION REPORT ==========\n")

    for item in items:

        if item in network_info:
            info = network_info[item]

            print("Device/Medium :", item)
            print("Layer         :", info["layer"])
            print("Primary Role  :", info["function"])
            print("-" * 60)

        else:
            print("Device/Medium :", item)
            print("Status        : Unknown")
            print("-" * 60)


items = [
    "Switch",
    "Router",
    "Bridge",
    "Access Point",
    "Twisted Pair Cable",
    "Coaxial Cable",
    "Fiber Optic Cable",
    "Wireless"
]

classification_report(items)
