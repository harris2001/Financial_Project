#!/usr/bin/env python3

from flask import Flask, render_template
 
app = Flask(__name__, template_folder='/root/Desktop')

@app.route('/')
def main():
	return render_template("main.html")

@app.route('/main')
def homepage():

    title = "Epic Tutorials"
    paragraph = ["wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!","wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!"]

    #try:
    return render_template("index.html", title = title, paragraph=paragraph)
    #except Exception:
    #    return "Sorry try again later..."

@app.route('/about')
def aboutpage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/about/contact')
def contactPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)



@app.route('/graph1')
#def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	#chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	#series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	#title = {"text": 'My Title'}
	#xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	#yAxis = {"title": {"text": 'yAxis Label'}}
def graph1():
	return render_template("graph.html")#, chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
 


@app.route('/graph2')
def graph2():
	return render_template("graph2.html")



if __name__ == "__main__":
	app.run(debug = True, host='127.0.0.1', port=8080, passthrough_errors=True)

