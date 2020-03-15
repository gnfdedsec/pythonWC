import datetime
tDate = datetime.datetime.now()
thdate = ["อาทิตย์", "จันทร์", "อังคาร","พุธ", "พฤหัสบดี","ศุกร์","เสาร์"]
thmonth =["","ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."]
thdatearr = int(tDate.strftime("%w"))
thmontharr = int(tDate.strftime("%m"))
tDate.strftime("%d")
tyear = int(tDate.strftime("%Y"))+543
THD = 'วัน '+thdate[thdatearr]
THDAY= 'ที่ '+tDate.strftime("%d")
TM = 'เดื่อน '+thmonth[thmontharr]
TY='ปี '+str(tyear)
print(THD+THDAY+TM+TY)

