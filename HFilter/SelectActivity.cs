using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;

namespace HFilter
{

    [Activity(Label = "@string/app_name", Theme = "@style/MyTheme.NoTitle")]
    class SelectActivity:Activity
    {
        Button endBtn;
        ListView selectLV;
        Alert alert;
        SelectListView selectListView;

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            SetContentView(Resource.Layout.activity_select);
        
            alert = new Alert(this);
            if (init() != 0)
            {
                alert.show("Error", "init failed");
            }
        }

        private int init()
        {
            Module.weight = 0;

            //View view = LayoutInflater.Inflate(Resource.Layout.activity_select, null);
            endBtn = FindViewById<Button>(Resource.Id.endBtn);
            endBtn.Click += endBtn_Click;
            endBtn.Enabled = false;

            selectLV = FindViewById<ListView>(Resource.Id.selectLV);
            
            selectListView = new SelectListView(this);
            selectLV.Adapter = selectListView;
            selectLV.ItemClick += SelectLV_ItemClick;

            return 0;
        }

        private void SelectLV_ItemClick(object sender, AdapterView.ItemClickEventArgs e)
        {
            var item = (Java.Util.ArrayList)selectLV.Adapter.GetItem(e.Position);

            float tmp= 0;
            string key = item.ToString();
            key = key.Substring(1, key.Length - 2);
            Module.modules[0].TryGetValue(key, out tmp);
            Module.weight += tmp;

            selectListView.Remove(e.Position);

            endBtn.Enabled = true;
            //Toast debug = Toast.MakeText(this, key+tmp, ToastLength.Long);
            //debug.Show();
        }

        private void endBtn_Click(object sender, EventArgs e)
        {
            string result;
            if (Module.weight > 0)
                result = "male!";
            else
                result = "not male!";

            string[] okButton = new string[1];
            okButton[0] = "ok";
            EventHandler<DialogClickEventArgs>[] end = new EventHandler<DialogClickEventArgs>[1];
            end[0]= delegate
            {
                Finish();
            };
            alert.show("you are...", result, okButton, end);
        }
    }
}