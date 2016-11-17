# python-crashcourse
Intro to Python 3 notebook and code sample. 

First you'll need to create a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) with the Python 3 dependencies defined in `requirements.txt`. 
Once you've activated the virtualenv you can:

### Run the notebook as slides

```jupyter nbconvert python_3_crash_course.ipynb --to slides --post serve```

If you want to customize the style of the notebook, simply override the `custom.css` file. The CSS included here is taken from [Dunovak's Jupyter Themes](https://github.com/dunovank/jupyter-themes/blob/master/jupyterthemes/styles/compiled/grade3.css).

### Run the notebook and edit

```jupyter notebook```

### Running the Python Twitter Sample

You'll need to grab Twitter credentials from [Twitter](http://apps.twitter.com) and fill them out at the top (in the "FILL ME IN" part :-) ) to make it work. 
