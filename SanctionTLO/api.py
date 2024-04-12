import httpx

class SanctionTLO:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "closetcheaters.com"

    def tlo_ssn_lookup(self, fname, lname, dob):
        """
        Performs a synchronous SSN lookup using specified parameters.

        Parameters:
        - fname: First name of the individual.
        - lname: Last name of the individual.
        - dob: Date of birth of the individual in 'YYYY-MM-DD' format.

        Returns:
        A dictionary containing the lookup results or an error message.
        """
        
        params = {
            "tlo_type": "formatted",
            "fname": fname,
            "lname": lname,
            "dob": dob,
            "api_key": self.api_key
        }
        
        with httpx.Client() as client:
            try:
                response = client.get(f"http://{self.base_url}/sanction/telo/ssn", params=params)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                return f"Request error occurred: {e}"
            except httpx.HTTPStatusError as e:
                return f"HTTP error occurred: {e.response.status_code}"

    def tlo_basic_lookup(self, tlo_type, search):
        """
        Performs a basic lookup synchronously based on the provided type and search query.

        Parameters:
        - tlo_type: Type of the lookup ('email' or 'number').
        - search: The search query, such as an email address or phone number.

        Returns:
        A dictionary containing the lookup results or an error message.
        """
        params = {
            "tlo_type": tlo_type,
            "search": search,
            "api_key": self.api_key
        }
        with httpx.Client() as client:
            try:
                response = client.get(f"https://{self.base_url}/sanction/tlo/basic", params=params)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                return f"Request error occurred: {e}"
            except httpx.HTTPStatusError as e:
                return f"HTTP error occurred: {e.response.status_code}"

    def telo_lookup(self, fname, lname, street = None, city = None, state = None, zipcode = None, dob = None):
        """
        Performs a detailed TLO lookup synchronously with various parameters for a more specific search.

        Parameters:
        - fname: First name of the individual.
        - lname: Last name of the individual.
        - street: Optional. Street address of the individual.
        - city: Optional. City of the individual.
        - state: Optional. State of the individual.
        - zipcode: Optional. Zipcode of the individual.
        - dob: Optional. Date of birth of the individual in 'YYYY-MM-DD' format.

        Returns:
        A dictionary containing the lookup results or an error message.
        """
        params = {
            "fname": fname,
            "lname": lname,
            "api_key": self.api_key,
            "street": street,
            "city": city,
            "state": state,
            "zipcode": zipcode,
            "dob": dob
        }
        # Filter out None values
        params = {k: v for k, v in params.items() if v is not None}

        with httpx.Client() as client:
            try:
                response = client.get(f"https://{self.base_url}/sanction/tlo", params=params)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                return f"Request error occurred: {e}"
            except httpx.HTTPStatusError as e:
                return f"HTTP error occurred: {e.response.status_code}"

    def telo_number_lookup(self, number):
        """
        Performs a synchronous lookup for a given phone number using the provided API key.

        Parameters:
        - number: The phone number to look up.
        
        Returns:
        A dictionary containing the lookup results or an error message.
        """
        params = {
            "number": number,
            "api_key": self.api_key
        }

        with httpx.Client() as client:
            try:
                response = client.get(f"https://{self.base_url}/sanction/tlo/number", params=params)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                return f"Request error occurred: {e}"
            except httpx.HTTPStatusError as e:
                return f"HTTP error occurred: {e.response.status_code}"
