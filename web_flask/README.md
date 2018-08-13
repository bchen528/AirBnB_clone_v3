## Web Framework
> In the backend, we use Flask as the web framework and Jinja as the template.

### Resources:
* [What is a web framework?](https://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)
* [Flask - Quickstart: Minimal Application, Routing except HTTP methods, Rendering templates](http://flask.pocoo.org/docs/1.0/quickstart/)
* [Jinja - Template Designer: Synopsis, Variables, Comments, Whitespace control, List of Control Structures (read up to Call)](http://jinja.pocoo.org/docs/2.9/templates/)

### Description of what each file shows:
* File 6 is cummulative from 0 onwards. The simple web-app file 6 shows how to use Flask to map what we see at each route, which html pages, and how to customize the html templates using Jinja. Each file can be run with ```python -m [dirname].[filename]```. This results in ```* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)```. To test the web app is running, for instance, in another terminal we can run ```curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""``` and should see the return value of our routes. 

* File 7 updates FileStorage and DBStorage with a close method. File 8 ___ File 9 ___ File 10 __

### Environment
* Languages: Python 3.4.3, HTML, CSS
* OS: Ubuntu 14.04 LTS
* Framework: Flask ```pip3 install flask```
* Style guidelines: [W3C-Validator](https://github.com/holbertonschool/W3C-Validator) || [PEP 8 (version 1.7) for Python 3.5](https://www.python.org/dev/peps/pep-0008/) || [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)