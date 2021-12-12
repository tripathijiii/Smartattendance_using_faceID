import os
import face_biometric_recognition
import cv2
from .excelupdation import updateexcel
def facerecognition(name,roll):
    known=[]
    try:
        for files in os.listdir("/Users/shashwateshtripathi/Desktop/SE/SE/Face/studentface/{}".format(name.upper())):
            if files =='.DS_Store':
                continue
            file_path=f"/Users/shashwateshtripathi/Desktop/SE/SE/Face/studentface/{name.upper()}/{files}"
            known_image=face_biometric_recognition.load_image_file(file_path)
            known.append(face_biometric_recognition.face_encodings(known_image)[0])
        image = cv2.imread("/Users/shashwateshtripathi/Desktop/SE/SE/media/imgofstud/{}_{}.jpeg".format(name,roll))
        image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        image=cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
        cv2.imwrite("/Users/shashwateshtripathi/Desktop/SE/SE/media/imgofstud/{}_{}.jpeg".format(name,roll),image)
        print(156789)
        unknown_image=face_biometric_recognition.load_image_file("/Users/shashwateshtripathi/Desktop/SE/SE/media/imgofstud/{}_{}.jpeg".format(name,roll))
        try:
            unknown_encoding=face_biometric_recognition.face_encodings(unknown_image)[0]
            for i in known:
                result=face_biometric_recognition.compare_faces([i],unknown_encoding)
                if result[0]==True:
                    os.remove("/Users/shashwateshtripathi/Desktop/SE/SE/media/imgofstud/{}_{}.jpeg".format(name,roll))
                    print(54)
                    percentage=updateexcel(name)
                    return {'name':name,'percentage':percentage}
        except:
            print(44)
            os.remove("/Users/shashwateshtripathi/Desktop/SE/SE/media/imgofstud/{}_{}.jpeg".format(name,roll))
            return {}
        os.remove("/Users/shashwateshtripathi/Desktop/SE/SE/media/imgofstud/{}_{}.jpeg".format(name,roll))
        return {}
    except:
        print(55)
        os.remove("/Users/shashwateshtripathi/Desktop/SE/SE/media/imgofstud/{}_{}.jpeg".format(name,roll))
        return {} 

