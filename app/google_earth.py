import ee

def main():
    # Trigger the authentication flow.
    ee.Authenticate(auth_mode='gcloud')

    # Initialize the library.
    ee.Initialize()

if __name__=="__main__":
    main()