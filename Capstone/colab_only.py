'''
Codes here should be used in Colab environment only

1. Install requirements by pip
!pip install -q configobj
!pip install -q hyperas

2. Mount to Google Drive
from google.colab import drive
drive.mount('/content/gdrive')

3. Import files
from google.colab import files
src = list(files.upload().values())[0]
open('data.py','wb').write(src)
import data

src = list(files.upload().values())[0]
open('tor_lstm.py','wb').write(src)
import tor_lstm

src = list(files.upload().values())[0]
open('tor_sdae.py','wb').write(src)
import tor_sdae

src = list(files.upload().values())[0]
open('tor_cnn.py','wb').write(src)
import tor_cnn
'''