# config_manager.py - Manages API keys for PuranaPata
import os
from dotenv import load_dotenv, set_key
import getpass

# Load environment variables from .env file if available
load_dotenv()

# API Keys Configuration
API_KEYS = {
    "WAYBACK_MACHINE": "WAYBACK_MACHINE_API_KEY",
    "VIRUSTOTAL": "VT_API_KEY",
    "ABUSEIPDB": "ABUSE_IPDB_KEY",
    "SHODAN": "SHODAN_API_KEY"
}

def request_api_key(service_name, env_var):
    """Prompts user for an API key if missing and stores it in .env"""
    print(f"⚠️ {service_name} API Key is missing.")
    api_key = getpass.getpass(f"Enter your {service_name} API Key: ")
    
    # Set the environment variable temporarily
    os.environ[env_var] = api_key

    # Store the key in .env for future use
    env_file = ".env"
    try:
        set_key(env_file, env_var, api_key)
        print(f"✅ {service_name} API Key saved successfully in {env_file}.")
    except Exception as e:
        print(f"❌ Failed to save API Key: {e}")

def check_api_keys():
    """Ensures all necessary API keys are set"""
    for service, env_var in API_KEYS.items():
        if not os.getenv(env_var):
            request_api_key(service, env_var)

def get_api_key(service_name):
    """Fetches the API key for a given service"""
    env_var = API_KEYS.get(service_name)
    return os.getenv(env_var) if env_var else None

# Entry point
if __name__ == "__main__":
    check_api_keys()
