using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Views.Animations;
using Android.Widget;

namespace HFilter
{

    [Activity(Label = "@string/app_name", Theme = "@style/MyTheme.NoTitle", NoHistory =true)]
    class SelectActivity:Activity
    {
        Button endBtn;
        ListView selectLV;
        Alert alert;
        SelectListView selectListView;
        System.Security.Cryptography.SHA256 sHA256;

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            // select layout
            SetContentView(Resource.Layout.activity_select);
        
            alert = new Alert(this);
            if (init() != 0)
            {
                alert.show("Error", "init failed");
            }
        }

        private int init()
        {
            Module.weights = new float[Module.weightLen];

            //View view = LayoutInflater.Inflate(Resource.Layout.activity_select, null);
            endBtn = FindViewById<Button>(Resource.Id.endBtn);
            endBtn.Click += endBtn_Click;
            endBtn.Enabled = false;

            selectLV = FindViewById<ListView>(Resource.Id.selectLV);
            
            selectListView = new SelectListView(this);
            selectLV.Adapter = selectListView;
            selectLV.ItemClick += SelectLV_ItemClick;

            sHA256 = System.Security.Cryptography.SHA256.Create();
            
            return 0;
        }

        private void SelectLV_ItemClick(object sender, AdapterView.ItemClickEventArgs e)
        {
            var item = (Java.Util.ArrayList)selectLV.Adapter.GetItem(e.Position);

            // get item name
            string key = item.ToString();
            // return [text]
            key = key.Substring(1, key.Length - 2);

            // hash
            byte[] keyB = Encoding.UTF8.GetBytes(key);
            string keyH = BitConverter.ToString(sHA256.ComputeHash(keyB)).Replace("-", string.Empty);
            float[] tmp;
            bool err = Module.module.TryGetValue(keyH, out tmp);
            if (!err) return;
            for (int i= 0; i<tmp.Length; i++)
            {
                Module.weights[i] += tmp[i];
            }

            //Animation anim = AnimationUtils.LoadAnimation(ApplicationContext, Resource.Animation.abc_fade_in);
            //e.View.Animation = anim;
            //selectLV.StartAnimation(anim);
            selectListView.Remove(e.Position);

            endBtn.Enabled = true;
            //Toast debug = Toast.MakeText(this, key+tmp, ToastLength.Long);
            //debug.Show();
        }

        private void endBtn_Click(object sender, EventArgs e)
        {
            string result = string.Empty;
            for(int i=0; i<Module.weightLen; i++)
            {
                result += Module.weights[i].ToString() + "\n";
            }

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