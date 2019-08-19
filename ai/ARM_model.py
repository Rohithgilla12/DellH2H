# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:53:35 2019

@author: Aadi
"""
import xlrd 

loc = (r"Dataset.xlsx") 

def detertype(price,gpu,resolution,processor,ram,weight,size):
    
    if gpu>=1050 and weight>=2.2:
        print ('Gamer')
        return 'Gamer'
    
    elif gpu<1050 and resolution>=2160 and ram>10:
        print ('Graphic Designer')
        return 'Graphic Designer'
    
    elif gpu>=1050 and processor>=7 and ram>=10:
        print ('Programmer')
        return 'Programmer'

    elif gpu==0 and ram<=4:
        print ('Personal User')
        return 'Personal User'

    elif price>=41000 and price<50000:
        print ('Office User')
        return 'Office User'

    else:
        print ('Type TBD')
        return 'Type TBD'

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

sheet.cell_value(0, 0) 
for i in range (1,sheet.nrows):
    detertype(sheet.row_values(i)[0],sheet.row_values(i)[1],sheet.row_values(i)[2],sheet.row_values(i)[3],sheet.row_values(i)[4],sheet.row_values(i)[5],sheet.row_values(i)[6])
    

    
