import os

os.system("jupyter nbconvert --to html notebooks/UNICEF_Assessment.ipynb "
          "--output outputs/report.html")

