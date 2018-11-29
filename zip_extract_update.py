import os, zipfile
import re
import shutil
import glob


particular_file_extract_dst = "C:/Users/rpedda/Desktop/ListingMetricsFile"
path_of_extraction = "C:/Users/rpedda/Desktop/Extracted_Files/"
network_path = "//paz02dsd956/awsbis3_dropbox_dev/HistoricalData_DoNotDelete/ListHub_Historical/"
copy_dst = "C:/Users/rpedda/Desktop/Copied_Files_From_network_path"
zipfiles = os.listdir(network_path)


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            print("Creating a directory in local machine to copy the .zip files")
            os.makedirs(directory)
            print("Directory Successfully")
    except OSError:
        print('Error: Creating directory. ' +  directory)

def unzip():
    files = []
    for filename in zipfiles:
        if filename.endswith(".zip"):
            print("Copying the zip file - {0} from network path to local folder".format(filename))
            shutil.copy(network_path+'/{0}'.format(filename), copy_dst)
            print("Preparing to Extract Zip Files")
            name = os.path.splitext(os.path.basename(filename))[0]
            if not os.path.isdir(name):
                try:
                    file = "C:/Users/rpedda/Desktop/Copied_Files_From_network_path/{0}".format(filename)
                    createFolder(directory="C:/Users/rpedda/Desktop/Extracted_Files")
                    print("Unzipping the File = ", file)
                    zip_ref = zipfile.ZipFile(file, 'r')
                    zip_ref.extractall(path_of_extraction)
                    zip_ref.close()
                    os.remove(file)
                except Exception as e:
                    print("Exception", e)
                    print("BAD ZIP: "+filename)

        for filename in os.listdir(path_of_extraction):
            if re.search(r'RDC_ListingMetrics', filename):
                print("Desired File - {0} found, moving to new folder for uploading to s3".format(filename))
                files.append(filename)
                for f in files:
                    src = 'C:/Users/rpedda/Desktop/Extracted_Files/{0}'.format(f)
                    shutil.copy(src, particular_file_extract_dst)
                    print("Copied Specified file to new folder")
                    files = []
                    os.remove(src)

    print("Removing the created directory")
    shutil.rmtree("C:/Users/rpedda/Desktop/Extracted_Files")


if __name__ == "__main__":
    unzip()
    print("Completed")





