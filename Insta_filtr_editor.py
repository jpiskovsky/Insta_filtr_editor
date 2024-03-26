from PIL import Image
import time

def filtr1(obrazek):
    sirka, vyska = obrazek.size
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x,y))
            R = int(min((0.393 * r) + (0.769 * g) + (0.189 * b), 255))
            G = int(min((0.349 * r) + (0.686 * g) + (0.168 * b), 255))
            B = int(min((0.272 * r) + (0.534 * g) + (0.131 * b), 255))
            obrazek.putpixel((x,y), (R, G, B))
    obrazek.show()

def filtr2(obrazek):
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            if r+g+b > 500:  
                obrazek.putpixel((x,y), (255-r, 255-g, 255-b))
            y += 1
        x += 1
    obrazek.show()

def filtr3(obrazek):
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            if prumer > 150:
                obrazek.putpixel((x,y), (r*2, g*2, b*2))  
            else:
                obrazek.putpixel((x,y), (r//2, g//2, b//2))  
            y += 1
        x += 1
    obrazek.show()
    

def main():
    
    print()
    print("Právě se nacházíš v editoru fotek pro tvůj Instagram.")
    time.sleep(3)
    
    while True: 
        
        try:
        
            print()
            fotka = Image.open(input("Zadejte název souboru fotky (i s příponou): "))
        
        except FileNotFoundError:
            print()
            print("Soubor fotky nebyl nalezen.")
            time.sleep(2)
            
            print()
            print("Zadejte název souboru fotky správně nebo nejprve fotku nahrajte.")
            time.sleep(2)
            continue
        
        print()
        filtr = input("Zvolte filtr, který chcete použít (sepie, sileny nebo syty): ")
        
        while filtr not in ["sepie", "sileny", "syty"]:
            
            print()
            print("Něco se pokazilo")
            time.sleep(2)
            
            print()
            filtr = input("Zvolte znovu správný filtr, který chcete použít (sepie, sileny nebo syty): ")
        
        if filtr == "sepie":
            filtr1(fotka)
        
        elif filtr == "sileny":
            filtr2(fotka)
        
        elif filtr == "syty":
            filtr3(fotka)
        
        print()
        pokracovat = input("Chcete upravit další fotku nebo použít jiný filtr? (ano/ne): ")
        if pokracovat.lower() != "ano":
            break
            
if __name__ == "__main__":
    main()
    
    
    