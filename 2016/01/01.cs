public class Day1
{
    struct coordinates
    {
        public static int x { get; set; }
        public static int y { get; set; }
    }

    static string[] directions = File.ReadAllText("./01/input.txt").Split(", ");
    static char facing = 'N';

    public static int Part1()
    {
        foreach (string direction in directions)
        {
            facing = newDirection(direction[0]);
            updateCoords(facing, int.Parse(direction.Substring(1)));
        }
        return coordinates.x + coordinates.y;
    }

    static void updateCoords(char direction, int distance)
    {
        switch (direction)
        {
            case 'N':
                coordinates.y += distance;
                break;
            case 'E':
                coordinates.x += distance;
                break;
            case 'S':
                coordinates.y -= distance;
                break;
            case 'W':
                coordinates.x -= distance;
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
}
