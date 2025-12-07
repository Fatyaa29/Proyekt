#PROYEKT

import tkinter as tk
from tkinter import messagebox

user_data = {}

def register_page():
    rg= tk.Toplevel(root)
    rg.title("Qeydiyyat")
    rg.geometry("300x350")

    tk.Label(rg,text="Istifadeci adi:").pack(pady=5)
    ent_user=tk.Entry(rg)
    ent_user.pack()

    tk.Label(rg,text="Password:").pack(pady=5)
    ent_pass = tk.Entry(rg,show="*")
    ent_pass.pack()

    tk.Label(rg,text="Yas:").pack(pady=5)
    ent_age=tk.Entry(rg)
    ent_age.pack()

    tk.Label(rg,text="Nomre:").pack(pady=5)
    ent_number=tk.Entry(rg)
    ent_number.pack()

    tk.Label(rg, text="Xesteliyi:").pack(pady=5)
    ent_illness=tk.Entry(rg)
    ent_illness.pack()

    def register():
        username=ent_user.get()
        password=ent_pass.get()
        yas=ent_age.get()
        nomre=ent_number.get()
        xestelik=ent_illness.get()

        if not username or not password:
            messagebox.showerror("Xəta", "İstifadəçi adı və şifrə boş ola bilməz!")
            return

        if username in user_data:
            messagebox.showerror("Xəta", "Bu istifadəçi artıq mövcuddur!")
            return

        if not nomre.isdigit() or not yas.isdigit():
            messagebox.showerror("Xeta", "Yas ve Nomre yalniz reqem ola biler")
            return


        user_data[username] = {
            "username": username,
            "password":password,
            "yas":yas,
            "nomre":nomre,
            "xestelik":xestelik,

        }


        messagebox.showinfo("OK", "Qeydiyyat tamamlandı!")
        rg.destroy()

    tk.Button(rg, text="Qeydiyyat", bg="#4CAF50", fg="white", command=register).pack(pady=20)


def open_profile(username):
        prof = tk.Toplevel(root)
        prof.title("Profil")
        prof.geometry("300x380")


        user = user_data[username]


        tk.Label(prof, text=f"Profil:{username}",font=("Arial", 14, "bold")).pack(pady=10)


        tk.Label(prof,text="Ad:").pack()
        ent_name = tk.Entry(prof)
        ent_name.insert(0, user["username"])
        ent_name.pack()


        tk.Label(prof,text="Yaş:").pack()
        ent_age=tk.Entry(prof)
        ent_age.insert(0,user["yas"])
        ent_age.pack()


        tk.Label(prof,text="Nomre:").pack()
        ent_number=tk.Entry(prof)
        ent_number.insert(0,user["nomre"])
        ent_number.pack()

        tk.Label(prof,text="Xestelik:").pack()
        ent_illness=tk.Entry(prof)
        ent_illness.insert(0, user["xestelik"])
        ent_illness.pack()

        def change_password_window(username):

            change = tk.Toplevel(root)
            change.title("Şifrə dəyiş")
            change.geometry("300x230")

            tk.Label(change, text="Köhnə şifrə:").pack(pady=5)
            old_pass = tk.Entry(change, show="*")
            old_pass.pack()

            tk.Label(change, text="Yeni şifrə:").pack(pady=5)
            new_pass = tk.Entry(change, show="*")
            new_pass.pack()

            tk.Label(change, text="Yeni şifrə (təkrar):").pack(pady=5)
            new_pass2 = tk.Entry(change, show="*")
            new_pass2.pack()

            def change_pass():

                if old_pass.get() != user_data[username]["password"]:
                    messagebox.showerror("Xəta", "Köhnə şifrə yanlışdır!")
                    return

                if new_pass.get() != new_pass2.get():
                    messagebox.showerror("Xəta", "Yeni şifrələr uyğun gəlmir!")
                    return

                user_data[username]["password"] = new_pass.get()
                messagebox.showinfo("OK", "Şifrə uğurla dəyişdirildi!")
                change.destroy()

            tk.Button(change, text="Təsdiqlə", bg="#4CAF50", fg="white", command=change_pass).pack(pady=15)




        def update_info():
            user["ad"]=ent_name.get()
            user["yas"]=ent_age.get()
            user["nomre"]=ent_number.get()
            user["xestelik"]=ent_illness.get()
            messagebox.showinfo("OK", "Məlumat yeniləndi!")


        def delete_account():
            if messagebox.askyesno("Təsdiq","Hesabı silmək istədiyinizə əminsiniz?"):
                del user_data[username]
                messagebox.showinfo("OK", "Hesab silindi!")
                prof.destroy()


        tk.Button(prof, text="Yenilə", bg="pink", fg="white",command=update_info).pack(pady=10)


        tk.Button(prof, text="Hesabı Sil", bg="lightblue", fg="white", command=delete_account).pack(pady=10)


        tk.Button(prof, text="Şifrəni Dəyiş", bg="gold", fg="white",command=lambda: change_password_window(username)).pack(pady=10)


def open_admin_panel():
    admin_change=tk.Toplevel(root)
    admin_change.title("Admin Panel")
    admin_change.geometry("300x600")
    tk.Label(admin_change,text="Admin Paneli").pack(pady=10)

    listbox=tk.Listbox(admin_change,width=30)
    listbox.pack(pady=10)

    for username in user_data:
        listbox.insert(tk.END,username)

    tk.Label(admin_change,text="Ad").pack(pady=5)
    ent_name=tk.Entry(admin_change)
    ent_name.pack()

    tk.Label(admin_change, text="Yas").pack(pady=5)
    ent_age = tk.Entry(admin_change)
    ent_age.pack()

    tk.Label(admin_change, text="Nomre").pack(pady=5)
    ent_number = tk.Entry(admin_change)
    ent_number.pack()

    tk.Label(admin_change, text="Xestelik").pack(pady=5)
    ent_illness = tk.Entry(admin_change)
    ent_illness.pack()

    tk.Label(admin_change, text="Yeni sifre").pack(pady=5)
    ent_new_password= tk.Entry(admin_change,show="*")
    ent_new_password.pack()


    def select_user(event):
        selected=listbox.curselection()
        if selected:
            username=listbox.get(selected[0])

            user=user_data[username]

            ent_name.delete(0,tk.END)
            ent_name.insert(0,user["username"])

            ent_age.delete(0, tk.END)
            ent_age.insert(0, user["yas"])

            ent_number.delete(0, tk.END)
            ent_number.insert(0, user["nomre"])

            ent_illness.delete(0, tk.END)
            ent_illness.insert(0, user["xestelik"])

    listbox.bind("<<ListboxSelect>>",select_user)

    def update_user():
        selected = listbox.curselection()
        if selected:
            username = listbox.get(selected[0])

            user = user_data[username]
            user["ad"]=ent_name.get()
            user["yas"] = ent_age.get()
            user["nomre"] = ent_number.get()
            user["xestelik"] = ent_illness.get()

            messagebox.showinfo("ok",f"{username} melumat yenilendi")
    def change_user_pass():
        selected=listbox.curselection()
        if selected:
            username=listbox.get(selected[0])
            new_pass=ent_new_password.get()

            if len(new_pass)<4:
                messagebox.showerror("Xeta","sifre 4 simvoldan az ola bilmez")
                return

            user_data[username]["password"]=new_pass
            messagebox.showinfo("ok",f"{username} sifre yenilendi")

    def delete():
        selected=listbox.curselection()
        if selected:
            username=listbox.get(selected[0])
            if messagebox.askyesno("Tesdiq","Hesabi silmek isteyir"):
                del user_data[username]
                listbox.delete(selected[0])

                ent_name.delete(0,tk.END)
                ent_age.delete(0, tk.END)
                ent_number.delete(0, tk.END)
                ent_illness.delete(0, tk.END)
                messagebox.showinfo("ok","hesab silindi")

    tk.Button(admin_change, text="Yenilə", bg="pink", fg="white",
              command=update_user).pack(pady=10)


    tk.Button(admin_change, text="Hesabı Sil", bg="lightblue", fg="white",
              command=delete).pack(pady=10)


    tk.Button(admin_change, text="Şifrəni Dəyiş", bg="gold", fg="white",
              command=change_user_pass).pack(pady=10)


def login():
    username = ent_user.get()
    password = ent_pass.get()
    if username=="admin" and password=="admin":
        open_admin_panel()


    elif username in user_data and user_data[username]["password"] == password:
        open_profile(username)
    else:
        messagebox.showerror("Xəta", "İstifadəçi adı və ya şifrə yanlışdır!")


root=tk.Tk()
root.title("Login Sistemi")
root.geometry("300x300")
tk.Label(root,text="Istifadeci adi").pack(pady=5)
ent_user=tk.Entry(root)
ent_user.pack(pady=5)
tk.Label(root,text="Password").pack(pady=5)
ent_pass=tk.Entry(root,show="*")
ent_pass.pack(pady=5)

tk.Button(root,text="Daxil ol",bg="pink",fg="white",command=login).pack(pady=10)
tk.Button(root,text="Qeydiyyatdan kec",bg="pink",fg="white",command=register_page).pack(pady=10)


root.mainloop()


















