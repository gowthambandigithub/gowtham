'''The example of encryption we use by julius caseser.casesar needed the provied intruction to his general
 but he did'nt want his enemies to learn his plans the message slipped into there hands
 it provided no protection againt modren code breaking techniques.
 each letter the original message is shifted by 3 place
 Eg : A is become C,B is become D,Y is become B,Z is become c '''



message = input("enter any name: ")
shift = int(input("enter the shift value: "))

new_message = ""

for ch in message:
    if ch>="a" and ch<="z":
        pos=ord(ch)-ord("a")
        pos=(pos+shift)%26
        new_char=chr(pos + ord("a"))
        new_message=new_message + new_char
    elif ch>="A" and ch<="Z":
        pos=ord(ch)-ord("A")
        pos=(pos+shift)%26
        new_char=chr(pos+ord ("A"))
        new_message = new_message + ch
    print("the shifted message is",new_message)
        
