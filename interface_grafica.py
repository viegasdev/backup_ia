# Importar o módulo tkinter
import tkinter

# Criar janela
window = tkinter.Tk()

# Dar título à janela
window.title('GUI')

# Adicionar um objeto com texto à janela
label = tkinter.Label(window, text = 'Hello world!').pack()

# Manter a janela aberta com o mainloop
window.mainloop()
