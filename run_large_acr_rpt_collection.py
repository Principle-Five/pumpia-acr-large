# command line "python -m nuitka .\run_large_acr_rpt_collection.py"

# tk-inter is needed for tkinter to work with nuitka
# nuitka documentation suggests it is not explicitly needed/found automatically but this is wrong
# (possibly due to inclusion of matplotlib)

# nuitka-project: --enable-plugin=tk-inter
# nuitka-project: --mode=onefile
# nuitka-project: --user-package-configuration-file=dicoms.nuitka-package.config.yml

from pumpia_acr_large.large_acr_rpt_collection import LargeACRrptCollection

LargeACRrptCollection.run()
