using Android.Content.Res;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace HFilter
{
    static class Module
    {
        public static List<string> total;
        public static List<List<string>> nears;
        public static Dictionary<string, float[]>module;
        public static List<string> flavor;
        public static float[] weights;
        public static AssetManager assets;
        public static int weightLen;

        public static void Init(AssetManager asset)
        {
            module = new Dictionary<string, float[]>();
            total = new List<string>();
            nears = new List<List<string>>();
            flavor = new List<string>();
            assets = asset;
        }

        // Read module
        public static async Task<int> ReadModule()
        {
            using (StreamReader sr = new StreamReader(assets.Open("TotalHS.dat")))
            {
                string line = await sr.ReadLineAsync();
                int ptr;

                while (line != null)
                {
                    ptr = line.IndexOf(":");
                    string tmp = line.Substring(ptr + 1);
                    List<float> valList = new List<float>();
                    while (tmp.Length != 0)
                    {
                        int vPtr = tmp.IndexOf(" ");
                        float f;
                        float.TryParse(tmp.Substring(0, vPtr), out f);
                        valList.Add(f);
                        tmp = tmp.Substring(vPtr + 1);
                    }
                    float[] vals = valList.ToArray();

                    module[line.Substring(0, ptr)] = vals;
                    line = await sr.ReadLineAsync();
                }
            }

            weightLen=module.Values.ToArray()[0].Length;
            weights = new float[weightLen];

            return 0; // Task<TResult> returns an object of type TResult, in this case int
        }

        // Read Total
        public static async Task<int> ReadTotal()
        {
            using (StreamReader sr = new StreamReader(assets.Open("Total.dat")))
            {
                string line = await sr.ReadLineAsync();

                while (line != null)
                {
                    total.Add(line);
                    line = await sr.ReadLineAsync();
                }
            }

            return 0;
        }

        //Read Near
        public static async Task<int> ReadNear()
        {
            using (StreamReader sr = new StreamReader(assets.Open("Near.dat")))
            {
                string line = await sr.ReadLineAsync();

                while (line != null)
                {
                    List<string> tmp = new List<string>();
                    while (line != string.Empty)
                    {
                        int ptr = line.IndexOf('>');
                        tmp.Add(line.Substring(0, ptr));
                        line = line.Substring(ptr + 1);
                    }
                    nears.Add(tmp);

                    line = await sr.ReadLineAsync();
                }
            }

            return 0;
        }

        //Read flavor
        public static async Task<int> ReadFlavor()
        {
            using (StreamReader sr = new StreamReader(assets.Open("Flavor.dat")))
            {
                string line = await sr.ReadLineAsync();

                while (line != null)
                {
                    flavor.Add(line);

                    line = await sr.ReadLineAsync();
                }
            }

            return 0;
        }
    }
}