public class Day3
{
	public static void Part1()
	{
		string[] triangles = File.ReadAllText("./03/input.txt").Split("\n");
		int count = 0;
		foreach (string line in triangles)
		{
			if (string.IsNullOrEmpty(line)) continue;
			string[] t = line.Trim().Split().Where(x => !string.IsNullOrEmpty(x)).ToArray();
			if (Int32.Parse(t[0]) + Int32.Parse(t[1]) > Int32.Parse(t[2]) && Int32.Parse(t[0]) + Int32.Parse(t[2]) > Int32.Parse(t[1]) && Int32.Parse(t[1]) + Int32.Parse(t[2]) > Int32.Parse(t[0])) count++;
		}
		Console.WriteLine(count);
	}
}
