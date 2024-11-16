print('Wie heißt du?')
Name = input()
print("Hello, " + Name)

print("Wie alt bist du?")
Alter = int(input()) 

if Alter > 18:
    print("Du bist erwachsen.")
elif 6 <= Alter <= 18:
    print("Du bist ein Teenager.")
else:
    print("Du bist ein Kind.")

print("Wo wohnst du?")
Wohnort = input()  

print("\nDanke für deine Antworten!")
print(f"Name: {Name}")
print(f"Alter: {Alter}")
print(f"Wohnort: {Wohnort}")
