#!/home/guyru/anaconda3/bin/python
# -*-coding:Utf-8-*
from __future__ import unicode_literals

#voir documentation tkinter:  https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#https://pillow.readthedocs.io/en/stable/index.html
import tkinter as tk #pour l'interface graphique
import os #pour la gestion des chemins
from tkinter import scrolledtext as stext 
from tkinter import filedialog as FD
from tkinter import StringVar
import PIL
from PIL import ImageFile, ImageTk, Image
import json
import pdb
import tempfile





class Application(): #début fenêtre principale
      def __init__(self): #que mettre en paramètre?
           #pourquoi?
            self.master = tk.Frame()
            self.master.pack(fill=tk.BOTH, expand=1)
            self.frame=tk.Frame(master = self.master)
            self.frame.pack(fill = tk.BOTH, expand=1)
            self.label=tk.Label(master= self.master, text="final project", font=16)
            self.label.pack(side=tk.TOP, fill = tk.X)
           
          
#fin elements fenêtre principale

#debut element fenêtres secondaires contenant le canvas et les boutons 
            self.fenetre_canvas = tk.Frame (master = self.frame)
            self.fenetre_canvas.pack(side = tk.RIGHT, fill = tk.BOTH)
            
            
            
            self.image = tk.Canvas(master = self.fenetre_canvas, width=1200, height=800, scrollregion=(0, 0, 2400, 2000))
            self.image.grid(row=0, column=0)

            self.scrollY = tk.Scrollbar(master = self.fenetre_canvas, orient=tk.VERTICAL, command=self.image.yview)
            self.scrollY.grid(row=0, column=1, sticky=tk.N+tk.S)

            self.scrollX = tk.Scrollbar(master = self.fenetre_canvas, orient=tk.HORIZONTAL, command=self.image.xview)
            self.scrollX.grid(row=1, column=0, sticky=tk.E+tk.W)

            self.image['xscrollcommand'] = self.scrollX.set
            self.image['yscrollcommand'] = self.scrollY.set

            self.image.bind("<Button-1>", self.clique_gauche)
            self.image.bind("<Button1-Motion>", self.select_plage)
    
            
          

            

            self.fenetre_boutons = tk.Frame (master = self.frame)
            self.fenetre_boutons.pack(side = tk.LEFT, fill = tk.BOTH)
            
            self.fenetre_etiquettes = tk.Frame (master = self.fenetre_boutons)
            self.fenetre_etiquettes.pack(side = tk.TOP, fill = tk.BOTH)
            
            self.label_etiquettes=tk.Label(master = self.fenetre_etiquettes, text="chemins d'étiquette", font=16)
            self.label_etiquettes.pack(side=tk.TOP, fill = tk.X)
            self.bouton_sauvegarder =tk.Button(master = self.fenetre_etiquettes, text = "sauvegarder les coordonnées", command =self.coord_fichier_label)
            self.bouton_sauvegarder.pack(side = tk.TOP, fill=tk.BOTH, expand=1)
            
            self.liste_label= tk.Listbox(master = self.fenetre_etiquettes)
            self.liste_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1) 
            with open (chemin, "r", encoding = "utf-8", newline = "\n") as fd:
              t = fd.read()
              t_split = t.splitlines(1)
              for element in t_split:
                self.liste_label.insert(tk.END,element) 

            self.fenetre_image = tk.Frame (master = self.fenetre_boutons)
            self.fenetre_image.pack(side = tk.BOTTOM, fill = tk.BOTH)
            
            self.liste_image= tk.Listbox(master = self.fenetre_image)
            self.liste_image.pack(side=tk.TOP, fill=tk.BOTH, expand=1)   
            self.btn_ouvrir = tk.Button (master = self.fenetre_image, text = "ouvrir", command =self.charger_image)
            self.btn_ouvrir.pack(side = tk.TOP, fill=tk.BOTH, expand=1)       
    
            self.btn_charger = tk.Button (master = self.fenetre_image, text = "charger l'image", command =self.afficher_image)
            self.btn_charger.pack(side = tk.TOP, fill=tk.BOTH, expand=1) 
            self.label_etiquettes=tk.Label(master = self.fenetre_image, text="chemins d'image", font=16)
            self.label_etiquettes.pack(side=tk.TOP, fill = tk.X)

            
            #fin declaration boutons

#déclaration de la fonction permettant de lire le label#trouver affichage liste
            
#fonction permettant au bouton "charger" d'importer l'image dans la listbox

      def charger_image(self):
         self.chemins = FD.askopenfilenames() #sort un chemin absolu
         print (self.chemins)
         if not self.chemins:
             return
         self.chemins_image = list(self.chemins)
         self.liste_image.delete(0, tk.END)
         for self.chemin in self.chemins_image:
            self.name = os.path.basename(self.chemin)
            self.dirname = os.path.dirname(self.chemin)
            self.absname = os.path.join(self.dirname, self.name)
            self.liste_image.insert(tk.END, self.name)

            #fonction pour afficher l'image provenant de la listbox dans le canevas
      
      def afficher_image(self) :
            canvas_image = Image.open(self.absname)
            file_image = PIL.ImageTk.PhotoImage(canvas_image,size= 2)
            self.file_image= file_image
            self.image.create_image((0,0), image = file_image, anchor = 'nw')
            return

              #fonctions de selection d'une plage de l'image 
      def clique_gauche(self, event):
            self.currObject = None
            self.x1, self.y1 = event.x, event.y 

      def select_plage(self, event):
            self.x2, self.y2 = event.x, event.y
            self.position = list()
            self.rect_liste =list()
            if self.x1 < self.x2:
                self.position.append(self.x1)
                if self.y1 < self.y2:
                  self.position.append(self.y1)
                  self.position.append(self.x2)
                  self.position.append(self.y2)
                else :
                  self.position.append(self.y2)
                  self.position.append(self.x2)
                  self.position.append(self.y1)
            else :
                  self.position.append(self.x2)
                  if self.y1 < self.y2 :
                   self.position.append(self.y1)
                   self.position.append(self.x1)
                   self.position.append(self.y2)
                  else :
                   self.position.append(self.y2)
                   self.position.append(self.x1)
                   self.position.append(self.y1) 
                    
            try :
             self.image.delete(self.rectangle)
             self.rectangle = self.image.create_rectangle(self.position[0], self.position[1],\
                                                  self.position[2], self.position[3], \
                                                  outline='red', width=2)
            except :
             self.rectangle = self.image.create_rectangle(self.position[0], self.position[1],\
                                                  self.position[2], self.position[3], \
                                                  outline='red', width=2)
            self.image.focus(self.rectangle)




      def coord_fichier_label(self) :
      #   #commande pour créer un fichier contenant les coordonnées associées au label choisi.
        selection_label = self.liste_label.curselection()
        indice_de_selection_label = selection_label[0]
        name_label = self.liste_label.get(indice_de_selection_label)
        fichier_json = FD.asksaveasfilename() 
        coord = json.dumps([name_label, (self.position[0], self.position[1],self.position[2], self.position[3])])
        with open (fichier_json, 'w') as fd : 
             fd.write (coord) 
        return



#déclaration fonction d'extraction du fichier 
    


#ouverture et fermeture de la fenetre
if __name__=="__main__":
   chemin = input("entrer un chemin d'étiquette")
   root = tk.Tk()
   app = Application()#création d'un objet prenant en paramètres master
   root.mainloop()


#demande du chemin de label 
 
       
            
  
           
     



 



