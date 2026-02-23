import requests
import json

API_BASE = "http://localhost:5000"

def test_health():
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{API_BASE}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        print("Health check: PASSED\n")
        return True
    except Exception as e:
        print(f"Health check: FAILED - {e}\n")
        return False

def test_skills():
    print("Testing skills endpoint...")
    try:
        response = requests.get(f"{API_BASE}/skills")
        skills = response.json()
        print(f"Available skills: {skills}")
        print("Skills endpoint: PASSED\n")
        return True
    except Exception as e:
        print(f"Skills endpoint: FAILED - {e}\n")
        return False

def test_generate_roadmap():
    print("Testing roadmap generation...")
    try:
        response = requests.post(
            f"{API_BASE}/generate",
            json={"skill": "python"},
            headers={"Content-Type": "application/json"}
        )
        data = response.json()
        if "roadmap" in data:
            print(f"Roadmap nodes: {len(data['roadmap']['nodes'])}")
            print(f"Roadmap edges: {len(data['roadmap']['edges'])}")
            print("Roadmap generation: PASSED\n")
            return True
        else:
            print(f"Roadmap generation: FAILED - {data}\n")
            return False
    except Exception as e:
        print(f"Roadmap generation: FAILED - {e}\n")
        return False

def test_node_certs():
    print("Testing node certifications...")
    try:
        response = requests.post(
            f"{API_BASE}/node-certs",
            json={"node": "Python Basics"},
            headers={"Content-Type": "application/json"}
        )
        data = response.json()
        if "certifications" in data:
            print(f"Certifications found: {len(data['certifications'])}")
            print("Node certifications: PASSED\n")
            return True
        else:
            print(f"Node certifications: FAILED - {data}\n")
            return False
    except Exception as e:
        print(f"Node certifications: FAILED - {e}\n")
        return False

def main():
    print("="*50)
    print("SkillPath Backend Test Suite")
    print("="*50)
    print("\nMake sure the backend is running on http://localhost:5000\n")

    results = []

    results.append(("Health Check", test_health()))
    results.append(("Skills Endpoint", test_skills()))
    results.append(("Roadmap Generation", test_generate_roadmap()))
    results.append(("Node Certifications", test_node_certs()))

    print("="*50)
    print("Test Results Summary")
    print("="*50)

    for test_name, passed in results:
        status = "PASSED" if passed else "FAILED"
        print(f"{test_name}: {status}")

    total_passed = sum(1 for _, passed in results if passed)
    total_tests = len(results)

    print(f"\nTotal: {total_passed}/{total_tests} tests passed")

    if total_passed == total_tests:
        print("\nAll tests passed! Backend is working correctly.")
    else:
        print("\nSome tests failed. Please check the backend configuration.")

if __name__ == "__main__":
    main()
