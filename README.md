# TensorFlowTutorial

## About

These are companion scripts, modules, and packages from going through sentdex's Machine Learning (ML)
playlist on Youtube. Applicable links may be found in the **Acknowledgement** section below.

For organizational purposes, all of the *extra* files used during this series (i.e. - ```.pickle```, ```.data```, 
```.names```, and ```.xls``` files) have been placed in ```/TensorFlowTutorial/etc/``` and the code adjusted as such. In these cases,
the code here will not be identical to that found on [pythonprogramming.net](https:\\www.pythonprogramming.net). The only
exception to this being the *NLTK* downloads used towards the beginning of the TensorFlow section as they are larger than
I wish to upload to Github.

**NOTE:** This project is titled TensorFlowTutorial because its original intention was to simply cover sentdex's tutorials
dealing with the tensorflow library alone, but after further examination it appeared prudent to cover the entirety of the
ML playlist.

##### Note converning requirements:
In the original Sentdex tutorial series, he uses the TensorFlow-gpu package. Due to the hardware that is being run locally
while going through this tutorial, I found it worked better for myself if I used the TensorFlow compiled for the CPU and my GPU
was still using Cuda 2.0, not the 3.0 needed for TensorFlow, so there will be slight dicrepencies throughout the TensorFlow section of this
series.

### Sections
These sections correspond to the parts of TensorFlowTutorial and not directly to the parts on [pythonprogramming.net](https:\\www.pythonprogramming.net),
although it should be similar. This will also be updated as I go along the series to include the finished sections of TensorFlowTutorial. 

##### Parts
1. Linear Regression: 2-12
2. K Nearest Neighbor (KNN): 14-18
3. Support Vector Machine (SVM): 20-28 
4. Clustering: 34 - 42
    1. K Means: 34 - 38
    2. Mean Shift: 39 - 42
5. Neural Networks: 44 - ...


## Author

**Thomas Kyle Robertson** - *Creator* - [Github](https://github.com/roberttk01) [LinkedIn](https://www.linkedin.com/in/thomas-robertson-3530743b/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements
* These scripts were **not** originally created by myself. They were created along with watching sentdex's videos.
    * [sentdex's Youtube Channel](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ)
    * [sentdex's Machine Learning playlist](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v)
    * [PythonProgramming.net](https://pythonprogramming.net/)
* Breast Cancer Datasets donated to University of California Irvine (UCI) by University of Wisconsin-Madison
    * [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
    * [Breast Cancer Dataset Index Page](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29)
    * [breast-cancer-wisconsin.data](https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data)
    * [breast-cancer-wisconsin.names](https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.names)