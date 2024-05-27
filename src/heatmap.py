'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template


def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    fig = px.imshow(
        data, 
        x=data.columns, 
        y=data.index, 
        labels=dict(
            x='Year',
            y='Neighborhood',
            colortitle='Trees'
        )
    )
    
    fig.update_layout(
        dragmode=False,
        xaxis=dict(
            tickmode='array',
            tickvals=data.columns,
            ticktext=data.columns.year
        ),
        coloraxis=dict(colorbar=dict(title='Trees'))
        # The coloraxis parameter creates the side bar showing the scale of the color on the left side
    )
    fig.update_traces(
        hovertemplate=hover_template.get_heatmap_hover_template()
    )
    return fig
