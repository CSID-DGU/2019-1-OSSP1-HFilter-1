using Android.Content.Res;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

namespace HFilter
{
    static class Module
    {
        public static List<string> total;
        public static Dictionary<string, float>[] modules;
        public static float weight;
        public static AssetManager assets;

        // Read module
        public static async Task<int> ReadModule(string assetName, int moduleid)
        {
            using (StreamReader sr = new StreamReader(assets.Open(assetName)))
            {
                string line = await sr.ReadLineAsync();
                int ptr;

                while (line != null)
                {
                    line = line.Substring(0, line.Length - 1);
                    ptr = line.LastIndexOf(" ");
                    modules[moduleid][line.Substring(0, ptr)] = float.Parse(line.Substring(ptr + 1));
                    line = await sr.ReadLineAsync();
                }
            }

            return 0; // Task<TResult> returns an object of type TResult, in this case int
        }

        // Read total
        public static async Task<int> ReadTotal()
        {
            using (StreamReader sr = new StreamReader(assets.Open("totaldata.txt")))
            {
                string line = await sr.ReadLineAsync();
                int ptr;

                while (line != null)
                {
                    line = line.Substring(0, line.Length - 1);
                    ptr = line.LastIndexOf(" ");
                    total.Add(line.Substring(0, ptr));
                    line = await sr.ReadLineAsync();
                }
            }

            return 0;
        }
    }
}