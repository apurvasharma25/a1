import xlwt
book=xlwt.Workbook()
w=book.add_sheet("sheet1")
w.write(0,0,"S.No")
w.write(0,1,"name")
w.write(0,2,"contact no")
w.write(0,3,"age")
w.write(0,4,"year")
w.write(0,5,"dob")
w.write(1,0,"1")
w.write(1,1,"apurva")
w.write(1,2,"9856734201")
w.write(1,3,"21")
w.write(1,4,"1996")
w.write(1,5,xlwt.Formula("d2+e2"))
a=book.add_sheet("sheet2")
a.write(0,0,"maths")
a.write(0,1,"science")
a.write(0,2,"s.s.t")
a.write(0,3,"total")
a.write(1,0,"78")
a.write(1,1,"87")
a.write(1,2,"77")
a.write(1,3,xlwt.Formula("a2+b2+c2"))
book.save("a.xls")