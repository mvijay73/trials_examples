import os
import sum
os.environ.setdefault('APP_SETTINGS_MODULE', 'sumapp.settings')
print("Value is " + str(sum.sum()))
