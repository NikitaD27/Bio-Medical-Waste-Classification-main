# Bio-Medical-Waste-Classification
Python 3.8+
Libraries:
NumPy
Pandas
OpenCV
PyTorch
Matplotlib
Install the necessary libraries by running:

bash
Copy code
pip install -r requirements.txt  
Instructions
1. Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/username/project-name.git  
cd project-name  
2. Import Necessary Libraries
Ensure all required libraries are imported into your Python environment. The requirements.txt file contains all dependencies.

3. Execute the Main Script
Run the main script by entering the path to the best.py file:

bash
Copy code
python main.py  
Inside main.py, update the path to best.py as required.

4. Simultaneously Run Supporting File
Execute the additional script for classification:

Option 1: Run BMW.py (for script-based execution):
bash
Copy code
python BMW.py  
Option 2: Open and run BMW.ipynb in Jupyter Notebook for an interactive experience.
5. Test with Sample Input
To see the output, display a sample medical waste item, such as:

Empty medicine packets
A syringe
Other biomedical waste items
6. Observe Results
The classification results will display whether the waste is Hazardous or Non-Hazardous in real time.

File Structure
main.py: Main script to initiate the classification.
best.py: Pre-trained model file for YOLOv5.
BMW.py: Python script for executing the classification model.
BMW.ipynb: Notebook version for interactive execution.
