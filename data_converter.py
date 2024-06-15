"""
I'm experimenting with converting data like wallet addresses into a format
that can be used in the systems or applications we're building. For example,
we might want to store user wallet addresses as integers for security or
storage efficiency reasons.
"""

import yaml

def string_to_ints(input_str):
    """
    Converts a string to a list of integers representing the ASCII values
    of each character in the string.

    Args:
        input_str (str): The string to be converted.

    Returns:
        list: A list of integers representing the ASCII values of each
              character in the input string.
    """
    return [ord(char) for char in input_str]

def ints_to_string(int_list):
    """
    Converts a list of integers back to a string.
    Inverse of the string_to_ints function.

    Args:
        int_list (list): A list of integers to be converted.

    Returns:
        str: The string reconstructed from the list of integers.
    """
    return ''.join(chr(int_val) for int_val in int_list)

def yaml_template(int_list):
    """
    Generates a YAML configuration section for the given list of integers.
    This YAML section can be used in the circuit we're building.

    Args:
        int_list (list): A list of integers.

    Returns:
        str: The YAML configuration section.
    """
    as_yaml_config = yaml.dump({
        "public_variables": {
            "inner_type": "Integer",
            "values": [{"Integer": x} for x in int_list],
        }
    })
    return as_yaml_config

# Example usage
wallet_address = "0x1234567890abcdef"
print(f"Wallet address: {wallet_address}")

# Convert wallet address to a list of integers
wallet_ints = string_to_ints(wallet_address)
print(f"Wallet address as integers: {wallet_ints}")

# Convert the list of integers back to a string
recovered_address = ints_to_string(wallet_ints)
print(f"Reconstructed wallet address: {recovered_address}")

# Generate the YAML configuration section
yaml_config = yaml_template(wallet_ints)
print(f"YAML configuration section:\n{yaml_config}")

# Verify that the original and reconstructed addresses match
assert wallet_address == recovered_address, "Wallet address conversion failed!"
print("Wallet address conversion successful!")