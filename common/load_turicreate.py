def install_turicreate():
    # check to see if it is already loaded and good to go
    try:
        import turicreate as tc
        tc.SFrame() # check to see that we can load an empty SFrame
        print("Turi Create was already installed. It's been saved to the tc variable.")
        return tc
    # if that fails, install it
    except:
        print("Turi Create was not installed, installing now.")
        from subprocess import check_output
        import sys
        try:
            # try installing, give it 3 mins to try and install 
            output = check_output(["pip", "install", "turicreate==5.1"], timeout=180)
        except:
            print("Timeout install for turicreate")
        
        try:
            # load turicreate directly from site-packages (avoid restart kernel)
            sys.path.append("./local/site-packages/")
            import turicreate as tc
            tc.SFrame() # check to see that we can load an empty SFrame
            print("Turi Create is now installed. Reference tc from here on out.")
            return tc
        except:
            print("Unable to install and load turicreate, please go to terminal and run pip install turicreate")

