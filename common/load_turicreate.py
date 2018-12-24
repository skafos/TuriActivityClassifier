from subprocess import check_output
import sys
import os


def try_install(timeout):
    print(f"\n Trying to install TuriCreate with timeout: {timeout} seconds")
    try:
        # try installing, give it 3 mins to try and install 
        output = check_output(["pip", "install", "turicreate==5.1"], timeout=timeout)
    except:
        print("Timeout install for turicreate")
        
    try:
        # load turicreate directly from site-packages (avoid restart kernel)
        if not os.path.exists(".local/site-packages/"):
            os.makedirs(".local/site-packages/")
        sys.path.append(".local/site-packages/")
        import turicreate as tc
        tc.SFrame() # check to see that we can load an empty SFrame
        print("Turi Create is now installed. Reference tc from here on out.")
        return tc
    except Exception as e:
        raise e
        return False
        



def install_turicreate(timeout=300, retries = 2):
    # check to see if it is already loaded and good to go
    try:
        import turicreate as tc
        tc.SFrame() # check to see that we can load an empty SFrame
        print("Turi Create was already installed. It's been saved to the tc variable.")
        return tc
    # if that fails, install it
    except:
        print("Turi Create was not installed, installing now.")
        for r in range(retries):
            try:
                tc = try_install(timeout)
                return tc
            except:
                timeout = timeout*2
        
        print("\n Was unable to install TuriCreate")
