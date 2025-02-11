import requests

def get_publi_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=text", timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao obter IP público: {e}")
        return None

if __name__ == "__main__":
    ip = get_public_ip()
    if ip:
        print(f"IP público: {ip}")
