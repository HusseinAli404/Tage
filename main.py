
                prey=y
            if(prevy-y>=10 or y-prevy>=10):
                print(mytext)
                Label(root,text=mytext,font=('Times',15,'bold')).pack()
                mytext=""
            mytext = mytext + text[11]+" "
            prevy=y
    Label(root,text=mytext,font=('Times',15,'bold')).pack()

def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda: extract(path),bg="#2f2f77",fg="gray",pady=15,padx=15,font=('Times',15,'bold'))
    extractBtn.pack()

def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        pass  

uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()

root.mainloop()
