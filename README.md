# Flask-Fuzzy Cloud Foundry Samples

A skfuzzy sample made with:

- Flask 1.0.2
- NumPy 1.12.1
- SciPy 1.2.0
- MatPlotLib 2.0.0
- SciKit-Fuzzy 0.4.0

The samples are an adaptation of the followin samples:

https://scikit-fuzzy.readthedocs.io/en/latest/auto_examples/plot_cmeans.html

~~This app uses the following buildpack:
https://github.com/trustedanalytics/scipy-python-buildpack
To push it to Cloud Foundry you will need to push it twice.
Comment scikit-fuzzy requitement and do a cf push.
After it installs all requirements, the application will fail.
Uncomment scikit-fuzzy requirement and do a cf push again.
Once this is done, the application will work.~~

>This project is now using miniconda to control the deployment of dependencies. Please take a look at the environment.yml

>Install miniconda on your environment to check your environment.yml file bore deploying. This ensures that the local conda environment reflects the one on Cloud Foundry. It may take more disk space in the cloud, but it is more guaranteed to work.

>Do not use the defaults conda repo! Use the conda-forge instead to minimize the file-system size. Also don't forget to include nomkl (this helps to reduce the overall size as well)

1) To create a local environment based on your yml file, use the following command:
```
conda env create -f environment.yml -n py3
```

2) If you update the environment file you can than update the local as well with this command:
```
conda env update -f environment.yml -n py3
```

3) Activate/Deactivate the py3 environment using this command:
```
conda activate py3
conda deactivate
```

4) Once conda is able to resolv all dependencies and your project runs locally, you can safely push your application to Cloud Foundry

Enjoy!
