import os, shutil

root_directory = "/root"
subdirectory = "workspace/static-site-generator"

def copy_static_files():
    public_directory = os.path.join(root_directory, subdirectory, 'public')
    static_directory = os.path.join(root_directory, subdirectory, 'static')

    # if (os.path.exists(public_directory)):
    #     shutil.rmtree(public_directory)
        
    # os.mkdir(public_directory)

    copy_files(static_directory)


def copy_files(current_path):
    directories = os.listdir(current_path)
    
    for directory in directories:
        path = os.path.join(current_path, directory)
        if (not os.path.isfile(path)):
            copy_files(path)
        else:
            print(directory)
