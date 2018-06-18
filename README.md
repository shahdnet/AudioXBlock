AudioXBlock
===========

This is a simple XBlock which will play audio files as an HTML5 audio
element. If unavailable, it will fall back to an embed element.

Usage: 

    <audio src="http://server.tld/static/song.mp3" />


**NOTE:** When you installed AudioXBlock using the latest [xblock installation manuall][1]
you have to add it to the INSTALLED_APPS. While there are a few different ways to do so, the easiest is this:

Add or edit the following line in your setting files ( both lms.env.json and cms.env.json ):

```
    "ADDL_INSTALLED_APPS": ["audio"],
```

[1]: http://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/install_xblock.html
