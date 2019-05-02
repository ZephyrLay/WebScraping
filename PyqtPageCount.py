from bs4 import BeautifulSoup
import xlwt
import requests
import sys
import string
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
import os
import csv


class MainPage(QDialog):

    linkState = ""
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('linkCount.ui',self)
        self.btnSearch.clicked.connect(self.searchText)
        self.btnExportExcel.clicked.connect(self.exportExcel)

    def searchText(self):
      searchLink = self.txtSearch.toPlainText()
      linkState = searchLink
      url =""
      
      #check the url is valid or not
      if linkState.startswith(("http://" , "https://")):
        if not linkState[-1] == '/':
          linkState = linkState.replace(" ","")
          url = linkState + '/'
        else:
          url = linkState.replace(" ","")
          url = linkState.replace(" ","")
          # Getting the webpage, creating a Response object.
        response = requests.get(url)

        # Extracting the source code of the page.
        data = response.text

        # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
        soup = BeautifulSoup(data, 'lxml')

        # Extracting all the <a> tags into a list.
        tags = soup.find_all('a')

        # Extracting URLs from the attribute href in the <a> tags.
        # for tag in tags:
        # print(tag.get('href'))

        # Checking Duplicate
        seen = set()
        result = []
        subStr = ""
        for item in tags:
          strTempOri = item.get('href')
          if(strTempOri):
            strTemp = strTempOri.replace(" ","")
            if strTemp[-1] == '/':
              subStr = strTemp[:-1]
              if subStr not in seen:
                  seen.add(subStr)
                  result.append(subStr)
            else:
              if item.get('href') not in seen:
                  seen.add(item.get('href'))
                  result.append(item.get('href'))

        #noDupList = list(removeDuplicate(tags)):

        # for idx, val in enumerate(tags):
        #print("index is %d and value is %s" % (idx, val.get('href')))
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setColumnWidth(0, 650)
       
        # Specifying column
        for row , rowData in enumerate(result):
          if rowData:
              if row == 1:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(url))
              #test link start with #
              if not rowData.startswith(("#")):
                conStr = rowData[-4:]
                #check link start with '/' or input URL
                if rowData.startswith(("/", url)):
                  if rowData.startswith(("/")):
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(rowData))
                  elif rowData.startswith((url)):
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(rowData))
                  else:
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(rowData))
                #check link end with 'html' or didn't start with 'http' or 'www'
                if conStr == "html" and not rowData.startswith(("http", "www")):
                  if rowData.startswith(("/")):
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(rowData))
                  else:
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(rowData))

        #this is to delete the Empty Row
        for row in reversed(range(self.tableWidget.rowCount())):
          widget = self.tableWidget.item(row, 0)
          print(widget)
          if widget is None:
            self.tableWidget.removeRow(row)
      else:
        self.lblError.setText('Your Link must start with "http://" or "https://" ')

#this is to Export Excel
    def exportExcel(self):
      path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
      if path[0] != '':
        with open(path[0], 'w', newline='') as csv_file:
          writer = csv.writer(csv_file, dialect='excel')
          for row in range(self.tableWidget.rowCount()):
            row_data = []
            for column in range(self.tableWidget.columnCount()):
              item = self.tableWidget.item(row, column)
              if item is not None:
                row_data.append(item.text())
              else:
                row_data.append('')
            writer.writerow(row_data) 

      QtWidgets.QMessageBox.information(self, "Saving CSV File", "Exporting CSV is SUCCESSFUL!")
      for row in reversed(range(self.tableWidget.rowCount())):
        self.tableWidget.removeRow(row)
      self.txtSearch.setText("")
  


      '''
          workbook = xlwt.Workbook()
      sheet = workbook.add_sheet("Scraping Link")
      # Specifying style
      style = xlwt.easyxf('font: bold 1;align: horiz left;protection: cell_locked false;')
      for row in range(self.tableWidget.rowCount()):
        filterResults = self.tableWidget.item(row,0).text()
      if(filterResults):
        for idx , data in enumerate(filterResults):
          sheet.write(idx, 0, data, style)
          row += 1
      print("here in there")

      #creating the excel file
      #path = QFileDialog.getSaveFileName(self, 'Save Excel' , os.getenv('HOME') , 'EXCEL(*.xlsx)')
      workbook.save("drupal.xls")
      QtWidgets.QMessageBox.information(self, "Saving Excel File", "Exporting Excel is SUCCESSFUL!")
      '''

'''
#get the argument from command line
if(len(sys.argv) == 2 ):
  linkState = sys.argv[1]
else:
  print('You need to type Only link address start with "http" or "www" ')
  exit()

url = ""
#check the url is valid or not
if linkState.startswith(("http://" , "https://")):
  if linkState.startswith(("www")):
    #Remove space from Input URL
    url = 'http://' + linkState.replace(" ","")
  else:
    #Remove space from Input URL
    url = linkState.replace(" ","")
else:
  print ('Caught ValueError Exception')
  print ('Type the Correct Link Address Again Please')
  print ('Your Link must start with "http://" or "wwww"')
  exit()

if not url[-1] == '/':
  url = url +'/'
print(url)


# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')

# Extracting all the <a> tags into a list.
tags = soup.find_all('a')

# Extracting URLs from the attribute href in the <a> tags.
# for tag in tags:
# print(tag.get('href'))

# Checking Duplicate
seen = set()
result = []
subStr = ""
for item in tags:
  strTempOri = item.get('href')
  if(strTempOri):
    strTemp = strTempOri.replace(" ","")
    if strTemp[-1] == '/':
      subStr = strTemp[:-1]
      if subStr not in seen:
          seen.add(subStr)
          result.append(subStr)
    else:
      if item.get('href') not in seen:
          seen.add(item.get('href'))
          result.append(item.get('href'))

#noDupList = list(removeDuplicate(tags)):



# for idx, val in enumerate(tags):
#print("index is %d and value is %s" % (idx, val.get('href')))

workbook = xlwt.Workbook()

sheet = workbook.add_sheet("Testing")
# Specifying style
style = xlwt.easyxf('font: bold 1;align: horiz left;protection: cell_locked false;')

# Specifying column
row = 0
col = 0
if row == 0:
      sheet.write(row, col, "Links Address", style)
      row += 1
for idx, val in enumerate(result):
  if row == 1:
      sheet.write(row, col, url, style)
      row += 1
  # you can put ANY CUSTOM validation in startswith("")
  if(val):
    #test link start with #
    if not val.startswith(("#")):
      conStr = val[-4:]
      #check link start with '/' or input URL
      if val.startswith(("/", url)):
        if val.startswith(("/")):
          sheet.write(row, col, url + val[1:], style)
          row += 1
        elif val.startswith((url)):
          sheet.write(row, col, val, style)
          row += 1
        else:
          sheet.write(row, col, val , style)
          row += 1
      #check link end with 'html' or didn't start with 'http' or 'www'
      if conStr == "html" and not val.startswith(("http", "www")):
        if val.startswith(("/")):
          sheet.write(row, col, url + val[1:], style)
          row += 1
        else:
          sheet.write(row, col, url + val, style)
          row += 1

#creating the excel file
workbook.save("drupal.xls")
'''

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())