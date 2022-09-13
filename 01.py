minha_string = input();

letras = "abcdefghijklmnopqrstuvwxyz0123456789"
flag = True;
for ch in minha_string.lower():
    if(ch not in letras):
        flag = False
if(flag): print("Legal")
else: print("Chata")