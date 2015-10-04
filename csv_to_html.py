# convert csv to html table
# using pandas
import pandas as pd

def csv_to_html(csvfile):
    htmltxt = '<TABLE border="1">'
    csvtxt=pd.read_csv(csvfile)
    for idx,row in csvtxt.iterrows():
        htmltxt+='<TR>'+ ''.join('<TD>%s</TD>' % data for data in row)+ '</TR>'
    return htmltxt