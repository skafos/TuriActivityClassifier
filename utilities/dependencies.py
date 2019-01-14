"""Module to help ensure that dependencies are installed correctly."""
import os
import sys
from subprocess import check_output


def _try_install(timeout, pkg):
    try:
        # try installing, give it 3 mins to try and install 
        output = check_output(["pip", "install", pkg], timeout=timeout)
    except:
        print(f"Timeout install for {pkg}", flush=True)
        
    try:
        # load pkg directly from site-packages (avoid restart kernel)
        if not os.path.exists(".local/site-packages/"):
            os.makedirs(".local/site-packages/")
        sys.path.append(".local/site-packages/")
    except Exception as e:
        raise e

def _install_turicreate(timeout=300, retries=2):
    """Check to see if turicreate and other deps have been installed, and handle as needed.
    :param timeout: int, number of seconds to allow for the installation to occur.
    :param retries: int, number of times to retry the installation, each extending the timeout length by 2.
    :return: True if successful
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
                _try_install(timeout, "turicreate==5.1")
                import turicreate as tc
                tc.SFrame() # check to see that we can load an empty SFrame
                print("Turi Create is now installed.", flush=True)
                return True
            except:
                timeout = timeout*2
        print(f"\n Was unable to install TuriCreate after {retries} attempts", flush=True)

def _install_s3fs(timeout=300, retries=2):
    """Check to see if s3fs has been installed, and handle as needed.
    :param timeout: int, number of seconds to allow for the installation to occur.
    :param retries: int, number of times to retry the installation, each extending the timeout length by 2.
    :return: True if successful
    """
    # check to see if it is already loaded and good to go
    try:
        from s3fs.core import S3FileSystem
        s3 = S3FileSystem(anon=True) # check to see that we can load an s3fs object
        print("s3fs was already installed.", flush=True)
    # if that fails, install it
    except:
        print(f"s3fs was not installed, installing now with timeout: {timeout} seconds.", flush=True)
        for r in range(retries):
            try:
                _try_install(timeout, "s3fs")
                from s3fs.core import S3FileSystem
                s3 = S3FileSystem(anon=True) # check to see that we can load an s3fs object
                print("s3fs is now installed.", flush=True)
                return True
            except:
                timeout = timeout*2
        print(f"\n Was unable to install s3fs after {retries} attempts", flush=True)
        
def install(timeout=300, retries=2):
    # Install both dependencies
    _install_turicreate(timeout, retries)
    _install_s3fs(timeout, retries)
    