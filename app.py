from google.cloud import compute_v1

def list_gcp_regions():
    client = compute_v1.RegionsClient()
    project = "NareshIT"  # Replace with your project ID

    request = compute_v1.ListRegionsRequest(project=project)
    response = client.list(request=request)

    print("Available Multi Cloud Regions:")
    for region in response:
        print(f"- {region.name} (Status: {region.status})")

if __name__ == "__main__":
    list_gcp_regions()
