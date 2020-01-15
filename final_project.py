#!/home/guyru/anaconda3/bin/python
# -*-coding:Utf-8-*

#voir documentation tkinter:  https://web.archive.org/web/20190524140835/https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#https://pillow.readthedocs.io/en/stable/index.html
import tkinter as tk #pour l'interface graphique
import os #pour la gestion des chemins
from tkinter import scrolledtext as stext 
from tkinter import filedialog as FD
from tkinter import StringVar
import PIL
from PIL import ImageFile, ImageTk, Image




class Application(): #début fenêtre principale
      def __init__(self): #que mettre en paramètre?
           #pourquoi?
            self.master = tk.Frame()
            self.master.pack(fill=tk.BOTH, expand=1)
            self.frame=tk.Frame(master = self.master)
            self.frame.pack(fill = tk.BOTH, expand=1)
            self.label=tk.Label(master= self.master, text="final project", font=16)
            self.label.pack(side=tk.TOP, fill = tk.X)
            self.zone_affichage_texte = tk.Scrollbar(master =self.master)
            self.zone_affichage_texte.pack(side = tk.LEFT, fill = tk.Y, expand = 1 )
          
#fin elements fenêtre principale

#debut element fenêtres secondaires contenant le canvas et les boutons 
            self.fenetre_canvas = tk.Frame (master = self.frame)
            self.fenetre_canvas.pack(side = tk.RIGHT, fill = tk.BOTH)

            self.fenetre_boutons = tk.Frame (master = self.frame)
            self.fenetre_boutons.pack(side = tk.LEFT, fill = tk.BOTH)
            
            self.fenetre_etiquettes = tk.Frame (master = self.fenetre_boutons)
            self.fenetre_etiquettes.pack(side = tk.TOP, fill = tk.BOTH)
            
            self.label_etiquettes=tk.Label(master = self.fenetre_etiquettes, text="chemins d'étiquette", font=16)
            self.label_etiquettes.pack(side=tk.TOP, fill = tk.X)
            
            self.liste_label= tk.Listbox(master = self.fenetre_etiquettes)
            self.demande_labels()
            self.liste_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)  

            self.fenetre_image = tk.Frame (master = self.fenetre_boutons)
            self.fenetre_image.pack(side = tk.BOTTOM, fill = tk.BOTH)
            
            self.liste_image= tk.Listbox(master = self.fenetre_image)
            self.liste_image.pack(side=tk.TOP, fill=tk.BOTH, expand=1)   
            self.btn_ouvrir = tk.Button (master = self.fenetre_image, text = "ouvrir", command =self.charger_image)
            self.btn_ouvrir.pack(side = tk.TOP, fill=tk.BOTH, expand=1)       
    
            self.btn_charger = tk.Button (master = self.fenetre_image, text = "charger l'image", command =self.afficher_image)
            self.btn_charger.pack(side = tk.TOP, fill=tk.BOTH, expand=1) 
            
            #fin declaration boutons

#déclaration de la fonction permettant de lire le label#trouver affichage liste
      def demande_labels(self):
            with open (chemin, "r", encoding = "utf-8", newline = "\n") as fd:
              t = fd.read()
              t_liste = t.split("\n")
              self.liste_label.insert(tk.END, t_liste)
            return(t_liste)
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
            self.image = tk.Canvas(self.fenetre_canvas, width = 100, height = 100)  
            self.scbar = tk.Scrollbar(master = self.image)
            canvas_image = Image.open(self.absname)
            file_image = PIL.ImageTk.PhotoImage(canvas_image)
            self.image.create_image(260, 260, image = file_image, anchor = 'nw')
            self.image.pack(fill=tk.BOTH, expand=1)
            return

            
   

#déclaration fonction d'extraction du fichier 
    


#ouverture et fermeture de la fenetre
if __name__=="__main__":
   chemin = input("entrer un chemin d'étiquette")
   root = tk.Tk()
   app = Application()#création d'un objet prenant en paramètres master
   root.mainloop()


#demande du chemin de label 
 
       
            
  
           
     



 



