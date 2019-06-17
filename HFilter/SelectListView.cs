using Android.Content;
using Android.Views;
using Android.Widget;
using System;
using System.Collections.Generic;
using System.Linq;

namespace HFilter
{
    class SelectListView : BaseAdapter
    {
        List<string> total;
        List<string> viewLS;
        List<List<string>> nears;
        LayoutInflater inflater;
        Random random;

        public SelectListView(Context context)
        {
            inflater = (LayoutInflater)context.GetSystemService(Context.LayoutInflaterService);

            random = new Random((int)DateTime.Now.Ticks);
            total = Module.total.ToList();
            nears = Module.nears.ToList();
            viewLS = new List<string>();
            for(int i=0; i<nears.Count; i++)
            {
                //deep copy
                nears[i] = Module.nears[i].ToList();
            }
            for(int i=0; i<nears.Count; i++)
            {
                int k = random.Next(nears[i].Count);
                viewLS.Add(nears[i][k]);
                total.Remove(nears[i][k]);
                nears[i].RemoveAt(k);
            }

            // shuffle
            for(int n=0; n<viewLS.Count; n++)
            {
                int k = random.Next(viewLS.Count - n) + n;

                string tmp = viewLS[k];
                viewLS[k] = viewLS[n];
                viewLS[n] = tmp;

                List<string> lTmp = nears[k];
                nears[k] = nears[n];
                nears[n] = lTmp;
            }

        }

        public override int Count {
            get
            {
                if (viewLS == null)
                    return 0;

                return viewLS.Count;
            }
        }

        public override Java.Lang.Object GetItem(int position)
        {
            Java.Util.ArrayList totalJList = new Java.Util.ArrayList();

            totalJList.Add(viewLS[position]);

            return totalJList;
        }

        public override long GetItemId(int position)
        {
            return position;
        }

        public class ListObject : Java.Lang.Object
        {
            public TextView largeText;
            public TextView mediumText;
        }

        public override View GetView(int position, View convertView, ViewGroup parent)
        {
            ListObject listObject = null;

            // if scroll over the screen, convertView returns null
            if (convertView == null)
            {
                // so make a new View
                convertView = inflater.Inflate(Resource.Layout.ListLayout, parent, false);
                
                listObject = new ListObject();
                listObject.largeText = convertView.FindViewById<TextView>(Resource.Id.largeText);
                listObject.mediumText = convertView.FindViewById<TextView>(Resource.Id.mediumText);

                convertView.Tag = listObject;
            }
            else
            {
                listObject = (ListObject)convertView.Tag;
            }

            listObject.largeText.Text = viewLS[position];

            return convertView;
        }

        // add to list
        public void Add(string info)
        {
            viewLS.Add(info);
            NotifyDataSetChanged();
        }

        // add specific point
        public void Add(string info, int position)
        {
            viewLS.Insert(position, info);
            NotifyDataSetChanged();
        }

        // add near
        public void AddNear(int position)
        {
            int k = random.Next(nears[position].Count);
            Add(nears[position][k], position);
            total.Remove(nears[position][k]);

            // if near is not total
            if (nears[position].Count != total.Count)
            {
                nears[position].RemoveAt(k);
            }

            if (nears[position].Count == 0)
            {
                nears[position] = total;
            }
        }

        // remove to list
        public void Remove(int position)
        {
            viewLS.RemoveAt(position);
            NotifyDataSetChanged();
        }

        // change list
        public void Change(int position)
        {
            nears[position] = total;
        }
    }
}