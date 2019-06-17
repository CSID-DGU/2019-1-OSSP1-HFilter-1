using Android.App;
using Android.Content;
using Android.Content.Res;
using Android.OS;
using Android.Support.V7.App;
using Android.Widget;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace HFilter
{
    [Activity(Label = "@string/app_name", Theme = "@style/MyTheme.Main")]
    public class MainActivity : AppCompatActivity
    {
        Button button1;
        TextView title;
        TextView state;

        Alert alert;

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            
            // Set our view from the "main" layout resource
            SetContentView(Resource.Layout.activity_main);

            Android.App.AlertDialog.Builder alert = new Android.App.AlertDialog.Builder(this);
            if (Init() != 0)
            {
                alert.SetTitle("Error");
                alert.SetMessage("Error to initialize");
                alert.SetPositiveButton("Ok", (senderAlert, args) =>
                {
                    // null
                });
                Dialog dialog = alert.Create();
                dialog.Show();
            }

        }

        private int Init()
        {
            alert = new Alert(this);

            button1 = FindViewById<Button>(Resource.Id.button1);
            button1.Click += Button1_Click;
            button1.Text = "Filter!";

            title = FindViewById<TextView>(Resource.Id.titleTV);
            title.Visibility = Android.Views.ViewStates.Invisible;

            state = FindViewById<TextView>(Resource.Id.outputTV);
            state.Visibility = Android.Views.ViewStates.Invisible;
            state.Text = "init success\n";

            return 0;
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            state.Text += "select clicked\n";
            if (Module.module == null)
            {
                alert.show("Error", "module unloaded");
                FinishAffinity();
                return;
            }

            // make another activity
            Intent intent = new Intent(this, typeof(SelectActivity));

            // show
            StartActivity(intent);
            FindViewById<TextView>(Resource.Id.textView1).Text = "당신을 맞춰볼께요;)";
        }
    }
}

//var intent = new Intent(this, typeof(SelectPage));
//StartActivity(intent);


//relativeLayout1 = FindViewById<RelativeLayout>(Resource.Id.relativeLayout1);

//            LayoutTransition trans = new LayoutTransition();
//relativeLayout1.LayoutTransition = trans;

//LayoutInflater inflater = (LayoutInflater)BaseContext.GetSystemService(Context.LayoutInflaterService);
//View addView = inflater.Inflate(Resource.Layout.activity_select, null);
//Button sbutton1 = addView.FindViewById<Button>(Resource.Id.sbutton1);
//sbutton1.Click += delegate
//            {
//                ((RelativeLayout) addView.Parent).RemoveView(addView);
//            };

//            relativeLayout1.AddView(addView);