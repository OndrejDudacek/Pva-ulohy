using System.Globalization;

class Program1
{    
    static void Main(string[] args)
    {
        System.Console.Clear();

        System.Console.WriteLine("Enter number of players: ");

        int numberOfPlayers = int.Parse(System.Console.ReadLine());
        if (numberOfPlayers < 2)
        {
            System.Console.WriteLine("Minimální počet hráčů je 2!");
            return;
        } 
        else if (numberOfPlayers > 5)
        {
            System.Console.WriteLine("Maximální počet hráčů je 5!");
            return;
        }

        Game game = new();
        game.AddPlayers(numberOfPlayers);

        while (true)
        {
            game.Move();
            if (game.Move() == 1) break;
        }
    }
}

class Player
{
    public string name;
    public int score;
    public Player(string name, int score)
    {
        this.name = name;
        this.score = 0;
    }
    public void UpdateScore(int points)
    {
        score += points;
    }
    public int[] ThrowDices(Dice dice1, Dice dice2)
    {
        dice1.Roll();
        dice2.Roll();
        return new int[] { dice1.value, dice2.value };
    }
}

class Dice
{
    public int value;
    public Dice()
    {
        value = 0;
    }
    public void Roll()
    {
        Random rnd = new();
        value = rnd.Next(1, 7);
    }
}

class Game
{
    public List<Player> players;
    public Dice dice1;
    public Dice dice2;
    public int winningScore;
    public Game()
    {
        dice1 = new Dice();
        dice2 = new Dice();
    }
    public void AddPlayers(int numberOfPlayers){
        winningScore = 100;
        players = new();

        for (int i = 0; i < numberOfPlayers; i++)
        {
            System.Console.WriteLine("Enter player name: ");
            string name = System.Console.ReadLine();
            players.Add(new Player(name, 0));
        }
        System.Console.Clear();
    }
    string WinChecker()
    {
        foreach (Player player in players)
        {
            if (player.score >= winningScore)
            {
                return player.name;
            }
        }
        return "";
    }
    public int Move(){
        foreach (Player player in players)
        {
            System.Console.WriteLine($"{player.name} je na řadě");
            System.Console.WriteLine("Stiskni klávesu pro hod kostkami:");
            System.Console.ReadKey();
            int[] turnScore = player.ThrowDices(dice1, dice2);
            System.Console.WriteLine($"Kostka 1: {turnScore[0]}");
            System.Console.WriteLine($"Kostka 2: {turnScore[1]}");
            if (turnScore[0] == 1 && turnScore[1] == 1)
            {
                System.Console.WriteLine("Hodil jsi 1 na obou kostkách, ztrácíš všechny body.");
                player.score = 0;
            }
            else if (turnScore[0] == 1 || turnScore[1] == 1)
            {
                System.Console.WriteLine("Hodil jsi 1 na jedné z kostek, ztrácíš body z tohoto tahu.");
            } 
            else {
                player.UpdateScore(turnScore[0] + turnScore[1]);
            }
            System.Console.WriteLine($"{player.name} skóre: {player.score}");
            string winner = WinChecker();
            if (winner != "")
            {
                System.Console.WriteLine("--------------------");
                System.Console.WriteLine($"{winner} VYHRÁVÁ!");
                return 1;
            }
            System.Console.WriteLine("--------------------");
        }
        return 0;
    }
}