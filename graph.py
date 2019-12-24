import matplotlib.pyplot as pl

def lineChart(xValues,yValues,xLabel,yLabel,ls,lw,color,marker,markersize,markercolor,title):
    xValues=eval(xValues)
    yValues = eval(yValues)

    pl.plot(xValues,yValues,ls=ls,linewidth=lw,color=color,marker=marker,markersize=markersize,markerfacecolor=markercolor)
    pl.title(title)
    pl.xlabel(xLabel)
    pl.ylabel(yLabel)

    pl.show()

def barChart(xLabel,yLabel,yValues,xValues,title,width=.8):

    pl.bar(eval(xValues),eval(yValues),width=width)

    pl.xlabel(xLabel)
    pl.ylabel(yLabel)
    pl.title(title)
    pl.show()
