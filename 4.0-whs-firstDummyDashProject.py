import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
	html.H1('HelloDashell!'),
	html.Div('Dash: Web Dashals for Dashells'),
	dcc.Graph(id='example',
		figure={'data': [			
			{'X':[1,2,3], 'y':[2,4,5], 'type': 'bar', 'name': 'WAS1'},
			{'X':[1,2,3], 'y':[2,8,9], 'type': 'bar', 'name': 'WAS2'}
			],

				'layout': {
				'title': 'Plots Bitch'
				}
		}	
	)])

if __name__ == '__main__':
	app.run_server()