using Android.Content;
using Android.Util;
using Android.Views;
using HFilter;
using HFilter.Droid;
using Xamarin.Forms;
using Xamarin.Forms.Platform.Android;

[assembly: ExportRenderer(typeof(CustomView), typeof(CustomView_android))]

namespace HFilter.Droid
{
    public class CustomView_android : ViewRenderer<CustomView, Android.Widget.DatePicker>
    {
        protected override void OnElementChanged(ElementChangedEventArgs<CustomView> e)
        {
            base.OnElementChanged(e);

            var datePicker = new Android.Widget.DatePicker(Forms.Context);

            SetNativeControl(datePicker);
        }
    }
}