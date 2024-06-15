# Data Conversion Experiment

This project is an experiment in converting sensitive data like wallet addresses into a more secure format for storage or transmission in systems and applications. The purpose is to enhance security and optimize storage requirements when handling sensitive user data.

## Motivation

When dealing with sensitive user data, such as wallet addresses, it is important to ensure that the data is stored and transmitted securely. One approach is to convert the data into a different format that obfuscates the original information, making it more difficult for unauthorized parties to access or interpret the sensitive data.

## Implementation

This Python script demonstrates a simple approach to converting wallet addresses into a list of integers representing the ASCII values of each character in the address. The script also provides functions to convert the list of integers back to the original string and generate a YAML configuration section for the converted data, which can be used in the circuit we're building.

The script defines three main functions:

1. `string_to_ints(input_str)`: Converts a string (e.g., a wallet address) to a list of integers representing the ASCII values of each character in the string.

2. `ints_to_string(int_list)`: Performs the inverse operation of `string_to_ints`, converting a list of integers back to a string.

3. `yaml_template(int_list)`: Generates a YAML configuration section for the given list of integers, which can be used in the circuit we're building.

## Usage

To use this script, simply run it with Python. It will demonstrate the conversion of a sample wallet address (`0x1234567890abcdef`) into a list of integers, convert the list back to a string, and generate a YAML configuration section for the converted data.

```python
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

Future Work
This project is a basic exploration of the concept of data conversion for security purposes. It serves as a starting point for further research and development into more robust and secure methods for handling sensitive user data in applications.
As the project progresses, we may require guidance or support from the Nillion team regarding best practices for secure data handling, integration with Nillion's privacy-preserving technologies, and potential use cases or applications within the Nillion ecosystem.
Contributing
As this is a simple proof of concept, there is no dedicated project link or team members to share at the moment. However, we are open to collaborating with others interested in this area and would be happy to provide our social handles upon request.
