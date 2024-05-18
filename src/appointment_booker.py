from src.api import get_bearer_token, get_appointments

if __name__ == "__main__":
    token = get_bearer_token()
    print(get_appointments(token))