try:
    Tiles = int(input('Number of tiles :'))
    TilesPerRow = int(input('Tiles per row  :')) #comments
    Color = input('Color :')
except:
    print("please input Number")
    Tiles = int(input('Number of tiles :'))
    TilesPerRow = int(input('Tiles per row  :'))
    Color = input('Color :')

TileColor = {'Red':100, 'Gold':140,'Green':80}

TotalRow = Tiles// TilesPerRow

RemainingTiles = Tiles % TilesPerRow


print(TotalRow,RemainingTiles)

MustBuy = TilesPerRow - RemainingTiles

print(f"you have to buy {MustBuy} tiles")
print(f"Total Cost {RemainingTiles*TileColor[Color]} THB")

#--------------------------------------
#
#Tiles = 14567
#TilesPerRow = 7 #comments
#MustBuy = TilesPerRow - RemainingTiles

#print(MustBuy)

#print(f"you will have to buy {MustBuy} tiles")
#









