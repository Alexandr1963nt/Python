
konfet = 50
print(f"Вначале конфет всего {konfet}")
player1 = konfet % 11
print(f"Игрок1 взял {player1}")
player2 = 0
konfet = konfet - player1

while konfet > 0 :
{
    Console.WriteLine($"Игрок2 {player2 = new Random().Next(1, 11)}")
    Console.WriteLine($"Конфет {konfet = konfet - player2}")
    player1 = konfet % 11
    Console.WriteLine($"Игрок1 {player1}")
    konfet = konfet - player1
}

Console.WriteLine(konfet)
Console.WriteLine(player1)