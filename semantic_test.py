import requests

def test_kubernetes_query():
    response = requests.post("http://localhost:8000/query?q=What is the kubernetes?")

    if response.status_code != 200:
        raise Exception(f"Server returned: {response.status_code} {response.text}")
    
    answer = response.json()["answer"]

    #check for key concepts in the answer
    assert "kubernetes" in answer.lower(), "Missing 'orchestration' keyword"
    assert "container" in answer.lower(), "Missing 'container' keyword"

    print("Kubernetes query test passed !!")

if __name__ == "__main__":
    test_kubernetes_query()
    print("All semantic tests passed !!")