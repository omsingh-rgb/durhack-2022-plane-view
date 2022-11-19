import ee
import private
def main():
    # Trigger the authentication flow.
    ee.Authenticate(auth_mode="notebook")

    # Initialize the library.
    ee.Initialize()

if __name__=="__main__":
    main()