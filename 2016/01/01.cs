public class Day1
{
    class Coordinates
    {
        public static int x { get; set; }
        public static int y { get; set; }
    }

    static string[] directions = File.ReadAllText("./01/input.txt").Split(", ");
    static char facing = 'N';

    public static void Part1()
    {
        foreach (string direction in directions)
        {
            facing = newDirection(direction[0]);
            updateCoords(facing, int.Parse(direction.Substring(1)));
        }
        Console.WriteLine($"1.1: {Coordinates.x + Coordinates.y}");
    }

    static void updateCoords(char direction, int distance)
    {
        switch (direction)
        {
            case 'N':
                Coordinates.y += distance;
                break;
            case 'E':
                Coordinates.x += distance;
                break;
            case 'S':
                Coordinates.y -= distance;
                break;
            case 'W':
                Coordinates.x -= distance;
                break;
        }
    }

    static char newDirection(char turn)
    {
        if (turn == 'R')
        {
            switch (facing)
            {
                case 'N':
                    return 'E';
                case 'E':
                    return 'S';
                case 'S':
                    return 'W';
                case 'W':
                    return 'N';
            }
        }
        else
        {
            switch (facing)
            {
                case 'N':
                    return 'W';
                case 'E':
                    return 'N';
                case 'S':
                    return 'E';
                case 'W':
                    return 'S';
            }
        }
        return 'x';
    }

    public static void Part2()
    {
        List<int[]> visited = new List<int[]>();
        foreach (string direction in directions)
        {
            facing = newDirection(direction[0]);
            int distance = int.Parse(direction.Substring(1));
            for (int i = 0; i < distance; i++)
            {
                updateCoords(facing, 1);
                int[] current = { Coordinates.x, Coordinates.y };
                visited.Add(current);
            }
        }
    }
}
