public class Day3
{
	public static void Part1()
	{
		string[] triangles = File.ReadAllText("./03/input.txt").Trim().Split("\n");
		int count = 0;
		foreach (string line in triangles)
		{
			int[] t = line.Trim().Split().Where(x => !string.IsNullOrEmpty(x)).Select(Int32.Parse).ToArray();
			if (t[0] + t[1] > t[2] && t[0] + t[2] > t[1] && t[1] + t[2] > t[0]) count++;
		}
		Console.WriteLine(count);
	}
}
