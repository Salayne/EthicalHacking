from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode('utf-8'))
        return True # Extraction successful

    except RuntimeError as e:
        if "Bad password" in str(e):
            return False # Extraction failed
        else:
            #Handle other potential RuntimeErrors, e.g corrupted zip file
            print(f"[-] Error: {e}")
            return False
    except Exception as e:
        print(f"[-] Unexpected error: {e}")
        return False

# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):
#     
#
#

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as file:
            # Write your logic here...
            # Iterate through password entries in rockyou.txt
            # >>>>> Process each line
            for line in file:
                password = line.strip().decode('utf-8') #>>>>> Remove leading/trailing whitespace.
                print(f"[+] Attempting password: {password}")

                # Attempt to extract the zip file using each password
                if attempt_extract(zf, password):

                     # Handle correct password extract versus incorrect password attempt)
                    print(f"[+] Password found: {password}")
                    return
                
                  #print("[+] Password not found in list")
                else:
                    print("[+] Password not found in the list")


            file.close()


if __name__ == "__main__":
    main()