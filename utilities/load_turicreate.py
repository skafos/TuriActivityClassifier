"""Module to help ensure that turicreate is installed correctly."""
import os
import sys
from subprocess import check_output


def _try_install(timeout):
    try:
        # try installing, give it 3 mins to try and install 
        output = check_output(["pip", "install", "turicreate==5.1"], timeout=timeout)
    except:
        print("Timeout install for turicreate", flush=True)
        
    try:
        # load turicreate directly from site-packages (avoid restart kernel)
        if not os.path.exists(".local/site-packages/"):
            os.makedirs(".local/site-packages/")
        sys.path.append(".local/site-packages/")
        import turicreate as tc
        tc.SFrame() # check to see that we can load an empty SFrame
        print("Turi Create is now installed. Reference tc from here on out.", flush=True)
        return tc
    except Exception as e:
        raise e

def install_turicreate(timeout=300, retries=2):
    """Check to see if turicreate has been installed, and handle as needed.
    :param timeout: int, number of seconds to allow for the installation to occur.
    :param retries: int, number of times to retry the installation, each extending the timeout length by 2.
    :return: a turicreate object if installation was successful
    """
    # check to see if it is already loaded and good to go
    try:
        import turicreate as tc
        tc.SFrame() # check to see that we can load an empty SFrame
        print("Turi Create was already installed. It's been saved to the tc variable.", flush=True)
        return tc
    # if that fails, install it
    except:
        print(f"Turi Create was not installed, installing now with timeout: {timeout} seconds.", flush=True)
        for r in range(retries):
            try:
                tc = _try_install(timeout)
                return tc
            except:
                timeout = timeout*2
        
        print(f"\n Was unable to install TuriCreate after {retries} attempts", flush=True)
