"""
Quickstart example for OpenRouter SDK.
"""
from sdk import RequestDispatcher

def main():
    client = RequestDispatcher(api_key="YOUR_API_KEY")
    # Example call
    response = client.dispatch("GET", "/api/v1/auth/key")
    print(response)

if __name__ == "__main__":
    main()
