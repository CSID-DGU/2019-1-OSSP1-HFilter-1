using Android.Content;
using Android.Views;
using Android.Widget;
using System.Collections.Generic;
using System.Linq;

namespace HFilter
{
    class SelectListView : BaseAdapter
    {
        List<string> total;
        LayoutInflater inflater;

        public SelectListView(Context context)
        {
            inflater = (LayoutInflater)context.GetSystemService(Context.LayoutInflaterService);
            total = new List<string>();
            total=Module.total.ToList();
        }

        public override int Count {
            get
            {
                if (total == null)
                    return 0;

                return total.Count;
            }
        }

        public override Java.Lang.Object GetItem(int position)
        {
            Java.Util.ArrayList totalJList = new Java.Util.ArrayList();

            totalJList.Add(total[position]);

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

            listObject.largeText.Text = total[position];

            return convertView;
        }

        // add to list
        public void Add(string info)
        {
            total.Add(info);
            NotifyDataSetChanged();
        }

        // remove to list
        public void Remove(int position)
        {
            total.RemoveAt(position);
            NotifyDataSetChanged();
        }
    }
}