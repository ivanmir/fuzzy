# Flask-Fuzzy Cloud Foundry Samples

A skfuzzy sample made with:

- Flask 
- NumPy 
- SciPy 
- MatPlotLib 
- SciKit-Fuzzy

The samples are an adaptation of the followin samples:

https://scikit-fuzzy.readthedocs.io/en/latest/auto_examples/plot_cmeans.html

This app uses the following buildpack:

https://github.com/trustedanalytics/scipy-python-buildpack

To push it to Cloud Foundry you will need to push it twice.

Comment scikit-fuzzy requitement and do a cf push.

After it installs all requirements, the application will fail.

Uncomment scikit-fuzzy requirement and do a cf push again.

Once this is done, the application will work.

Enjoy!
