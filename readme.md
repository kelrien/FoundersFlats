# HackToTheRoots: Founders Flat

## Setup
To run this project you need to have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [python 2.7+](http://askubuntu.com/questions/101591/how-do-i-install-python-2-7-2-on-ubuntu) and [pip](https://pip.pypa.io/en/stable/installing/) installed


1. clone the repository: `git clone https://github.com/kelrien/FoundersFlats.git`
2. get the requirements using pip: `pip install -r requirements.txt`
3. get your xing consumer key for your site: https://dev.xing.com/plugins/login_with/new
4. Edit templates/login.html and replace `"YOUR-XING-KEY"` with a valid consumer id
5. run `python setup.py`
6. run `python app.py` to start the flask server
7. Enjoy!
