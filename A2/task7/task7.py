import re


class RegexHandler:

    def __init__(self, email_pattern) -> None:
        self.email_pattern = '^([a-zA-Z]+\.?){1,}@([a-zA-Z]+\.?){1,}'

    def validate_email(self, str2check: str) -> bool:
        email_match = re.match(email_pattern, str2check)
        print(email_match)
        if not email_match:
            return True
        return False
        
    def validate_phone(self, str2check: str) -> bool:
        pass


def prop_email_matcher(prop_fpath: str, email_fpath: str) -> str:
    pass


def prop_phone_matcher(prop_fpath: str, phone_fpath: str) -> str:
    pass


def merge_prop_email_phone(prop_fpath: str, email_phone_fpath: str) -> str:
    pass
    

if __name__ == "__main__":
    print("Task 1 results: ")
    print(prop_email_matcher("sample_properties.csv", "sample_properties_email_phone.csv"))
    print("="*50)
    print("Task 2 results: ")
    print(prop_phone_matcher("sample_properties.csv", "sample_properties_email_phone.csv"))
    print("="*50)
    print("Task 3 results: ")
    print(merge_prop_email_phone("sample_properties.csv", "sample_properties_email_phone.csv"))

