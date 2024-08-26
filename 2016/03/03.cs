public class Day3
{
	static string[] triangles = File.ReadAllText("./03/input.txt").Trim().Split("\n");
	// static string[] triangles = File.ReadAllText("./03/test-input.txt").Trim().Split("\n");
	static int count = 0;

	public static void Part1()
	{
		foreach (string line in triangles)
		{
			int[] t = line.Trim().Split().Where(x => !string.IsNullOrEmpty(x)).Select(Int32.Parse).ToArray();
			if (t[0] + t[1] > t[2] && t[0] + t[2] > t[1] && t[1] + t[2] > t[0]) count++;
		}
		Console.WriteLine(count);
	}

	public static void Part2()
	{
		List<int> row0 = new List<int>();
		List<int> row1 = new List<int>();
		List<int> row2 = new List<int>();

		for (int row = 0; row < triangles.Count(); row++)
		{
			int[] t = triangles[row].Trim().Split().Where(x => !string.IsNullOrEmpty(x)).Select(Int32.Parse).ToArray();
			row0.Add(t[0]);
			row1.Add(t[1]);
			row2.Add(t[2]);
			if (row2.Count() == 3)
			{
				if (row0[0] + row0[1] > row0[2] && row0[0] + row0[2] > row0[1] && row0[1] + row0[2] > row0[0]) count++;
				if (row1[0] + row1[1] > row1[2] && row1[0] + row1[2] > row1[1] && row1[1] + row1[2] > row1[0]) count++;
				if (row2[0] + row2[1] > row2[2] && row2[0] + row2[2] > row2[1] && row2[1] + row2[2] > row2[0]) count++;
				row0.Clear();
				row1.Clear();
				row2.Clear();
			}
		}
		Console.WriteLine(count);
	}
}
