# Prototype integration with ODA


Scientific context is constantly changing, modules which depend on the context are needed.

The modules (filters and science values) need to be near input LSST/ZTF stream, in the broker, but the context can be updated from elsewhere.

Certain platforms fetch known transients, and yield (basic) templates.

The science value / filter is to be derived in Fink in stages:

* upload time+locations, download parametric optical templates (possibly trivial), with ranges, per event class 
* match templates, produce (normalized) relevance ranks per class 
* filter outputs per class

In this context, in some cases, the optical templates can be trivial (e.g. "decaying"), so that only the location/time is matched.
