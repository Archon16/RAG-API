import requests

def test_kubernetes_query():
    print("Testing Kubernetes query...")
    response = requests.post("http://localhost:8000/query?q=What is the kubernetes?")

    if response.status_code != 200:
        raise Exception(f"Server returned: {response.status_code} {response.text}")
    
    answer = response.json()["answer"]

    #check for key concepts in the answer
    assert "kubernetes" in answer.lower(), "Missing 'orchestration' keyword"
    assert "container" in answer.lower(), "Missing 'container' keyword"

    print("Kubernetes query test passed !!")

def test_neetcode_query():
    print("Testing Neetcode query...")
    response = requests.post("http://localhost:8000/query?q=What is the Neetcode?")

    if response.status_code != 200:
        raise Exception(f"Server returned: {response.status_code} {response.text}")
    
    answer = response.json()["answer"]

    #check for key concepts in the answer
    assert "maximus" in answer.lower(), "Missing 'maximus' keyword"

    print("Neetcode query test passed !!")

if __name__ == "__main__":
    test_kubernetes_query()
    test_neetcode_query()
    print("All semantic tests passed !!")