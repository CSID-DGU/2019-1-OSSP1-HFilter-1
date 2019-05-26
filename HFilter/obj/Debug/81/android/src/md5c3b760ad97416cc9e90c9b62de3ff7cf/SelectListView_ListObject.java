package md5c3b760ad97416cc9e90c9b62de3ff7cf;


public class SelectListView_ListObject
	extends java.lang.Object
	implements
		mono.android.IGCUserPeer
{
/** @hide */
	public static final String __md_methods;
	static {
		__md_methods = 
			"";
		mono.android.Runtime.register ("HFilter.SelectListView+ListObject, HFilter", SelectListView_ListObject.class, __md_methods);
	}


	public SelectListView_ListObject ()
	{
		super ();
		if (getClass () == SelectListView_ListObject.class)
			mono.android.TypeManager.Activate ("HFilter.SelectListView+ListObject, HFilter", "", this, new java.lang.Object[] {  });
	}

	private java.util.ArrayList refList;
	public void monodroidAddReference (java.lang.Object obj)
	{
		if (refList == null)
			refList = new java.util.ArrayList ();
		refList.add (obj);
	}

	public void monodroidClearReferences ()
	{
		if (refList != null)
			refList.clear ();
	}
}
