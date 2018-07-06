from shutil import copy2
import glob 
import random 
import os

def getFileNameList(list_dir):
    return [os.path.basename(x) for x in list_dir]

def getRandomNumPics(dir,num=50):  
    # print(glob.glob("C:/Users/mhbt-/Desktop/kaistImageSet/DaySet/visible/*.jpg"))
    fileList = glob.glob(dir)
    #fileList = [os.path.basename(x) for x in glob.glob(dir)]
    randlist = random.sample(range(1, len(fileList)), num)
    
    res = [fileList[i] for i in randlist]
    print(res)
    # copy2("../sample_img/sample_computer.jpg", "./visible")

def getFileName(dir):
    for i in list(range(len(dir))[::-1]):         
        if(dir[i] == '.'):break
    print(dir[:i])        
    return dir[:i]


if __name__ =="__main__":
    random.seed(0)   
    # getRandomNumPics("C:/Users/mhbt-/Desktop/kaistImageSet/DaySet/visible/*.jpg")
    # getFileName("keker.png")
    ls = glob.glob("C:/Users/mhbt-/Desktop/kaistImageSet/set02/*")
    for i in ls:
        
        i+="/lwir/*.jpg"
        print(i)
        getRandomNumPics(i)