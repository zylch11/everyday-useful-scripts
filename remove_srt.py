import os

# Insert parent directory here, it will recursively search through the sub directories
# as well
rootdir = 'D:\Courses\Real-World Ethical Hacking Hands-on Cybersecurity'
print(rootdir)

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith('.srt'):
            try:
                os.remove(filepath)
                print(filepath + ' removed.')
            except:
                print('Error in deletion of file')
