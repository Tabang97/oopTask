from tkinter import *


inheritance = Tk()
inheritance.title("StudentNo:78120734678964")
inheritance.geometry("800x400")
inheritance.configure(background="Black")

# 1st label
label = Label(inheritance, text="SicknessCode", padx="10", pady="10")
label.grid(row=0, column=0)
txt_box1 = Entry(inheritance, width="30")
txt_box1.grid(row=0, column=1)

# 2n label
label2 = Label(inheritance, text="DurationOfTreatment",padx="10", pady="10")
label2.grid(row=1, column=0)
txt_box2 = Entry(inheritance,width="30")
txt_box2.grid(row=1, column=1)

#2.1 label
label2_1= Label(inheritance, text="Weeks/Months",padx="10", pady="10")
label2_1.grid(row=1, column=2)

#3rd label
label3=Label(inheritance, text="DoctersPracticeNumber", padx="10", pady="10")
label3.grid(row=2, column=0)
txt_box3 = Entry(inheritance, width="20")
txt_box3.grid(row=2, column=1)

#4th label
label4=Label(inheritance, text="Scan/ConsultationFee",padx="10", pady="10")
label4.grid(row=3, column=0)
txt_box4 = Entry(inheritance, width="30")
txt_box4.grid(row=3, column=1)

#5th label
treatment_amount = Label(text="AmountPaidForTreatment:", padx="10", pady="10")
treatment_amount.grid(row=12, column=0)
cons_treatment =Label(text="R900.00")
cons_treatment.grid(row=12,column=3)


#Radiobutton
choose = IntVar()
Radiobutton(inheritance,
text="Cancer",
padx = 20,
variable=choose,
value=1).grid(row=14,column=0)

#another Radiobutton
choose1 = IntVar()
Radiobutton(inheritance,
text="Influenza",
padx = 20,
variable=choose,
value=2).grid(row=16,column=0)

#creating class
class sick():
    pass
class cancer(sick):
    def treatment(self):
        if self.scanfee<600:
            print("We cannot treat you")
        else:
            self.answer = self.medication + self.scanfree
            print(self.answer)
p1 = cancer()
p1.medication = 400
p1.scanfree =int(input("enter scanfree amont"))
p1.treatment()

#Calculate function
def calc():
    pass
#Calculate button
calc_button = Button(inheritance, text="Calculate", bg="grey", command=calc)
calc_button.grid(row=18,column=0)

#clear function
def clear_function():
    txt_box1.delete(0,END)
    txt_box2.delete(0,END)
    txt_box3.delete(0, END)
    txt_box4.delete(0, END)

#clear button
clear_button = Button(inheritance, text="Clear", bg="grey", command=clear_function)
clear_button.grid(row=18,column=3)

inheritance.mainloop()
