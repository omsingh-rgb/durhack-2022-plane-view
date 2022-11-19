import ee

def main():
    # Trigger the authentication flow.
    ee.Authenticate()

    # Initialize the library.
    ee.Initialize()

if __name__=="__main__":
    main()