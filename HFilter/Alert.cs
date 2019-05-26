using Android.App;
using Android.Content;
using System;

namespace HFilter
{
    class Alert
    {
        Context context;

        public Alert(Context context)
        {
            this.context = context;
            
        }

        // create alert and show dialog
        public void show(string title, string message, string[] buttons = null,
            EventHandler<DialogClickEventArgs>[] eventHandlers=null
            )
        {
            // do nothing
            if(eventHandlers==null && buttons == null)
            {
                buttons = new string[1];
                buttons[0] = "ok";
                eventHandlers = new EventHandler<DialogClickEventArgs>[1];
                eventHandlers[0] = delegate { };
            }
            // error
            if (buttons.Length != eventHandlers.Length) return;

            AlertDialog.Builder alert = new Android.App.AlertDialog.Builder(context);
            alert.SetTitle(title);
            alert.SetMessage(message);
            for (int i = 0; i < buttons.Length; i++)
            {
                alert.SetPositiveButton(buttons[i], eventHandlers[i]);
            }

            //alert.Show();
            Dialog dialog = alert.Create();
            dialog.Show();
        }
    }
}