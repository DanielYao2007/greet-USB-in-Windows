import os
def plate_exist(List_test):
     have_plate = []
     for plates in List_test:
          if os.path.exists(plates):
               have_plate.append(plates)
     return have_plate

def whether_in(List1,List2):       #list1:电脑原有的盘，list2:测试存在的盘
     not_in = []
     for a in List2:
          if a not in List1:
               not_in.append(a)
     return not_in

def USB_exist(former_plates = ['C:','D:'] ,text_plates = ['C:','D:','E:','F:']):
     have_plates = plate_exist(text_plates)
     new = whether_in(former_plates,have_plates)
     return new
