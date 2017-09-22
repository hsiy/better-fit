#!/usr/bin/python

import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure

username = 'hsiy'
api_key = 'y1YXzt7TIsc7RRY2TMAb'
stream_token = ['2xc6yk9l09', 'euxrawpca5', 'ekbgwm6lcd']
py.sign_in(username, api_key)
trace1 = Scatter(
	name='X',
	x=[],
	y=[],
	stream=dict(
		token=stream_token[0],
		maxpoints=200
	)
)
trace2 = Scatter(
	name='Y',
	x=[],
	y=[],
	stream=dict(
		token=stream_token[1],
		maxpoints=200
	), 
	marker=dict(
		color='rgb(255,0,0)'
	)
)
trace3 = Scatter(
	name='Z',
	x=[],
	y=[],
	stream=dict(
		token=stream_token[2],
		maxpoints=200
	), 
	marker=dict(
		color='rgb(255,255,0)'
	)
)


layout = Layout(
	title='Raspberry Pi Streaming Sensor Data'
)

fig = Figure(data=[trace1,trace2,trace3], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')


stream1 = py.Stream(stream_token[0])
stream1.open()
stream2 = py.Stream(stream_token[1])
stream2.open()
stream3 = py.Stream(stream_token[2])
stream3.open()
t = 0

def displayValues(data, labels):
	global t
	if len(data) != len(labels):
		print 'Length of data and labels do not match'
		return

	stream1.write({'x': t, 'y': data[0]})
	stream2.write({'x': t, 'y': data[1]})
	stream3.write({'x': t, 'y': data[2]})
	t += 1


