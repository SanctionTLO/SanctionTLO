from SanctionTLO import SanctionTLOAPI

api = SanctionTLOAPI(api_key="YOUR_API_KEY")

def SSN_Lookup():
    result = api.tlo_ssn_lookup("John", "Doe", "1990-01-01")
    print(result)

def Basic_Lookup():
    result = api.tlo_basic_lookup("email", "john.doe@example.com")
    print(result)

def TLO_Lookup():
    result = api.telo_lookup("John", "Doe", "123 Main St", "Anytown", "Anystate", "12345", "1990-01-01")
    print(result)

def Number_Lookup():
    result = api.telo_number_lookup("15551234567")
    print(result)

if __name__ == "__main__":
    SSN_Lookup()
    Basic_Lookup()
    TLO_Lookup()
    Number_Lookup()
