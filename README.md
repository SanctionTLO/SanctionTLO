
# SanctionTLO

The 'SanctionTLOAPI' library was created to provide an easy way to use SanctionTLO in Python. It helps with background checks and compliance by allowing you to search for someone's details using their SSN, email, or phone number. It also includes advanced searches and phone number lookups.

## Features

- **SSN Lookup**: Perform SSN verifications to check individual backgrounds.
- **Basic Lookup**: Retrieve basic information using an email address or phone number.
- **Detailed TLO Lookup**: Conduct comprehensive searches using multiple parameters for detailed background checks.
- **Phone Number Lookup**: Get detailed information associated with a phone number.

## Installation

To incorporate `SanctionTLO` into your project, clone the repository and install it manually:

```bash
git clone https://github.com/SanctionTLO/SanctionTLO.git
```

```bash
cd SanctionTLO/SanctionTLO
```

```bash
python setup.py install
```

## Getting Started

Here's a quick example of how to perform an SSN lookup using `SanctionTLOAPI`:

```python
from SanctionTLOAPI import SanctionTLOAPI

# Initialize the API with your TLO API key
api = SanctionTLOAPI(api_key="your_api_key_here")

# Perform an SSN lookup
response = api.tlo_ssn_lookup(
    fname="John",
    lname="Doe",
    dob="1990-01-01"
)

print(response)
```

## Documentation

For a more comprehensive guide to the `SanctionTLO` library's capabilities and how to use it for different types of lookups, refer to the included documentation and example scripts.

## Examples

You'll find more examples on how to utilize the `SanctionTLO` for various lookup operations in the project's `tests` directory.

## Contributing

Contributions are highly appreciated! If you'd like to help improve `SanctionTLO`, please check out the contributing guidelines.

## License

`SanctionTLO` is released under the MIT License. See the LICENSE file in the repository for more information.

## Support and Contact

Encountering issues or have questions? Feel free to open an issue on the [GitHub issue tracker](https://github.com/SanctionTLO/SanctionTLO/issues).

---

We hope `SanctionTLO` empowers your applications with efficient access to TLO's sanction lookup services. Happy coding!
