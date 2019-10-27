# From Raw Recruit Scripts to Perfect Python (in 90 minutes)

[PyData NYC 2019 Tutorial](https://pydata.org/nyc2019/schedule/presentation/14/from-raw-recruit-scripts-to-perfect-python-in-90-minutes/)

[Stanley van der Merwe](https://pydata.org/nyc2019/speaker/profile/153/stanley-van-der-merwe), [Petr Wolf](https://pydata.org/nyc2019/speaker/profile/119/petr-wolf)

Audience level: Novice

## Setup instructions

To follow the tutorial, you will need a python environment with Jupyter Notebook and several python libraries.

You can either install those on your computer or use an on-line Notebook environment via [Binder](https://mybinder.org/).

### Option 1: on-line environment (Binder)

Open the following link

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PetrWolf/pydata_nyc_2019/master?filepath=Tutorial.ipynb)

### Option 2: local installation (conda)

#### Prerequisites
* install [Git](https://git-scm.com/downloads)
* install [Anaconda Distribution](https://www.anaconda.com/distribution) (for Python 3)

#### Steps
1. clone [this repository](https://github.com/PetrWolf/pydata_nyc_2019) in Git
    ```
    git clone https://github.com/PetrWolf/pydata_nyc_2019
    ```
2. create a Conda environment at a desired location (`<DIR>`)
    ```
    conda create -p <DIR> python=3.6 --file=requirements.txt
    ```
3. activate the environment
    ```
    conda activate <DIR> 
    ```
4. launch Jupyter Notebook
    ```
    jupyter notebook
    ```

### Option 3: local installation (venv)

#### Prerequisites
* install [Git](https://git-scm.com/downloads)
* install [python](https://www.python.org/downloads/) (3.6 or newer) 
* download [pip](https://pip.pypa.io/en/stable/installing/)

#### Steps

1. clone [this repository](https://github.com/PetrWolf/pydata_nyc_2019) in Git
    ```
    git clone https://github.com/PetrWolf/pydata_nyc_2019
    ```
2. create a python [virtual environment](https://docs.python.org/3/library/venv.html) in a desired location (`<DIR>`)
    ```
    python -m venv <DIR>
    ```
3. activate the environment
    * `source <DIR>/bin/activate` (on Linux or Mac)
    * `<DIR>\Scripts\activate.bat` (on Windows)

4. install all necessary packages via pip
    ```
    pip install -r requirements.txt
    ```
5. launch Jupyter Notebook
    ```
    jupyter notebook
    ```