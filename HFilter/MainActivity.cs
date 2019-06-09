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
    [Activity(Label = "@string/app_name", Theme = "@style/MyTheme.NoTitle")]
    public class MainActivity : AppCompatActivity
    {
        Button button1;
        Button button2;
        Button button3;
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
            Module.Init(Assets);

            button1 = FindViewById<Button>(Resource.Id.button1);
            button1.Click += Button1_Click;
            button1.Text = "select";
            button2 = FindViewById<Button>(Resource.Id.button2);
            button2.Click += Button2_Click;
            button2.Text = "module";
            button3 = FindViewById<Button>(Resource.Id.button3);
            button3.Click += Button3_Click;
            button3.Text = "list";

            state = FindViewById<TextView>(Resource.Id.outputTV);
            state.Text = "init success\n";

            return 0;
        }

        private void Button3_Click(object sender, EventArgs e)
        {
            button3.Enabled = false;

            // read text
            Toast loading = Toast.MakeText(this, "this button is not used", ToastLength.Long);
            loading.Show();

            //Task<int> read = Module.ReadTotal();
            //int result = await read;
            //if(result==0)
            //    state.Text += "total read success\n";

            //button3.Enabled = true;
        }

        private async void Button2_Click(object sender, EventArgs e)
        {
            button2.Enabled = false;
            alert.show("Alert", "you've clicked ");

            // read text
            Toast loading = Toast.MakeText(this, "loading...", ToastLength.Long);
            loading.Show();
            
            Task<int> read = Module.ReadModule("TotalHS.txt", 0);
            int result = await read;

            if (result == 0)
            {
                state.Text += "modul read success\n";
                for(int i=0; i<3; i++)
                    state.Text += Module.module.Keys.ToArray()[i]+"\n";
                state.Text += "...\n";
            }

            Task<int> list = Module.ReadTotal();
            result = await read;
            if(result==0)
                state.Text += "list read success\n";

            button2.Enabled = true;
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            state.Text += "select clicked\n";
            if (Module.module == null)
            {
                alert.show("Alert", "please make module first");
                return;
            }

            // make another activity
            Intent intent = new Intent(this, typeof(SelectActivity));

            // show
            StartActivity(intent);
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