# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:35:28 2023

@author: C-117
"""
import tkinter as tk
import math  
  
def rakam_bas(rakam):
      btn_1.insert(tk.END, rakam)
  
def islem_bas(islem):
      btn_1.insert(tk.END," "+ islem+ " ")
      
def hesap():
      alınan_ifade = btn_1.get()
      try:
          sonuc = eval(alınan_ifade)
          
          btn_1.delete(0, tk.END)
          
          btn_1.insert(0, sonuc)
      except:
          btn_1.delete(0, tk.END)
          btn_1.insert(0, "hata")
    
    
    
def hafıza_kayit():
    global hafıza 
    hafıza = btn_1.get()
   
        
def hafıza_artır():
    global hafıza
    try:
        hafıza= str(float(hafıza)  -  float(btn_1.get()))
    except:
        hafıza= "HATA"
 
    
 
    
 
def hafıza_azalt():
    global hafıza
    try:
        hafıza= str(float(hafıza)  -  float(btn_1.get()))
    except:
        hafıza= "HATA"
     
 
def hafıza_oku():
    btn_1.delete(0, tk.END)
    btn_1.insert(0,hafıza)
    
    
def temizle():
    btn_1.delete(0, tk.END)
    
    
    
    
    
pencere=  tk.Tk()
pencere.title("HESAP MAKİNESİ")   
 
 
btn_1 = tk.Entry(pencere, width=55)
btn_1.grid(row=0, column=0 , columnspan=4)   
 
rakamlar=("0123456789")
 
row, col = 1, 0 
 
for rakam in rakamlar :
     tk.Button(pencere,  text=rakam, width=10, command=lambda rakam=rakam: rakam_bas(rakam)).grid(row=row, column=col)
     col += 1
     if col > 2:
         col = 0
         row +=1
         
         


tk.Button(pencere, text=".", width=5, command=lambda: rakam_bas(".")).grid(row=4, column=1)
tk.Button(pencere, text="=", width=5, command=hesap).grid(row=4, column=2)         
tk.Button(pencere, text="+", width=5, command=lambda: rakam_bas("+")).grid(row=1, column=3)  
tk.Button(pencere, text="-", width=5, command=lambda: rakam_bas("-")).grid(row=2, column=3)
tk.Button(pencere, text="*", width=5, command=lambda: rakam_bas("*")).grid(row=3, column=3)  
tk.Button(pencere, text="/", width=5, command=lambda: rakam_bas("/")).grid(row=4, column=3)
   
hafıza = ""
tk.Button(pencere, text="mc", width=5, command=temizle).grid(row=6, column=0)
tk.Button(pencere, text="m+", width=5, command=hafıza_artır).grid(row=6, column=1)  
tk.Button(pencere, text="m-", width=5, command=hafıza_azalt).grid(row=6, column=2)  
tk.Button(pencere, text="mr", width=5, command=hafıza_oku).grid(row=6, column=3)  
tk.Button(pencere, text="c", width=5, command=temizle).grid(row=6, column=4)  
    
pencere.mainloop()
  
    
    
    
    
    
    
    
    
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
  
  
 