#!/usr/bin/env python



import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from optparse import OptionParser














def student_id(s):
    df = pd.read_csv(r"data.csv")
    col_list1 = list(df["Student id"])
    if s in col_list1:
        rf = pd.DataFrame()
        rf = df[df['Student id'] == s]
        # rf
        rata = [rf['Marks'].sum()]
        # rata
        sata = ["Total Marks"]
        tf = pd.DataFrame(rata, sata)
        # tf
        student_title = "Student Details"

        html1 = f'''<html><!DOCTYPEhtml>
        <head>
              <title>{student_title}</title>
              </head>
              <body>
              <h1>Student Details</h1>
              <h2>{rf.to_html()}</h2>
              <h2>{tf.to_html()}</h2>
              </body></html>'''

        with open('result.html', 'w') as f:

            f.write(html1)
            f.close()
    else:
        error_title = "Wrong Inputs"

        html3 = f'''<html><!DOCTYPEhtml>
        <head>
              <title>{error_title}</title>
              </head>
              <body>
              <h1>{error_title}</h1>
              <h2>Something Went Wrong</h2>

              </body>





        </html>'''

        with open('result.html', 'w') as f:
            f.write(html3)
            f.close()
    exit()











def course_id(c):
    df = pd.read_csv(r"data.csv")

    col_list =  list(df["Course id"])
    if c in col_list:



        gf=pd.DataFrame()
        gf= df[df["Course id"] == c]
        #gf
        data = [[gf['Marks'].mean(), gf['Marks'].max()]]
        #data
        bf=pd.DataFrame(data,columns=['Average_marks', 'Maximum_marks'])
        #bf
        ax=gf.hist(column='Marks')
        fig = ax[0][0].get_figure()
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        course_title="Course Details"


        html2=f'''<html><!DOCTYPEhtml>
        <head>
              <title>{course_title}</title>
              </head>
              <body>
              <h1>{course_title}</h1>
              <h2>{bf.to_html()}</h2>
              <img src=\'data:image/png;base64,{encoded}\'>
              </body>
    
    
    
    
    
        </html>'''

        with open ('result.html','w') as f:
            f.write(html2)
            f.close()
    else:
        error_title="Wrong Inputs"


        html3=f'''<html><!DOCTYPEhtml>
        <head>
              <title>{error_title}</title>
              </head>
              <body>
              <h1>{error_title}</h1>
              <h2>Something Went Wrong</h2>
    
              </body>
    
    
    
    
    
        </html>'''

        with open ('result.html','w') as f:
            f.write(html3)
    exit()


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--student_id", dest="s",type="int",
                      help="Give student Id")
    parser.add_option("-c", "--course_id", dest="c",type="int",
                      help="Give Course Id")

    (options, args) = parser.parse_args()



    s=options.s
    c=options.c
    if options.s:
        student_id(s)

    if options.c:
        course_id(c)


    # course_id(c)
    # student_id(s)



